import mediapipe as mp

mp_hands = mp.solutions.hands

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

    elif tip_mcp_middle_delta_y < 0 and tip_mcp_index_delta_y > 0 and orient_ratio < 0.5:
        return "pointing down"
    elif abs(Thumb_tip[1] - Wrist[1]) > 0.2 and abs(Index_tip[1] - Wrist[1]) > 0.2 and abs(Middle_tip[1] - Wrist[1]) > 0.2 and abs(ring_tip[1] - Wrist[1]) > 0.2 and abs(pinky_tip[1] - Wrist[1]) > 0.2:
        return "hand open"
    elif abs(Index_tip[1] - Index_mcp[1]) > 0.2 and abs(pinky_tip[1] - pinky_mcp[1]) > 0.2 and abs(Middle_tip[1] - Middle_mcp[1]) < 0.1 and abs(ring_tip[1] - ring_mcp[1]) < 0.1:
        return "rock n roll"
    elif abs(Index_tip[1] - Index_mcp[1]) > 0.2 and abs(Middle_tip[1] - Middle_mcp[1]) > 0.2 and abs(ring_tip[1] - ring_mcp[1]) > 0.2 and abs(Thumb_tip[1] - Wrist[1]) < 0.1 and abs(pinky_tip[1] - Wrist[1]) < 0.1:
        return "number 3"
    elif abs(Index_tip[1] - Index_mcp[1]) > 0.2 and abs(Middle_tip[1] - Middle_mcp[1]) > 0.2 and abs(ring_tip[1] - ring_mcp[1]) < 0.1 and abs(pinky_tip[1] - pinky_mcp[1]) < 0.1:
        return "peace"
    
    else:
        return "None"
