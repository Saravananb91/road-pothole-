# Contributing to Pothole Detection System

Thank you for your interest in contributing to this project! Here are some guidelines to help you get started.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with the following information:

- **Clear description** of the bug
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **Screenshots** or error messages (if applicable)
- **Environment details** (OS, Python version, GPU/CPU)

### Suggesting Features

Feature suggestions are welcome! Please create an issue with:

- **Clear description** of the feature
- **Use case** - why this feature would be useful
- **Possible implementation** approach (if you have ideas)

### Pull Requests

1. **Fork the repository** and create your branch from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines below

3. **Test your changes** thoroughly

4. **Commit your changes** with clear, descriptive messages
   ```bash
   git commit -m "Add feature: description of what you added"
   ```

5. **Push to your fork** and submit a pull request
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style Guidelines

### Python Style

- Follow **PEP 8** style guide
- Use **meaningful variable names**
- Add **docstrings** to functions and classes
- Keep functions **focused and modular**
- Add **type hints** where appropriate

Example:
```python
def process_frame(frame: np.ndarray, model: cv.dnn_DetectionModel) -> tuple:
    """
    Process a single frame for pothole detection.
    
    Args:
        frame: Input image frame
        model: YOLOv4 detection model
        
    Returns:
        Tuple of (classes, scores, boxes)
    """
    # Implementation
    pass
```

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- First line should be 50 characters or less
- Add detailed description if needed in the body

Good examples:
- `Add webcam support for live detection`
- `Fix GPS coordinate accuracy issue`
- `Improve detection performance by 20%`
- `Update README with installation instructions`

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/your-username/pothole-detection.git
   cd pothole-detection
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download model files (see README.md)

## Testing

Before submitting a pull request:

- [ ] Test with video files
- [ ] Test with webcam (if applicable)
- [ ] Test on both GPU and CPU
- [ ] Verify no new warnings or errors
- [ ] Check that output files are generated correctly

## Areas for Contribution

Here are some areas where contributions would be particularly valuable:

### High Priority
- [ ] Add unit tests and integration tests
- [ ] Improve detection accuracy
- [ ] Add real-time GPS tracking (hardware GPS)
- [ ] Optimize performance for lower-end hardware

### Medium Priority
- [ ] Create web dashboard for visualization
- [ ] Add database integration (SQLite/PostgreSQL)
- [ ] Implement data augmentation for training
- [ ] Add support for YOLOv5/v8 models

### Documentation
- [ ] Add video tutorials
- [ ] Create API documentation
- [ ] Add more usage examples
- [ ] Translate README to other languages

### New Features
- [ ] Mobile app integration
- [ ] Cloud deployment guides (AWS/GCP/Azure)
- [ ] Dataset collection tool
- [ ] Model retraining pipeline
- [ ] Email/SMS notification system

## Questions?

If you have questions about contributing, feel free to:
- Open an issue with the `question` label
- Reach out via email (your.email@example.com)

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn and grow

Thank you for contributing! 🎉
