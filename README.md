# 🚗 Real-Time Pothole Detection System

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg)](https://opencv.org/)
[![YOLOv4](https://img.shields.io/badge/YOLOv4-Tiny-red.svg)](https://github.com/AlexeyAB/darknet)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An intelligent computer vision system that detects potholes in real-time using YOLOv4-Tiny deep learning model, automatically captures their GPS coordinates, and generates annotated video output.

## 🌟 Features

- **Real-time Detection**: Processes video streams or files to identify potholes with high accuracy
- **GPU Acceleration**: Leverages CUDA for fast inference (fallback to CPU supported)
- **Automatic Geolocation**: Captures GPS coordinates of detected potholes
- **Smart Filtering**: Prevents duplicate detections within 2-second intervals
- **Visual Output**: Generates annotated videos with detection boxes and confidence scores
- **Evidence Collection**: Saves screenshots and coordinates for each detected pothole

## 📋 Table of Contents

- [Demo](#-demo)
- [System Architecture](#-system-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Output](#-output)
- [Technical Details](#-technical-details)
- [Contributing](#-contributing)
- [License](#-license)

## 🎬 Demo

The system detects potholes in real-time and annotates them with:
- Detection bounding boxes
- Confidence scores (percentage)
- Real-time FPS counter

*Note: Add demo GIF or video here*

## 🏗️ System Architecture

```
Input Video → Frame Extraction → YOLOv4-Tiny Model → Detection
                                                           ↓
GPS Capture ← Coordinate Logging ← Post-processing ← Filtering
                                                           ↓
                                            Annotated Video Output
```

### Detection Pipeline

1. **Video Capture**: Reads from camera or video file
2. **Preprocessing**: Resizes frames to 640x480, normalizes pixel values
3. **Inference**: YOLOv4-Tiny model detects potholes
4. **Filtering**: Applies confidence threshold (70%) and size filters
5. **Deduplication**: 2-second cooldown between detections
6. **Output**: Saves coordinates, screenshots, and annotated video

## 🔧 Installation

### Prerequisites

- Python 3.7 or higher
- CUDA-capable GPU (optional, but recommended)
- Webcam or video file for testing

### Step 1: Clone the Repository

```bash
git clone https://github.com/Saravananb91/road-pothole-.git
cd pothole-detection
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Download Model Files

Download the YOLOv4-Tiny model files and place them in the `project_files` directory:

```
project_files/
├── yolov4_tiny.weights
├── yolov4_tiny.cfg
└── obj.names
```

**Download Links:**
- [yolov4_tiny.weights](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights)
- [yolov4_tiny.cfg](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg)

### Step 4: Create Required Directories

```bash
mkdir -p project_files pothole_coordinates
```

## 🚀 Usage

### Basic Usage

Process a video file:

```bash
python pothole_detection.py
```

### Using Webcam

Modify line 24 in `pothole_detection.py`:

```python
cap = cv.VideoCapture(0)  # 0 for default webcam
```

### Custom Video Source

```python
cap = cv.VideoCapture("path/to/your/video.mp4")
```

### Run the Script

```bash
python pothole_detection.py
```

Press `q` to stop the detection and save results.

## ⚙️ Configuration

### Detection Parameters

Adjust these parameters in the script for optimal performance:

```python
Conf_threshold = 0.5    # Minimum confidence threshold (0.0 - 1.0)
NMS_threshold = 0.4     # Non-maximum suppression threshold
detection_cooldown = 2   # Seconds between duplicate detections
```

### Size Filtering

```python
if((recarea/area) <= 0.1 and box[1] < 600):
```
- `recarea/area <= 0.1`: Filters detections that are too large (likely false positives)
- `box[1] < 600`: Filters detections in the bottom portion of frame

### GPU Settings

For CPU-only inference, comment out these lines:

```python
# net1.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
# net1.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)
```

## 📤 Output

The system generates the following outputs:

### 1. Annotated Video
- **Location**: `result1.avi`
- **Content**: Original video with detection boxes and FPS counter

### 2. Detection Screenshots
- **Location**: `pothole_coordinates/pothole{N}.jpg`
- **Content**: Frame capture when pothole is detected

### 3. GPS Coordinates
- **Location**: `pothole_coordinates/pothole{N}.txt`
- **Content**: Latitude and longitude of detection
- **Format**: `[latitude, longitude]`

### Example Output Structure

```
pothole-detection/
├── result1.avi                    # Annotated video output
└── pothole_coordinates/
    ├── pothole0.jpg              # First detection screenshot
    ├── pothole0.txt              # First detection coordinates
    ├── pothole1.jpg              # Second detection screenshot
    ├── pothole1.txt              # Second detection coordinates
    └── ...
```

## 🔬 Technical Details

### Model Specifications

- **Architecture**: YOLOv4-Tiny
- **Input Size**: 640x480 pixels
- **Framework**: OpenCV DNN module
- **Precision**: FP16 (GPU) / FP32 (CPU)

### Performance

- **FPS**: 15-30 fps (GPU), 5-10 fps (CPU)
- **Accuracy**: ~70%+ confidence threshold for reliable detections
- **Latency**: ~30-100ms per frame

### Key Libraries

- **OpenCV**: Computer vision and DNN inference
- **Geocoder**: GPS coordinate retrieval
- **NumPy**: Array operations

## 🛠️ Troubleshooting

### Common Issues

**Issue**: `FileNotFoundError: project_files/yolov4_tiny.weights`
- **Solution**: Download model files and place them in `project_files/` directory

**Issue**: Low FPS or slow processing
- **Solution**: 
  - Enable GPU acceleration (requires CUDA)
  - Reduce input video resolution
  - Use YOLOv4-Tiny instead of full YOLOv4

**Issue**: No GPS coordinates captured
- **Solution**: Check internet connection (geocoder requires network access)

**Issue**: Too many false positives
- **Solution**: Increase `Conf_threshold` to 0.7 or higher

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Improvement

- [ ] Add training pipeline for custom datasets
- [ ] Implement live GPS tracking (using GPS hardware)
- [ ] Create web dashboard for visualization
- [ ] Add database integration for coordinate storage
- [ ] Improve detection accuracy with YOLOv5/v8
- [ ] Mobile app integration

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Saravanan B - [mrsaravananb@gmail.com ](mrsaravananb@gmail.com)

Project Link: [https://github.com/Saravananb91/road-pothole-](https://github.com/Saravananb91/road-pothole-)

Portfolio website : [portfolio-saravananb.vercel.app](portfolio-saravananb.vercel.app ) 

Linkedin: [www.linkedin.com/in/saravanan-b-46244b290](www.linkedin.com/in/saravanan-b-46244b290)
## 🙏 Acknowledgments

- [YOLOv4](https://github.com/AlexeyAB/darknet) by AlexeyAB
- [OpenCV](https://opencv.org/) for computer vision tools
- [Geocoder](https://geocoder.readthedocs.io/) for location services

## 📊 Roadmap

- [x] Basic pothole detection
- [x] GPS coordinate logging
- [x] Video annotation
- [ ] Real-time dashboard
- [ ] Mobile application
- [ ] Cloud deployment
- [ ] Dataset collection tool
- [ ] Model retraining pipeline

---

**⭐ If you find this project useful, please consider giving it a star!**
