# 🥧 NeuraFace: Face Recognition System

**NeuraFace** is a powerful, open-source face recognition system that enables users to capture face images, train a recognition model, and perform real-time face identification using a webcam. Built with simplicity and efficiency in mind, NeuraFace is perfect for developers, hobbyists, and researchers exploring computer vision.

## 🌟 Features

- **Face Capture**: Seamlessly capture face images via webcam for new user profiles.
- **Model Training**: Train a robust face recognition model with captured images.
- **Real-Time Recognition**: Identify faces in real-time, displaying user names and confidence scores.
- **Cross-Platform Support**: Compatible with Windows, macOS, and Linux.
- **User-Friendly Interface**: Includes a menu-driven launcher for Windows users.
- **Open-Source**: Freely modify and extend the codebase.

## 📦 Project Structure

```
NeuraFace/
├── dataset/                  # Stores user face images
│   └── User.<id>.<name>/     # User-specific folder (e.g., User.1.John/1.jpg)
├── trainer/                  # Stores trained model
│   └── trainer.yml           # Trained face recognition model
├── recognizer.py             # Captures face images
├── trainer.py                # Trains the recognition model
├── webcam.py                 # Performs real-time face recognition
├── run.bat                   # Menu-driven launcher (Windows)
└── requirements.txt          # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- A functional webcam
- OpenCV Haar cascade file (included with `opencv-contrib-python`)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/nameIess/Neura-Face.git
   cd Neura-Face
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running NeuraFace

#### On Windows

- Double-click `run.bat` for an interactive menu, or run:
  ```sh
  .\run.bat
  ```

#### On macOS/Linux

Execute the scripts in sequence:

1. **Capture face images**:

   ```sh
   python recognizer.py
   ```

   - Input a user ID (e.g., `1`) and name (e.g., `John`).
   - Follow prompts to capture face images via webcam.

2. **Train the model**:

   ```sh
   python trainer.py
   ```

   - Processes images in `dataset/` and saves the model to `trainer/trainer.yml`.

3. **Run real-time recognition**:
   ```sh
   python webcam.py
   ```
   - Displays recognized user names and confidence scores in real-time.

## 🖼️ How It Works

1. **Capture**: `recognizer.py` captures webcam images and saves them to `dataset/User.<id>.<name>/` as numbered `.jpg` files.
2. **Train**: `trainer.py` uses the captured images to train a face recognition model, stored in `trainer/trainer.yml`.
3. **Recognize**: `webcam.py` processes webcam feed, detects faces, and identifies them using the trained model.

## 📁 Data Organization

- **Images**: Stored in `dataset/User.<id>.<name>/` (e.g., `dataset/User.1.John/1.jpg`).
- **Model**: Saved as `trainer/trainer.yml`.

## ⚠️ Important Notes

- Ensure your webcam is properly connected.
- Capture images and train the model before running real-time recognition.
- Use good lighting for accurate face capture and recognition.
- The Haar cascade file (`haarcascade_frontalface_default.xml`) is required and bundled with `opencv-contrib-python`.

## 🛠️ Requirements

- `opencv-contrib-python` (includes Haar cascades)
- `numpy`
- `pillow`

Install with:

```sh
pip install -r requirements.txt
```

## 🧪 Example Usage

1. Run `recognizer.py`:

   - Enter ID: `1`, Name: `Alice`.
   - Capture images by looking at the webcam.

2. Run `trainer.py` to train the model.

3. Run `webcam.py`:
   - The system will display "Alice" with a confidence score when her face is detected.

## 🙌 Contributing

We welcome contributions! To get started:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request.

Please follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/).

## 📚 Resources

- [OpenCV Documentation](https://docs.opencv.org/)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [GitHub Guides](https://guides.github.com/)

## 🙏 Credits

- Powered by [OpenCV](https://opencv.org/) for face detection and recognition.
- Utilizes [Pillow](https://python-pillow.org/) for image processing.
- Inspired by open-source computer vision communities.

## 📬 Contact

For issues or suggestions, open an issue on [GitHub](https://github.com/nameIess/Neura-Face/issues) or reach out via [yh8265j0c@mozmail.com](mailto:yh8265j0c@mozmail.com).

---

Share your feedback!