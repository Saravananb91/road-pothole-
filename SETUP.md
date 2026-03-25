# Project Setup Guide

This guide will help you set up the complete project structure for the Pothole Detection System.

## Directory Structure

After setup, your project should look like this:

```
pothole-detection/
├── project_files/              # Model files directory
│   ├── yolov4_tiny.weights    # YOLOv4-Tiny weights (download required)
│   ├── yolov4_tiny.cfg        # YOLOv4-Tiny configuration
│   └── obj.names              # Class names file
├── pothole_coordinates/        # Output directory for detections
│   ├── pothole0.jpg           # Detection screenshots (generated)
│   ├── pothole0.txt           # GPS coordinates (generated)
│   └── ...
├── pothole_detection.py       # Main detection script
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── LICENSE                    # License file
├── CONTRIBUTING.md            # Contribution guidelines
├── .gitignore                 # Git ignore rules
├── test1.mp4                  # Test video (optional)
└── result1.avi                # Output video (generated)
```

## Step-by-Step Setup

### 1. Create Directory Structure

Run these commands in your project root:

```bash
# Create required directories
mkdir -p project_files
mkdir -p pothole_coordinates

# Create placeholder files
touch project_files/.gitkeep
touch pothole_coordinates/.gitkeep
```

### 2. Download Model Files

#### Option A: Using wget (Linux/Mac)

```bash
cd project_files

# Download YOLOv4-Tiny weights
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights -O yolov4_tiny.weights

# Download YOLOv4-Tiny config
wget https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg -O yolov4_tiny.cfg

cd ..
```

#### Option B: Manual Download

1. Download weights from: https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights
2. Download config from: https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg
3. Save both files in `project_files/` directory
4. Rename them to `yolov4_tiny.weights` and `yolov4_tiny.cfg`

### 3. Create obj.names File

Create `project_files/obj.names` with the following content:

```bash
echo "pothole" > project_files/obj.names
```

Or create the file manually with one line: `pothole`

### 4. Install Python Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 5. Verify Installation

Check that all required files are in place:

```bash
# Check project structure
ls -R

# Verify Python packages
pip list | grep -E "opencv|numpy|geocoder"
```

### 6. Test the Setup

Run a quick test to ensure everything is working:

```python
python -c "import cv2; print(f'OpenCV version: {cv2.__version__}')"
python -c "import geocoder; print('Geocoder installed successfully')"
```

## GPU Setup (Optional but Recommended)

### For NVIDIA GPUs with CUDA

1. Install CUDA Toolkit (version 11.0 or higher)
   - Download from: https://developer.nvidia.com/cuda-downloads

2. Install cuDNN
   - Download from: https://developer.nvidia.com/cudnn

3. Verify CUDA installation:
   ```bash
   nvcc --version
   nvidia-smi
   ```

4. OpenCV should automatically detect and use CUDA if available

### For CPU-only Systems

If you don't have a GPU, modify `pothole_detection.py`:

```python
# Change this line in the load_model function:
model = load_model(
    weights_path=os.path.join(project_dir, 'yolov4_tiny.weights'),
    config_path=os.path.join(project_dir, 'yolov4_tiny.cfg'),
    use_gpu=False  # Change to False
)
```

## Adding Test Video

### Option 1: Use Your Own Video

Place your video file in the project root and update line 100 in `pothole_detection.py`:

```python
video_source = "your_video.mp4"
```

### Option 2: Use Webcam

For live webcam detection:

```python
video_source = 0  # 0 for default webcam
```

### Option 3: Download Sample Videos

You can find road condition videos on:
- YouTube (use youtube-dl to download)
- Free stock video sites (Pexels, Pixabay)
- Dashcam footage repositories

## Troubleshooting

### Issue: "FileNotFoundError: project_files/yolov4_tiny.weights"

**Solution**: Make sure you've downloaded the model files and placed them in the correct directory.

### Issue: "ImportError: No module named 'cv2'"

**Solution**: 
```bash
pip install opencv-python opencv-contrib-python
```

### Issue: "CUDA not available" warning

**Solution**: This is normal if you don't have a CUDA-capable GPU. The script will fall back to CPU processing.

### Issue: Low FPS during detection

**Solutions**:
- Enable GPU acceleration (if available)
- Reduce video resolution
- Use a smaller model (YOLOv4-Tiny is already optimized)
- Close other applications to free up resources

### Issue: GPS coordinates not accurate

**Solution**: The script uses IP-based geolocation which is approximate. For accurate GPS:
- Use a GPS hardware module
- Implement smartphone GPS integration
- Use GPS-enabled dashcam footage

## Next Steps

Once setup is complete:

1. Run the detection script: `python pothole_detection.py`
2. Check the output in `pothole_coordinates/` directory
3. Watch the annotated video: `result1.avi`
4. Adjust parameters in the script for optimal performance

## Additional Resources

- [YOLOv4 Paper](https://arxiv.org/abs/2004.10934)
- [OpenCV Documentation](https://docs.opencv.org/)
- [CUDA Installation Guide](https://docs.nvidia.com/cuda/)

## Getting Help

If you encounter issues:
1. Check the troubleshooting section above
2. Review the [GitHub Issues](https://github.com/yourusername/pothole-detection/issues)
3. Create a new issue with detailed information
4. Reach out via email: your.email@example.com

---

Happy detecting! 🚗💨
