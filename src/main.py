import cv2
import threading
import tkinter as tk
from tkinter import messagebox
from alarm import play_alarm
from detector import DrowsinessDetector

# --- Configuration ---
EAR_THRESHOLD = 0.25   # If EAR drops below this, eyes are closed
MAR_THRESHOLD = 0.60   # If MAR goes above this, yawning
CONSEC_FRAMES = 20     # Number of frames (approx 1 second) before alarm

def start_detection():
    detector = DrowsinessDetector()
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not access camera.")
        return

    counter = 0
    yawn_counter = 0
    alarm_on = False

    print("Camera started! Press 'q' in the video window to quit.")

    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            continue

        # Flip the frame so it acts like a mirror
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (640, 480))
        
        try:
            ear, mar, landmarks = detector.process_frame(frame)
        except Exception:
            continue

        if ear is not None and mar is not None:
            # Print numbers to terminal so you can see the math working
            print(f"EAR: {ear:.2f} | MAR: {mar:.2f}")

            # Show numbers on the video feed
            cv2.putText(frame, f"EAR: {ear:.2f}", (500, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
            cv2.putText(frame, f"MAR: {mar:.2f}", (500, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

            # 1. Eye Logic
            if ear < EAR_THRESHOLD:
                counter += 1
            else:
                counter = 0

            # 2. Yawn Logic
            if mar > MAR_THRESHOLD:
                yawn_counter += 1
            else:
                yawn_counter = 0

            # 3. Trigger Alarm
            if counter >= CONSEC_FRAMES or yawn_counter >= CONSEC_FRAMES:
                cv2.putText(frame, "DROWSINESS ALERT!", (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                
                if not alarm_on:
                    print(">>> ALARM TRIGGERED! <<<")
                    threading.Thread(target=play_alarm, daemon=True).start()
                    alarm_on = True
            else:
                alarm_on = False

            # Draw the dots
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
