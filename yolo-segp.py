from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('best.pt')

# Run inference on 'frame_00000.jpg' with arguments
model.predict('/home/billy/catkin_ws/src/turtlebot3_autorace_HSA23/turtlebot3_autorace_detect/nodes/frame_000000.jpg', save=True, imgsz=320, conf=0.5)