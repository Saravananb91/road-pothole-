# Quick Start Guide

Get the Pothole Detection System up and running in 5 minutes!

## Prerequisites

- Python 3.7+
- pip package manager
- (Optional) NVIDIA GPU with CUDA support

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/pothole-detection.git
cd pothole-detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Model Files

```bash
cd project_files

# Download weights (245 MB)
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights -O yolov4_tiny.weights

# Download config
wget https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg -O yolov4_tiny.cfg

cd ..
```

### 4. Add Your Video

Place your test video in the project root or use webcam:

```python
# For video file (in pothole_detection.py, line 100):
video_source = "test1.mp4"

# For webcam:
video_source = 0
```

### 5. Run Detection

```bash
python pothole_detection.py
```

Press `q` to stop detection.

## Output

After running, you'll find:

- **Annotated video**: `result1.avi`
- **Detection screenshots**: `pothole_coordinates/pothole{N}.jpg`
- **GPS coordinates**: `pothole_coordinates/pothole{N}.txt`

## Configuration

Adjust detection sensitivity in `pothole_detection.py`:

```python
CONF_THRESHOLD = 0.5      # Lower = more detections
MIN_CONFIDENCE = 0.7      # Minimum to save detection
DETECTION_COOLDOWN = 2    # Seconds between saves
```

## Common Issues

**No CUDA/GPU detected**: The script will automatically use CPU (slower but works).

**FileNotFoundError**: Make sure model files are in `project_files/` directory.

**Low FPS**: Reduce video resolution or enable GPU acceleration.

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [SETUP.md](SETUP.md) for advanced configuration
- See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

## Support

- Create an issue on GitHub
- Email: your.email@example.com

Happy detecting! 🚗
