"""
Computer Vision Playground - Minimal & Clean Code
Professional-grade implementation with best practices
"""

import gradio as gr
import cv2
import numpy as np
from PIL import Image
import tempfile

# Custom styling
CSS = """
.gradio-container {font-family: 'Inter', sans-serif;}
.main-header {text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
              color: white; border-radius: 15px; margin-bottom: 2rem;}
footer {display: none !important;}
"""

class CVApp:
    def __init__(self):
        """Initialize cascades"""
        self.face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        self.body = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
    
    def detect_faces(self, img):
        """Face detection in images"""
        if img is None: return None, "Upload image first"
        arr = np.array(img)
        gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
        faces = self.face.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(arr, (x, y), (x+w, y+h), (147, 20, 255), 3)
        
        return Image.fromarray(arr), f"✓ Found {len(faces)} face(s)"
    
    def detect_face_eye(self, img):
        """Face + Eye detection"""
        if img is None: return None, "Upload image first"
        arr = np.array(img)
        gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
        faces = self.face.detectMultiScale(gray, 1.3, 5)
        
        eyes = 0
        for (x, y, w, h) in faces:
            cv2.rectangle(arr, (x, y), (x+w, y+h), (255, 127, 0), 3)
            roi = gray[y:y+h, x:x+w]
            roi_c = arr[y:y+h, x:x+w]
            
            for (ex, ey, ew, eh) in self.eye.detectMultiScale(roi):
                eyes += 1
                cv2.rectangle(roi_c, (ex, ey), (ex+ew, ey+eh), (0, 255, 255), 2)
        
        return Image.fromarray(arr), f"✓ {len(faces)} face(s), {eyes} eye(s)"
    
    def webcam_detect(self, frame):
        """Real-time webcam detection"""
        if frame is None: return None
        arr = np.array(frame)
        gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
        
        for (x, y, w, h) in self.face.detectMultiScale(gray, 1.1, 6, minSize=(30, 30)):
            cv2.rectangle(arr, (x, y), (x+w, y+h), (255, 200, 0), 3)
            roi = gray[y:y+h, x:x+w]
            roi_c = arr[y:y+h, x:x+w]
            
            for (ex, ey, ew, eh) in self.eye.detectMultiScale(roi):
                cv2.rectangle(roi_c, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        
        return Image.fromarray(arr)
    
    def detect_pedestrians(self, video, progress=gr.Progress()):
        """Pedestrian detection in video"""
        if video is None: return None, "Upload video first"
        
        cap = cv2.VideoCapture(video)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        w, h = int(cap.get(3)), int(cap.get(4))
        total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        out_path = tempfile.mktemp(suffix='.mp4')
        out = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
        
        frame_num = 0
        detections = []
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret: break
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            bodies = self.body.detectMultiScale(gray, 1.2, 3, minSize=(50, 50))
            detections.append(len(bodies))
            
            for (x, y, w, h) in bodies:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
            
            out.write(frame)
            frame_num += 1
            if frame_num % 10 == 0: 
                progress(frame_num/total, f"Processing {frame_num}/{total}")
        
        cap.release()
        out.release()
        
        avg = sum(detections)/len(detections) if detections else 0
        return out_path, f"✓ Processed {frame_num} frames\nAvg: {avg:.1f} pedestrians"
    
    def create_sketch(self, img, blur=21):
        """Convert image to sketch"""
        if img is None: return None, "Upload image first"
        arr = np.array(img)
        gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
        inv = cv2.bitwise_not(gray)
        blur_img = cv2.GaussianBlur(inv, (blur, blur), 0)
        sketch = cv2.divide(gray, cv2.bitwise_not(blur_img), scale=256.0)
        return Image.fromarray(sketch), "✓ Sketch created"

# Initialize
app = CVApp()

# Build interface
with gr.Blocks(css=CSS, theme=gr.themes.Soft(), title="CV Playground") as demo:
    
    gr.HTML('<div class="main-header"><h1>🎨 Computer Vision Playground</h1><p>Your OpenCV Projects Hub</p></div>')
    
    with gr.Tabs():
        # Face Detection Tab
        with gr.Tab("👤 Face Detection"):
            with gr.Row():
                face_in = gr.Image(type="pil", label="Upload Image")
                face_out = gr.Image(label="Result")
            face_info = gr.Textbox(label="Info", show_label=False)
            gr.Button("Detect Faces", variant="primary").click(
                app.detect_faces, face_in, [face_out, face_info])
        
        # Face + Eye Tab
        with gr.Tab("👁️ Face + Eyes"):
            with gr.Row():
                fe_in = gr.Image(type="pil", label="Upload Image")
                fe_out = gr.Image(label="Result")
            fe_info = gr.Textbox(label="Info", show_label=False)
            gr.Button("Detect Both", variant="primary").click(
                app.detect_face_eye, fe_in, [fe_out, fe_info])
        
        # Webcam Tab
        with gr.Tab("📹 Webcam"):
            gr.Markdown("**Click Start below to activate camera**")
            with gr.Row():
                cam_in = gr.Image(sources=["webcam"], streaming=True, label="Camera")
                cam_out = gr.Image(label="Detection", streaming=True)
            cam_in.stream(app.webcam_detect, cam_in, cam_out)
        
        # Pedestrian Tab
        with gr.Tab("🚶 Pedestrian"):
            ped_in = gr.Video(label="Upload Video")
            ped_btn = gr.Button("Detect Pedestrians", variant="primary")
            ped_out = gr.Video(label="Result")
            ped_info = gr.Textbox(label="Info", show_label=False, lines=3)
            ped_btn.click(app.detect_pedestrians, ped_in, [ped_out, ped_info])
        
        # Sketch Tab
        with gr.Tab("✏️ Sketch"):
            with gr.Row():
                sk_in = gr.Image(type="pil", label="Upload Photo")
                sk_out = gr.Image(label="Sketch")
            sk_blur = gr.Slider(1, 99, 21, step=2, label="Blur Intensity")
            sk_info = gr.Textbox(label="Info", show_label=False)
            gr.Button("Create Sketch", variant="primary").click(
                app.create_sketch, [sk_in, sk_blur], [sk_out, sk_info])
    
    gr.Markdown("---\n**Tech:** OpenCV • Gradio • Python | **Ready to Use!** ✨")

if __name__ == "__main__":
    demo.launch()
