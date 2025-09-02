import cv2

# Open default camera (0 = first camera)
cap = cv2.VideoCapture(0)

# Get default video frame width and height
frame_width = int(cap.get(3))   # property 3 = width
frame_height = int(cap.get(4))  # property 4 = height

# Define the codec and create VideoWriter object
out = cv2.VideoWriter(
    'output.avi',                      # filename
    cv2.VideoWriter_fourcc(*'XVID'),   # codec
    20.0,                              # FPS
    (frame_width, frame_height)        # frame size
)

print("Recording... Press 'q' to stop.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Write the frame to file
    out.write(frame)

    # Show the recording in a window
    cv2.imshow('Recording', frame)

    # Press 'q' to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()

print("Video saved as output.avi")
