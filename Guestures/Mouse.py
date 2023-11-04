import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize MediaPipe Drawing Utility
mp_drawing = mp.solutions.drawing_utils

# Initialize the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    # Flip the image horizontally for a selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB and process it with MediaPipe Hands
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Draw hand landmarks on the image
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the coordinates of the index finger tip
            x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1])
            y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0])

            # Move the mouse to the index finger tip position
            pyautogui.moveTo(x, y)

    # Display the image
    cv2.imshow('MediaPipe Hands', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV window
cap.release()
cv2.destroyAllWindows()
