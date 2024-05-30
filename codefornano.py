# pip install mediapipe opencv-python

import cv2
import mediapipe as mp

def get_gesture(hand_landmarks):
    Wrist = [hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x,hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y]
    Thumb_cmc = [hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x,hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y]
    Thumb_mcp = [hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x,hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y]
    Thumb_ip = [hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x,hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y]
    Thumb_tip = [hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y]
    Index_mcp = [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x,hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y]
    Index_pip = [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y]
    Index_dip = [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y]
    Index_tip = [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y]
    Middle_mcp = [hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x,hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y]
    Middle_pip = [hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y]
    Middle_dip = [hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y]
    Middle_tip = [hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y]
    ring_mcp = [hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x,hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y]
    ring_pip = [hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y]
    ring_dip = [hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y]
    ring_tip = [hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y]
    pinky_mcp = [hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x,hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y]
    pinky_dip = [hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y]
    pinky_pip = [hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y]
    pinky_tip = [hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y]

    mcp_delta_y = abs(pinky_mcp[1] - Index_mcp[1])
    wrist_to_mcp_y = abs(Middle_mcp[1] - Wrist[1])
    wrist_to_mcp_x = abs(Middle_mcp[0] - Wrist[0])
    hands_orient_param = mcp_delta_y/wrist_to_mcp_y
    orient_ratio = wrist_to_mcp_x/wrist_to_mcp_y

    hands_x_side = Wrist[0] - Middle_mcp[0]
    tip_mcp_middle_delta_y = Middle_tip[1]-Middle_mcp[1]
    tip_mcp_middle_delta_x = Middle_tip[0]-Middle_mcp[0]
    
    tip_mcp_index_delta_y = Index_tip[1] - Index_mcp[1]
    tip_mcp_index_delta_x = Index_tip[0] - Index_mcp[0]
    
    tip_pip_middle_delta_x =Middle_tip[0]-Middle_pip[0]
    tip_pip_index_delta_x = Index_tip[0]-Index_pip[0]

    if tip_mcp_middle_delta_y >0 and tip_mcp_index_delta_y<0 and orient_ratio <0.5:
        return "pointing up"
        
    elif tip_pip_index_delta_x<0 and orient_ratio >0.5:
        return "pointing right"
    
    elif tip_pip_index_delta_x>0 and orient_ratio > 0.5:
        return "pointing left"
    
    else:
        return "None"

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    model_complexity=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

print("camera capture started")

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    # draw landmarks on hands
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
            )

            print(get_gesture(hand_landmarks))
        
# cleanup
cap.release()