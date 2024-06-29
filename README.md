# AI Face Detector

This is a simple AI face detector that captures video from a webcam and detects faces in real-time. It uses the `detectMultiScale` function to detect faces of various sizes and can detect multiple faces simultaneously. A square is displayed around each detected face.

## Features

- Real-time face detection from webcam feed
- Detects faces of different sizes
- Detects multiple faces simultaneously

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/AI-face-detector.git
   cd AI-face-detector
   
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. Run the face detector script:
   ```bash
   python main.py
2.The script will start capturing video from your webcam and will display a window with the video feed. Detected faces will be highlighted with a square.
## Code Overview

The main functionality is implemented in `main.py`. Here is a brief overview of the key parts:

- **Capturing Webcam Feed**: The script captures video from the webcam using OpenCV.
- **Face Detection**: The `detectMultiScale` function from OpenCV is used to detect faces in each frame of the video.
- **Drawing Squares**: Once faces are detected, squares are drawn around them in the video feed.

## Dependencies

- OpenCV
- Other dependencies can be found in `requirements.txt`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

If you have any questions or suggestions, feel free to reach out at [abdulparveezya@gmail.com](mailto:abdulparveezya@gmail.com).

