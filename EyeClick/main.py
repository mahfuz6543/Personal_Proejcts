import cv2
import mediapipe as mp
import pyautogui

# Initialize the webcam
cam = cv2.VideoCapture(0)

# Initialize the FaceMesh model from mediapipe
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# Get the screen size for later mapping of coordinates
screen_w, screen_h = pyautogui.size()

# Main loop for video processing
while True:
   # Read a frame from the webcam
   _, frame = cam.read()
   # Flip the frame horizontally for a more intuitive view
   frame = cv2.flip(frame, 1)
   # Convert the frame to RGB for processing with mediapipe
   rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   # Process the frame with FaceMesh
   output = face_mesh.process(rgb_frame)
   # Extract facial landmark points
   landmark_points = output.multi_face_landmarks
   # Get the height and width of the frame
   frame_h, frame_w, _ = frame.shape

   # Check if facial landmarks are detected
   if landmark_points:
      landmarks = landmark_points[0].landmark
      # Extract the coordinates of specific landmarks for cursor control
      for id, landmark in enumerate (landmarks[474:478]):
          x = int(landmark.x * frame_w)
          y = int(landmark.y * frame_h)
          cv2.circle(frame, (x,y), 3, (0, 255, 0))
          # Move the cursor to the specified position based on landmark id
          if id == 1:
              screen_x = screen_w / frame_w * x
              screen_y = screen_h / frame_h * y
              pyautogui.moveTo(screen_x,screen_y)
      # Extract and display left eye landmarks
      left = [landmarks[145], landmarks[159]]
      for landmark in left:
          x = int(landmark.x * frame_w)
          y = int(landmark.y * frame_h)
          cv2.circle(frame, (x, y), 3, (0, 255, 255))
      # Check for a blink by measuring the vertical distance between two points
      if(left[0].y - left[1].y) < 0.004:
          pyautogui.click()
          pyautogui.sleep(1)
   # Display the processed frame
   cv2.imshow('Eye Clicker Mouse', frame)
   # Wait for a key press
   cv2.waitKey(1)