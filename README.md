# Driver Drowsiness Detection System

This is a Real-Time Driver Drowsiness Detection system built using Python, OpenCV & EAR (Eye Aspect Ratio) based facial landmark detection.

The system continuously monitors eye aspect ratio from live webcam video stream. When the EAR value drops below threshold for certain duration, it means eyes are closing / drowsiness. Then an alarm is triggered to alert the driver and help prevent accidents.

---

## Features
- Real-time drowsiness detection using Eye Aspect Ratio (EAR)
- Uses facial landmark detection method
- Detects closed eyes continuously (not just single blink)
- Alerts driver with sound alarm
- Works live with any webcam

---

## Tech Stack & Libraries Used
- Python
- OpenCV
- dlib (for facial landmarks)
- winsound (alert alarm)
- tkinter (GUI display if needed)
- numpy

---

## Project Flow
1. Capture webcam frames
2. Detect eyes using facial landmarks
3. Compute EAR (Eye Aspect Ratio)
4. Track EAR value continuously
5. If EAR < Threshold for continuous frames → Drowsiness detected
6. Trigger Alarm

---

## How To Run

### 1) Install Dependencies

### 2) Run Project

> Replace `main.py` with your running file name (the file which starts the program)

---

## Demo

Demo images & video are inside the repository.

---

## Future Improvements
- Add yawning detection
- Add head pose estimation
- Add mobile version with mediapipe
- Add online dashboard analytics

---

## Credits
Developed as Driver Safety & Computer Vision project.
