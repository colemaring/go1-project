import cv2
import mediapipe as mp
import math
import gestures
import sys
import time

sys.path.append('../lib/python/amd64')
import robot_interface as sdk

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    model_complexity=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

HIGHLEVEL = 0xee
LOWLEVEL  = 0xff

udp = sdk.UDP(HIGHLEVEL, 8080, "192.168.12.1", 8082)

cmd = sdk.HighCmd()
state = sdk.HighState()
udp.InitCmdData(cmd)

# Initialize MediaPipe Drawing
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Convert the BGR image to RGB.
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and find hands
    results = hands.process(image_rgb)

    # Draw hand landmarks on the image
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
            )

            udp.Recv()
            udp.GetRecv(state)

            cmd.mode = 0      # 0:idle, default stand      1:forced stand     2:walk continuously
            cmd.gaitType = 0
            cmd.speedLevel = 0
            cmd.footRaiseHeight = 0
            cmd.bodyHeight = 0
            cmd.euler = [0, 0, 0]
            cmd.velocity = [0, 0]
            cmd.yawSpeed = 0.0
            cmd.reserve = 0

            current_gesture = gestures.get_gesture(hand_landmarks)
            print(current_gesture)

            if (current_gesture == "pointing up"):
                cmd.mode = 5

            elif (current_gesture == "pointing right"):
                cmd.mode = 12

            elif (current_gesture == "pointing left"):
                cmd.mode = 13

            else:
                cmd.mode = 1

            udp.SetSend(cmd)
            udp.Send()

# Release the webcam and close all OpenCV windows
cap.release()