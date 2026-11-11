<div align="center">
  <img src="https://img.icons8.com/color/96/000000/car--v1.png" width="80" alt="Car Icon"/>
  <h1>Driver Drowsiness Detection System</h1>
  <p><b>Real-Time Driver Safety & Computer Vision Solution</b></p>

  <!-- Badges -->
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://opencv.org/"><img src="https://img.shields.io/badge/OpenCV-Computer_Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"></a>
  <a href="http://dlib.net/"><img src="https://img.shields.io/badge/dlib-Facial_Landmarks-008000?style=for-the-badge" alt="dlib"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License"></a>
</div>

<br />

> **Overview:** The Driver Drowsiness Detection System is a real-time safety application built using Python and Computer Vision. It continuously monitors a driver's eyes via a live webcam feed. By calculating the **Eye Aspect Ratio (EAR)**, it detects signs of fatigue and triggers an immediate alarm if prolonged eye closure is observed, preventing potential accidents.

## ✨ Key Features

- **Real-Time Detection** — Fast, frame-by-frame analysis using Eye Aspect Ratio (EAR).
- **Facial Landmark Tracking** — Powered by `dlib`'s 68-point facial landmark predictor.
- **Continuous Monitoring** — Distinguishes between normal blinks and dangerous prolonged eye closure.
- **Instant Alert System** — Triggers a loud, audible alarm to wake the driver.
- **Hardware Agnostic** — Instantly works with any standard built-in or USB webcam.

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Language** | <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" height="20"> | Core programming language |
| **Vision** | <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" height="20"> | Real-time video capture and processing |
| **AI / ML** | <img src="https://img.shields.io/badge/dlib-008000?style=flat-square" height="20"> | 68-point facial landmark detection |
| **Math** | <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white" height="20"> | Euclidean distance calculations for EAR |
| **Audio** | <img src="https://img.shields.io/badge/winsound-grey?style=flat-square" height="20"> | Alarm trigger (Windows) |
| **GUI** | <img src="https://img.shields.io/badge/Tkinter-grey?style=flat-square" height="20"> | (Optional) Graphical display |

## ⚙️ System Architecture

```mermaid
graph TD
    A([Webcam Feed]) --> B[Face & Eye Detection]
    B -->|dlib 68 Landmarks| C[Compute EAR]
    C --> D[Track EAR over Frames]
    D --> E{Is EAR < Threshold?}
    
    E -->|No| G[Continue Monitoring]
    G --> A
    
    E -->|Yes| F[🚨 Trigger Alarm]
    F --> G
