# Smart Scanner

This simple smart scanner captures frames from a webcam feed, applies image processing techniques to detect contours, and extracts objects with a significant area. The extracted object can be saved as a PDF file.

## Prerequisites

- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- Pillow (`pip install Pillow`)

## Setting up the Webcam Feed

1. Install IP Webcam on your Android phone

2. Start the IP Webcam app on your phone and note the URL displayed at the bottom.

3. Adjust the `url` variable in the `scanner.py` script to the URL provided by IP Webcam.