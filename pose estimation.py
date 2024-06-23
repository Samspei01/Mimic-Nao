import cv2
import mediapipe as mp
import numpy as np

class Body:
    class Side:
        def __init__(self, landmarks):
            self.shoulder = landmarks[0]
            self.elbow = landmarks[1]
            self.wrist = landmarks[2]

    def __init__(self, landmarks):
        self.nose = landmarks[0]
        self.left_eye_inner = landmarks[1]
        self.right_eye_inner = landmarks[4]
        self.left = self.Side([landmarks[11], landmarks[13], landmarks[15]])  # Left shoulder, elbow, wrist
        self.right = self.Side([landmarks[12], landmarks[14], landmarks[16]]) # Right shoulder, elbow, wrist

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if not ret:
        break
    img = cv2.resize(img, (800, 600))

    
    results = pose.process(img)

    if results.pose_landmarks:
        mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        body = Body(results.pose_landmarks.landmark)

        right_shoulder_x = body.right.shoulder.x
        right_shoulder_y = body.right.shoulder.y
        right_shoulder_z = body.right.shoulder.z
        right_elbow_x = body.right.elbow.x
        right_elbow_y = body.right.elbow.y
        right_elbow_z = body.right.elbow.z

        right_wrist_x = body.right.wrist.x
        right_wrist_y = body.right.wrist.y
        right_wrist_z = body.right.wrist.z

        left_shoulder_x = body.left.shoulder.x
        left_shoulder_y = body.left.shoulder.y
        left_shoulder_z = body.left.shoulder.z
        left_elbow_x = body.left.elbow.x
        left_elbow_y = body.left.elbow.y
        left_elbow_z = body.left.elbow.z

        left_wrist_x = body.left.wrist.x
        left_wrist_y = body.left.wrist.y
        left_wrist_z = body.left.wrist.z

        output_filename = 'output_file.txt'

        
        with open(output_filename, 'w') as outfile:

            outfile.write(f"Right Shoulder: x={right_shoulder_x}, y={right_shoulder_y}, z={right_shoulder_z}\n")
            outfile.write(f"Right Elbow: x={right_elbow_x}, y={right_elbow_y}, z={right_elbow_z}\n")
            outfile.write(f"Right Wrist: x={right_wrist_x}, y={right_wrist_y}, z={right_wrist_z}\n")

            outfile.write(f"left Shoulder: x={left_shoulder_x}, y={left_shoulder_y}, z={left_shoulder_z}\n")
            outfile.write(f"left Elbow: x={left_elbow_x}, y={left_elbow_y}, z={left_elbow_z}\n")
            outfile.write(f"left Wrist: x={left_wrist_x}, y={left_wrist_y}, z={left_wrist_z}\n")



            cv2.imshow("Pose Estimation", img)

            if cv2.waitKey(1) == ord('q'):
                break

cv2.destroyAllWindows()
cap.release()
