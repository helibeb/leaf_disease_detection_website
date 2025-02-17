import cv2
from ultralytics import YOLO

# Load the custom YOLO model
model = YOLO('best.pt')  # Replace with the path to your custom model

# Initialize webcam
cap = cv2.VideoCapture('leafs.mp4')  # 0 is usually the default camera

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Perform inference on the frame
    results = model(frame)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()  # Draw bounding boxes and labels

    # Show the annotated frame
    cv2.imshow('YOLO Webcam Detection', annotated_frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()