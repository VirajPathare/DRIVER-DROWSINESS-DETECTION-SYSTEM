# 🚗 Driver Drowsiness Detection System

**Real-Time Driver Safety & Computer Vision Solution**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![dlib](https://img.shields.io/badge/dlib-19.x-008080)](http://dlib.net/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 📖 Overview

The **Driver Drowsiness Detection System** is a real-time safety application built using Python and Computer Vision. It continuously monitors a driver's eyes via a live webcam feed. By calculating the **Eye Aspect Ratio (EAR)**, it detects signs of fatigue and triggers an immediate alarm if prolonged eye closure is observed, preventing potential accidents.

---

## ✨ Key Features

- ⚡ **Real-Time Detection** — Fast, frame-by-frame analysis using Eye Aspect Ratio (EAR).
- 👁️ **Facial Landmark Tracking** — Powered by dlib's 68-point facial landmark predictor.
- 🔄 **Continuous Monitoring** — Distinguishes between normal blinks and dangerous prolonged eye closure.
- 🚨 **Instant Alert System** — Triggers a loud, audible alarm to wake the driver.
- 🔌 **Hardware Agnostic** — Instantly works with any standard built-in or USB webcam.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Language** | Python | Core programming language |
| **Vision** | OpenCV | Real-time video capture and processing |
| **AI / ML** | dlib | 68-point facial landmark detection |
| **Math** | NumPy / SciPy | Euclidean distance calculations for EAR |
| **Audio** | winsound / playsound | Alarm trigger (Windows/Cross-platform) |
| **GUI** | OpenCV HighGUI | Graphical display |

---

## ⚙️ System Architecture

```text
┌─────────────────┐    ┌──────────────────┐    ┌───────────────────┐
│  Webcam Feed    │───▶│  Face Detection  │───▶│  Landmark Predict │
│  (OpenCV)       │    │  (dlib HOG)      │    │  (68 points)      │
└─────────────────┘    └──────────────────┘    └─────────┬─────────┘
                                                         │
                                                         ▼
┌─────────────────┐    ┌──────────────────┐    ┌───────────────────┐
│  Alarm Trigger  │◀───│  Fatigue Logic   │◀───│  EAR Calculation  │
│  (winsound)     │    │  (frame counter) │    │  (6-point eyes)   │
└─────────────────┘    └──────────────────┘    └───────────────────┘
