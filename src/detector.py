import cv2
import mediapipe as mp
import numpy as np
from scipy.spatial import distance as dist

class DrowsinessDetector:
    def __init__(self):
        # Initialize MediaPipe Face Mesh
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1, 
            refine_landmarks=True, 
            min_detection_confidence=0.5
        )
        
        # Landmark Indexes
        self.LEFT_EYE = [362, 385, 387, 263, 373, 380]
        self.RIGHT_EYE = [33, 160, 158, 133, 153, 144]
        self.MOUTH = [78, 81, 13, 311, 308, 402, 14, 178]

    def calculate_ear(self, eye):
        """Calculate Eye Aspect Ratio"""
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        C = dist.euclidean(eye[0], eye[3])
        return (A + B) / (2.0 * C)

    def calculate_mar(self, mouth):
        """Calculate Mouth Aspect Ratio (Yawning)"""
        A = dist.euclidean(mouth[2], mouth[10])
        B = dist.euclidean(mouth[4], mouth[8])
        C = dist.euclidean(mouth[0], mouth[6])
        return (A + B) / (2.0 * C)

    def process_frame(self, frame):
        """Processes the frame and returns EAR, MAR, and landmarks"""
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(frame_rgb)
        
        if not results.multi_face_landmarks:
            return None, None, None

        face_landmarks = results.multi_face_landmarks[0]
        h, w, _ = frame.shape
        mesh_coords = [(int(lm.x * w), int(lm.y * h)) for lm in face_landmarks.landmark]

        left_eye = [mesh_coords[i] for i in self.LEFT_EYE]
        right_eye = [mesh_coords[i] for i in self.RIGHT_EYE]
        mouth = [mesh_coords[i] for i in self.MOUTH]

        ear = (self.calculate_ear(left_eye) + self.calculate_ear(right_eye)) / 2.0
        mar = self.calculate_mar(mouth)

        return ear, mar, (left_eye, right_eye, mouth)
