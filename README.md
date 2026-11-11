<div align="center">
  <h1>🚗 Driver Drowsiness Detection System</h1>
  <p><b>Real-Time Driver Safety using Computer Vision & Eye Aspect Ratio (EAR)</b></p>

  <!-- Badges -->
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-Computer_Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/dlib-Facial_Landmarks-008000?style=for-the-badge" alt="dlib">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</div>

<br />

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
| <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" height="20"> | Core programming language |
| <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" height="20"> | Real-time video capture and image processing |
| <img src="https://img.shields.io/badge/dlib-008000?style=flat-square" height="20"> | 68-point facial landmark detection |
| <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white" height="20"> | Calculating Euclidean distance for EAR |
| <img src="https://img.shields.io/badge/winsound-grey?style=flat-square" height="20"> | Triggering the alarm system (Windows) |
| <img src="https://img.shields.io/badge/Tkinter-grey?style=flat-square" height="20"> | (Optional) GUI display |
| <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" height="20"> | Array and matrix operations |

## ⚙️ System Architecture & Project Flow

```mermaid
graph TD
    A[Webcam Feed] --> B[Face & Eye Detection <br> dlib 68 Landmarks]
    B --> C[Compute EAR <br> Eye Aspect Ratio]
    C --> D[Track EAR continuously over frames]
    D --> E{Is EAR < Threshold <br> for N frames?}
    E -- Yes --> F[🚨 Trigger Alarm]
    E -- No --> G[Continue Monitoring]
    F --> G
