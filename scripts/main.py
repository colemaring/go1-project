import cv2
import mediapipe as mp
import gestures
from collections import deque

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    model_complexity=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Initialize MediaPipe Drawing
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize deque to store last 10 gestures
gesture_history = deque(maxlen=30)

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

            # Get the current gesture
            current_gesture = gestures.get_gesture(hand_landmarks)
            gesture_history.append(current_gesture)

            # Print the majority gesture if history is full
            if len(gesture_history) == gesture_history.maxlen:
                majority_gesture = max(set(gesture_history), key=gesture_history.count)
                print(majority_gesture)

                # Write the majority gesture to the file
                with open("../command.txt", "w") as file:
                    file.write(majority_gesture)

    # Display the image with landmarks
    cv2.imshow('Hand Tracking', image)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
