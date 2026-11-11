## 📖 Overview

This is a **Real-Time Driver Drowsiness Detection System** built using Python, OpenCV, and EAR (Eye Aspect Ratio) based facial landmark detection.

The system continuously monitors the eye aspect ratio from a live webcam video stream. When the EAR value drops below a specific threshold for a sustained duration, it indicates that the driver's eyes are closing (drowsiness). An alarm is then triggered to alert the driver and help prevent accidents.

## ✨ Features

- ✅ **Real-time detection** using Eye Aspect Ratio (EAR)
- ✅ **Facial landmark detection** via `dlib` (68-point model)
- ✅ **Continuous tracking** (detects prolonged eye closure, not just single blinks)
- ✅ **Audible alarm system** to instantly alert the driver
- ✅ **Plug-and-play** compatibility with any standard webcam

## 🛠️ Tech Stack & Libraries

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core programming language |
| **OpenCV** | Real-time video capture and image processing |
| **dlib** | 68-point facial landmark detection |
| **SciPy** | Calculating Euclidean distance for EAR |
| **winsound** | Triggering the alarm system (Windows) |
| **Tkinter** | (Optional) GUI display |
| **NumPy** | Array and matrix operations |

## ⚙️ System Architecture & Project Flow

```text
[ Webcam Feed ]
      │
      ▼
[ Face & Eye Detection ] ── (dlib 68 Landmarks)
      │
      ▼
[ Compute EAR ] ── (Eye Aspect Ratio)
      │
      ▼
[ Track EAR continuously over frames ]
      │
      ▼
[ Is EAR < Threshold for N frames? ]
      │
 ┌────┴────┐
Yes        No
 │          │
 ▼          ▼
[🚨 Alarm]  [Continue Monitoring]
