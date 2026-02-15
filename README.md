# 🎨 Computer Vision Playground

An interactive Computer Vision Playground built using OpenCV, Gradio, and Python. This project provides multiple real-world computer vision applications in a clean, minimal, and professional interface.

---

## 🚀 Features

This playground includes multiple powerful computer vision tools:

### 👤 Face Detection
- Detects human faces in images
- Uses Haar Cascade Classifier
- Displays bounding boxes around faces
- Shows total number of faces detected

### 👁️ Face and Eye Detection
- Detects faces and eyes simultaneously
- Uses optimized cascade detection
- Accurate ROI-based eye detection

### 📹 Real-time Webcam Detection
- Live face and eye detection using webcam
- Real-time processing
- Efficient and fast detection pipeline

### 🚶 Pedestrian Detection (Video)
- Detects full human bodies in videos
- Processes complete video frame-by-frame
- Generates output video with detection boxes
- Shows average pedestrian count

### ✏️ Image Sketch Generator
- Converts images into pencil sketches
- Adjustable blur intensity
- Uses image division technique for realistic sketch effect

---

## 🧠 Technologies Used

- Python
- OpenCV
- Gradio
- NumPy
- PIL (Python Imaging Library)

---

## 🧪 How It Works

This project uses Haar Cascade Classifiers to detect:

- Faces
- Eyes
- Full Body (Pedestrians)

Processing Pipeline:

1. Input Image / Video / Webcam
2. Convert to Grayscale
3. Apply Cascade Detection
4. Draw Bounding Boxes
5. Display Output via Gradio Interface

---

