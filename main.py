import cv2
import dlib
import numpy as np
import threading
import platform
import tkinter as tk
from tkinter import messagebox
from scipy.spatial import distance as dist
import os

# --- Configuration ---
MODEL_PATH = "shape_predictor_68_face_landmarks.dat"
EAR_THRESHOLD = 0.25
CONSEC_FRAMES = 20

# --- Cross-Platform Alarm ---
def play_alarm():
    """Plays a system beep cross-platform."""
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(2500, 1000)
    else:
        # Mac/Linux fallback
        print('\a') 

def calculate_ear(eye):
    """Calculates the Eye Aspect Ratio (EAR)."""
    # Compute the euclidean distances between the two sets of vertical eye landmarks
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    # Compute the euclidean distance between the horizontal eye landmark
    C = dist.euclidean(eye[0], eye[3])
    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)
    return ear

def start_detection():
    """Starts the main video capture and drowsiness detection loop."""
    
    # Initialize dlib's face detector and facial landmark predictor
    print("[INFO] Loading facial landmark predictor...")
    if not os.path.exists(MODEL_PATH):
        messagebox.showerror("Error", f"Missing model file: {MODEL_PATH}\nPlease download it and place it in the same folder.")
        return

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(MODEL_PATH)

    # Grab the indexes of the facial landmarks for the left and right eye
    (lStart, lEnd) = (42, 48)
    (rStart, rEnd) = (36, 42)

    print("[INFO] Starting video stream...")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not access camera.")
        return

    counter = 0
    alarm_on = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)

        for rect in rects:
            shape = predictor(gray, rect)
            shape = np.array([(shape.part(i).x, shape.part(i).y) for i in range(68)])

            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]

            leftEAR = calculate_ear(leftEye)
            rightEAR = calculate_ear(rightEye)
            ear = (leftEAR + rightEAR) / 2.0

            # Draw eye contours
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            if ear < EAR_THRESHOLD:
                counter += 1
                if counter >= CONSEC_FRAMES:
                    cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    if not alarm_on:
                        threading.Thread(target=play_alarm, daemon=True).start()
                        alarm_on = True
            else:
                counter = 0
                alarm_on = False

        cv2.imshow("Driver Drowsiness Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def show_info():
    messagebox.showinfo("Instructions", "1. Ensure your face is well-lit.\n2. Press 'q' in the video window to stop.")

# --- Tkinter GUI ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Driver Alertness System")
    root.geometry("300x200")

    label = tk.Label(root, text="Driver Drowsiness Detection", font=("Arial", 12, "bold"))
    label.pack(pady=10)

    start_button = tk.Button(root, text="Start Detection", command=start_detection, bg="green", fg="white")
    start_button.pack(pady=5)

    info_button = tk.Button(root, text="Instructions", command=show_info)
    info_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white")
    exit_button.pack(pady=10)

    root.mainloop()
