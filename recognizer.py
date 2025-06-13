import cv2
import os

os.makedirs('dataset', exist_ok=True)

cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
if not os.path.exists(cascade_path):
    print("[ERROR] Haar cascade file not found at", cascade_path)
    print("Download it from: https://github.com/opencv/opencv/tree/master/data/haarcascades")
    exit(1)
face_detector = cv2.CascadeClassifier(cascade_path)

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("[ERROR] Could not open webcam. Try changing cv2.VideoCapture(0) to (1) or (2).")
    exit(1)
cam.set(3, 640)
cam.set(4, 480)

user_name = input('\nEnter user name and press <Enter>: ')
if not user_name.strip():
    print("[ERROR] User name cannot be empty.")
    cam.release()
    exit(1)

face_id = input('Enter user ID (e.g., 1, 2) and press <Enter>: ')
try:
    face_id = int(face_id)
except ValueError:
    print("[ERROR] User ID must be a number.")
    cam.release()
    exit(1)

user_dir = os.path.join('dataset', f"User.{face_id}.{user_name}")
os.makedirs(user_dir, exist_ok=True)

existing_image_count = 0
if os.listdir(user_dir):
    print(f"\n[WARNING] User '{user_name}' already exists.")
    print("[1] Overwrite - Delete existing images and start fresh")
    print("[2] Append - Add more images to existing data")
    print("[3] Cancel - Exit without changes")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == '1':
        # Overwrite - delete all existing files
        for file in os.listdir(user_dir):
            file_path = os.path.join(user_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print(f"[INFO] Existing data for '{user_name}' cleared.")
    elif choice == '2':
        # Append - find the highest numbered image to continue from there
        existing_images = [f for f in os.listdir(user_dir) if f.endswith('.jpg') or f.endswith('.png')]
        if existing_images:
            existing_image_numbers = [int(os.path.splitext(img)[0]) for img in existing_images if os.path.splitext(img)[0].isdigit()]
            if existing_image_numbers:
                existing_image_count = max(existing_image_numbers)
                print(f"[INFO] Found {existing_image_count} existing images. Will append new images.")
    else:
        print("[INFO] Operation cancelled. Exiting.")
        cam.release()
        exit(0)

print(f"\n[INFO] Initializing face capture for {user_name}. Look at the camera and wait...")
print("[INFO] Ensure good lighting and face the camera directly. Press ESC to exit early.")

count = existing_image_count
max_images = existing_image_count + 30  # Capture 30 new images

while count < max_images:
    ret, img = cam.read()
    if not ret:
        print("[ERROR] Failed to capture image from webcam.")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1
        image_path = os.path.join(user_dir, f"{count}.jpg")
        cv2.imwrite(image_path, cv2.equalizeHist(gray[y:y+h, x:x+w]))
        print(f"[INFO] Captured image {count}/{max_images} for {user_name}")

    cv2.imshow('Face Capture', img)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        print("[INFO] Exited early by user.")
        break

print(f"\n[INFO] Captured {count-existing_image_count} new images for {user_name} (ID: {face_id}).")
print(f"[INFO] Total images: {count}. Exiting.")
cam.release()
cv2.destroyAllWindows()
