from ultralytics import YOLO

model = YOLO('yolov8n.yaml')
model = YOLO('/home/billy/catkin_ws/src/turtlebot3_autorace_HSA23/turtlebot3_autorace_detect/nodes/runs/segment/train7/weights/best.pt')

metrics = model.val()
metrics.box.map 
metrics.box.map50
metrics.box.map75
metrics.box.maps