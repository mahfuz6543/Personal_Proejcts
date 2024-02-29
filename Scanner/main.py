import urllib.request as request
from PIL import Image
import cv2
import time
import numpy as np

# URL of the webcam feed
url = 'http://192.168.1.233:8080/shot.jpg'

# Main loop for continuous scanning
while True:
    img = request.urlopen(url)
    # Convert the image to a byte array
    img_bytes = bytearray(img.read())
    # Convert the byte array to a NumPy array
    img_np = np.array(img_bytes, dtype=np.uint8)
    # Decode the NumPy array to obtain the frame
    frame = cv2.imdecode(img_np, -1)
    frame_cvt = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Apply Gaussian Blur to reduce noise
    frame_blur = cv2.GaussianBlur(frame_cvt, (5, 5), 0)
    # Apply Canny edge detection
    frame_edge = cv2.Canny(frame_blur, 30, 50)
    cv2.imshow('My Scanner', frame_edge)
    # Find contours in the edge-detected frame
    contours, h = cv2.findContours(frame_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # Check if contours are found
    if contours:
        # Find the contour with the maximum area
        max_contours = max(contours, key=cv2.contourArea)
        # Get the bounding rectangle of the maximum contour
        x, y, w, h = cv2.boundingRect(max_contours)
        # Check if the area of the maximum contour is above a threshold
        if cv2.contourArea(max_contours) > 5000:
            #cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)
            # Extract the region of interest (ROI) containing the detected object
            object_only=frame[y:y+h, x:x+w]
            # Display the extracted object
            cv2.imshow('My Smart Scanner', object_only)
            # Save the extracted object as a PDF file when 's' key is pressed
            if cv2.waitKey(1) == ord('s'):
                img_pil = Image.fromarray(object_only)
                time_str = time.strftime('%Y-%m-%d-%H-%M-%S')
                img_pil.save(f'{time_str}.pdf')
                print(time_str)