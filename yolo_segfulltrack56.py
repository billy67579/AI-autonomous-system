import cv2
from ultralytics import YOLO

# Load the model
model = YOLO('best.pt')  # pretrained YOLOv8n model

# Open the video path
video_path = "/home/billy/catkin_ws/src/turtlebot3_autorace_HSA23/turtlebot3_autorace_detect/nodes/smart_city.mp4"
cap = cv2.VideoCapture(video_path)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video_path = 'output_video.avi'
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Loop through the video frames
while cap.isOpened():
    success, frame = cap.read()
    if success:
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        out.write(annotated_frame)  # Write the frame to the output video
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()