<div align="center">
  <h1>🚗 Driver Drowsiness Detection System</h1>
  <p><b>Real-Time Eye Aspect Ratio (EAR) based Driver Safety System</b></p>

  <!-- Badges -->
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-Computer_Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/dlib-Facial_Landmarks-008000?style=for-the-badge" alt="dlib">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</div>

<br />

## 📖 Overview
This is a **Real-Time Driver Drowsiness Detection System** built using Python, OpenCV, and EAR (Eye Aspect Ratio) based facial landmark detection.

The system continuously monitors the eye aspect ratio from a live webcam video stream. When the EAR value drops below a specific threshold for a certain duration, it indicates that the driver's eyes are closing (drowsiness). An alarm is then triggered to alert the driver and help prevent accidents.

## ✨ Features
- ✅ **Real-time detection** using Eye Aspect Ratio (EAR)
- ✅ **Facial landmark detection** via `dlib`
- ✅ **Continuous tracking** (detects prolonged eye closure, not just single blinks)
- ✅ **Audible alarm system** to instantly alert the driver
- ✅ **Plug-and-play** with any standard webcam

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

## ⚙️ Project Flow

```text
[ Webcam Feed ] 
      │
      ▼
[ Face & Eye Detection ] (dlib 68 Landmarks)
      │
      ▼
[ Compute EAR ] (Eye Aspect Ratio)
      │
      ▼
[ Track EAR continuously over frames ]
      │
      ▼
[ EAR < Threshold for N frames? ] ──(Yes)──► [ 🚨 Trigger Alarm ]
      │
     (No)
      │
      ▼
[ Continue Monitoring ]
