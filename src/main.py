import cv2
import threading
import tkinter as tk
from tkinter import messagebox
from alarm import play_alarm
from detector import DrowsinessDetector

# --- Configuration ---
EAR_THRESHOLD = 0.25
MAR_THRESHOLD = 0.6
CONSEC_FRAMES = 20

def start_detection():
    detector = DrowsinessDetector()
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not access camera.")
        return

    counter = 0
    yawn_counter = 0
    alarm_on = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))
        ear, mar, landmarks = detector.process_frame(frame)

        if ear is not None and mar is not None:
            if ear < EAR_THRESHOLD:
                counter += 1
            else:
                counter = 0

            if mar > MAR_THRESHOLD:
                yawn_counter += 1
            else:
                yawn_counter = 0

            if counter >= CONSEC_FRAMES or yawn_counter >= CONSEC_FRAMES:
                cv2.putText(frame, "DROWSINESS ALERT!", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                if not alarm_on:
                    threading.Thread(target=play_alarm, daemon=True).start()
                    alarm_on = True
            else:
                alarm_on = False

            # Draw landmarks
            left_eye, right_eye, mouth = landmarks
            for pt in left_eye + right_eye:
                cv2.circle(frame, pt, 2, (0, 255, 0), -1)
            for pt in mouth:
                cv2.circle(frame, pt, 2, (255, 0, 0), -1)

        cv2.imshow("Driver Drowsiness Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Driver Alertness System")
    root.geometry("300x200")
    
    tk.Label(root, text="AI Driver Safety", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Button(root, text="Start Detection", command=start_detection, bg="green", fg="white").pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white").pack(pady=10)
    
    root.mainloop()
