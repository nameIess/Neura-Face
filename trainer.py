import cv2
import numpy as np
from PIL import Image
import os
import re

if not os.path.exists('dataset'):
    print("[ERROR] Dataset folder not found. Run recognizer.py first.")
    exit(1)
os.makedirs('trainer', exist_ok=True)

cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
if not os.path.exists(cascade_path):
    print("[ERROR] Haar cascade file not found at", cascade_path)
    print("Download it from: https://github.com/opencv/opencv/tree/master/data/haarcascades")
    exit(1)
detector = cv2.CascadeClassifier(cascade_path)

def getImagesAndLabels(path):
    faceSamples = []
    ids = []
    user_dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and d.startswith('User.')]
    
    if not user_dirs:
        print("[ERROR] No user directories found in dataset folder. Run recognizer.py to capture images.")
        exit(1)
    
    print("\n[INFO] Found the following users:")
    for user_dir in user_dirs:
        match = re.match(r'User\.(\d+)\.(.+)', user_dir)
        if match:
            user_id, user_name = match.groups()
            print(f"  - ID: {user_id}, Name: {user_name}")
    
    for user_dir in user_dirs:
        match = re.match(r'User\.(\d+)\.(.+)', user_dir)
        if not match:
            continue
            
        user_id = int(match.group(1))
        user_path = os.path.join(path, user_dir)
        image_files = [f for f in os.listdir(user_path) if f.endswith('.jpg') or f.endswith('.png')]
        
        if not image_files:
            print(f"[WARNING] No images found for user directory: {user_dir}")
            continue
        
        for image_file in image_files:
            try:
                image_path = os.path.join(user_path, image_file)
                PIL_img = Image.open(image_path).convert('L')
                img_numpy = np.array(PIL_img, 'uint8')
                
                faces = detector.detectMultiScale(img_numpy, scaleFactor=1.1, minNeighbors=5)
                for (x, y, w, h) in faces:
                    faceSamples.append(img_numpy[y:y+h, x:x+w])
                    ids.append(user_id)
            except Exception as e:
                print(f"[WARNING] Skipping {image_path}: {str(e)}")
    
    if not faceSamples:
        print("[ERROR] No valid faces found in dataset images.")
        exit(1)
    
    return faceSamples, ids

print("\n[INFO] Training faces. This may take a few seconds...")
faces, ids = getImagesAndLabels('dataset')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(ids))

recognizer.write('trainer/trainer.yml')
print(f"\n[INFO] Trained {len(np.unique(ids))} faces. Model saved to trainer/trainer.yml")
