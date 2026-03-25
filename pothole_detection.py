"""
Real-Time Pothole Detection System using YOLOv4-Tiny

This script processes video streams to detect potholes using a YOLOv4-Tiny model,
captures GPS coordinates, and generates annotated output videos.

Author: Your Name
Date: 2024
License: MIT
"""

import cv2 as cv
import time
import geocoder
import os

# Configuration Parameters
CONF_THRESHOLD = 0.5      # Confidence threshold for detections
NMS_THRESHOLD = 0.4       # Non-maximum suppression threshold
DETECTION_COOLDOWN = 2    # Seconds between duplicate detections
MIN_CONFIDENCE = 0.7      # Minimum confidence for saving detections
MAX_SIZE_RATIO = 0.1      # Maximum detection size ratio (filters large detections)
MAX_Y_POSITION = 600      # Maximum Y position for detections


def load_model(weights_path, config_path, use_gpu=True):
    """
    Load YOLOv4-Tiny model with specified configuration.
    
    Args:
        weights_path (str): Path to model weights file
        config_path (str): Path to model configuration file
        use_gpu (bool): Whether to use GPU acceleration
        
    Returns:
        cv.dnn_DetectionModel: Configured detection model
    """
    net = cv.dnn.readNet(weights_path, config_path)
    
    if use_gpu:
        net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)
    
    model = cv.dnn_DetectionModel(net)
    model.setInputParams(size=(640, 480), scale=1/255, swapRB=True)
    
    return model


def load_class_names(filepath):
    """
    Load class names from obj.names file.
    
    Args:
        filepath (str): Path to obj.names file
        
    Returns:
        list: List of class names
    """
    with open(filepath, 'r') as f:
        return [cname.strip() for cname in f.readlines()]


def save_detection(frame, coordinates, output_dir, detection_count):
    """
    Save detected pothole image and GPS coordinates.
    
    Args:
        frame: Video frame with detection
        coordinates: GPS coordinates [lat, lng]
        output_dir (str): Directory to save outputs
        detection_count (int): Current detection number
    """
    # Save image
    image_path = os.path.join(output_dir, f'pothole{detection_count}.jpg')
    cv.imwrite(image_path, frame)
    
    # Save coordinates
    coord_path = os.path.join(output_dir, f'pothole{detection_count}.txt')
    with open(coord_path, 'w') as f:
        f.write(str(coordinates))
    
    print(f"Detection {detection_count} saved: {coordinates}")


def main():
    """Main detection loop."""
    
    # Initialize paths
    project_dir = "project_files"
    output_dir = "pothole_coordinates"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Load class names
    class_names = load_class_names(os.path.join(project_dir, 'obj.names'))
    
    # Load model
    print("Loading YOLOv4-Tiny model...")
    model = load_model(
        weights_path=os.path.join(project_dir, 'yolov4_tiny.weights'),
        config_path=os.path.join(project_dir, 'yolov4_tiny.cfg'),
        use_gpu=True
    )
    print("Model loaded successfully!")
    
    # Get current GPS location
    g = geocoder.ip('me')
    current_location = g.latlng
    print(f"Current location: {current_location}")
    
    # Initialize video capture
    video_source = "test1.mp4"  # Change to 0 for webcam
    cap = cv.VideoCapture(video_source)
    
    if not cap.isOpened():
        print(f"Error: Could not open video source: {video_source}")
        return
    
    # Get video properties
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv.CAP_PROP_FPS))
    
    # Initialize video writer
    output_video = cv.VideoWriter(
        'result1.avi',
        cv.VideoWriter_fourcc(*'MJPG'),
        fps,
        (width, height)
    )
    
    # Initialize counters and timers
    frame_counter = 0
    detection_count = 0
    last_detection_time = 0
    starting_time = time.time()
    
    print("Starting detection... Press 'q' to quit")
    
    # Main detection loop
    while True:
        ret, frame = cap.read()
        frame_counter += 1
        
        if not ret:
            print("End of video or cannot read frame")
            break
        
        # Perform detection
        classes, scores, boxes = model.detect(
            frame,
            CONF_THRESHOLD,
            NMS_THRESHOLD
        )
        
        # Process detections
        for (classid, score, box) in zip(classes, scores, boxes):
            x, y, w, h = box
            rec_area = w * h
            total_area = width * height
            size_ratio = rec_area / total_area
            
            # Apply filters
            if score >= MIN_CONFIDENCE and size_ratio <= MAX_SIZE_RATIO and y < MAX_Y_POSITION:
                # Draw bounding box
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                # Add label
                label = f"{round(score * 100, 2)}% pothole"
                cv.putText(
                    frame,
                    label,
                    (x, y - 10),
                    cv.FONT_HERSHEY_COMPLEX,
                    0.6,
                    (255, 0, 0),
                    2
                )
                
                # Save detection (with cooldown)
                current_time = time.time()
                if detection_count == 0 or (current_time - last_detection_time) >= DETECTION_COOLDOWN:
                    save_detection(frame, current_location, output_dir, detection_count)
                    last_detection_time = current_time
                    detection_count += 1
        
        # Calculate and display FPS
        elapsed_time = time.time() - starting_time
        current_fps = frame_counter / elapsed_time if elapsed_time > 0 else 0
        cv.putText(
            frame,
            f'FPS: {current_fps:.2f}',
            (20, 50),
            cv.FONT_HERSHEY_COMPLEX,
            0.7,
            (0, 255, 0),
            2
        )
        
        # Display frame
        cv.imshow('Pothole Detection', frame)
        
        # Write to output video
        output_video.write(frame)
        
        # Check for quit command
        if cv.waitKey(1) & 0xFF == ord('q'):
            print("Detection stopped by user")
            break
    
    # Cleanup
    cap.release()
    output_video.release()
    cv.destroyAllWindows()
    
    print(f"\nDetection complete!")
    print(f"Total frames processed: {frame_counter}")
    print(f"Total detections saved: {detection_count}")
    print(f"Output video: result1.avi")
    print(f"Detection data saved in: {output_dir}/")


if __name__ == "__main__":
    main()
