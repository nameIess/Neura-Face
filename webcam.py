import cv2
import numpy as np
import os
import re

def debug_dataset_folders():
    dataset_dir = 'dataset'
    print("\n[DEBUG] Checking dataset directory structure:")
    if os.path.exists(dataset_dir):
        folders = os.listdir(dataset_dir)
        print(f"Found {len(folders)} items in dataset directory:")
        for item in folders:
            path = os.path.join(dataset_dir, item)
            if os.path.isdir(path):
                print(f"  - Directory: {item}")
                files = [f for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.png')]
                print(f"    Contains {len(files)} image files")
            else:
                print(f"  - File: {item}")
    else:
        print(f"Dataset directory '{dataset_dir}' does not exist!")
    print("")

def load_user_names():
    names = {0: 'None'}
    dataset_dir = 'dataset'
    
    if os.path.exists(dataset_dir):
        user_dirs = [d for d in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, d)) and d.startswith('User.')]
        
        for user_dir in user_dirs:
            match = re.match(r'User\.(\d+)\.(.+)', user_dir)
            if match:
                user_id = int(match.group(1))
                user_name = match.group(2)
                names[user_id] = user_name
    
    return names

if not os.path.exists('trainer/trainer.yml'):
    print("[ERROR] Trained model (trainer/trainer.yml) not found. Run trainer.py first.")
    exit(1)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
if not os.path.exists(cascade_path):
    print("[ERROR] Haar cascade file not found at", cascade_path)
    print("Download it from: https://github.com/opencv/opencv/tree/master/data/haarcascades")
    exit(1)
faceCascade = cv2.CascadeClassifier(cascade_path)

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("[ERROR] Could not open webcam. Try changing cv2.VideoCapture(0) to (1) or (2).")
    exit(1)
cam.set(3, 640)
cam.set(4, 480)
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

debug_dataset_folders()

names = load_user_names()
print(f"[INFO] Loaded {len(names)-1} users: {', '.join([f'{k}: {v}' for k, v in names.items() if k != 0])}")

font = cv2.FONT_HERSHEY_SIMPLEX
print("\n[INFO] Starting real-time face recognition. Press ESC to exit.")

while True:
    ret, img = cam.read()
    if not ret:
        print("[ERROR] Failed to capture image from webcam.")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        
        if confidence < 100:
            name = names.get(id, 'Unknown')
            confidence_text = f" ({round(100 - confidence)}%)"
            print(f"[MATCH] Recognized {name} (ID: {id}) with {round(100 - confidence)}% confidence")
        else:
            name = "Unknown"
            confidence_text = ""

        cv2.putText(img, f"{name}{confidence_text}", (x+5, y-5), font, 1, (255, 255, 255), 2)

    cv2.imshow('Face Recognition', img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

print("\n[INFO] Exiting Face Recognition")
cam.release()
cv2.destroyAllWindows()
