Primary contents of the folder have been updated or expanded:
1 config.yaml: it is configuration file of custom dataset used
2 detect_lane.py: it is the node used for detection of lane using YOLO
3 images: it contains images which are trained for model
4 labels: annotations of the same images which are used for model
5 requirements.txt: libraries required to be installed for using YOLO
6 runs: contains pre-trained models
7 train.py: node to train the images with annotation and make a model
8 yolov8n-seg.pt: used in train.py as reference for training segmentation model
9\.yolov8n.yaml: used in train.py as reference for training classification model
10\.masks_to_polygons.py: used to convert segmentation masks to labels
11\.predict.py: used to predict the trained model on real-time video of the lane
12\.yolo_segfulltrack56.py: used to run the trained segmentation model on realtime video of the smart city with 56frames
13\.yolo_segfulltrack25: used to run the trained segmentation model on realtime video of the smart city with 25frames
14\.yolo-segp.py: used to run inference on the frame of the lane
15\.accuracy.py:  use to calculate the accuracy of the segmentation model

To train your own model

Step 1: Install “ultralytics” library with version higher than or equal to ‘8.0.128

Step 2: Gather a dataset containing images or videos of road scenes with clearly marked lanes

Step 3: Annotate the dataset to indicate the position and type of each lane.for this project cvat.ai was used to annotate the images with bounding boxes around the lanes.

Step 4: Once you annotated images if you have used online tool then export dataset in yolo format

Step 5: extract images from lane detection video into frames
Directory 1: “images” with sub directory “train” (copy all annotated images in this directory)
Directory 2: “labels” with sub-directory “train” (copy all labels from dataset exported in this directory)

Step 7: Prepare YOLO configuration files “config.yaml” . Create a data configuration file specifying the path to training and val datasets, class names, etc

Step 8: Run a “train.py” file

Step 9: Once training is completed you can find a "runs" directory in your working directory. This contains report of the training and weights of your trained model.

To used your own trained model

Step 1: install requirements.txt

Step 2: create a "yolo-seg.py","yolo_segfulltrack56.py",for the implementation of the customized pretrained model

Step 3: Place customized pretrained model (‘runs’ directory) and video in working directory

Step 4: Run “yolo-seg.py” to performed Yolo segmentation
"yolo_segfulltrack56.py" to performed yolo segmenation on the fulltrack with 56 customised frames
"yolo_segfulltrack25"  to performed yolo segmentation on the fulltrack with 25 customised frames
"predict.py" to performed yolo classification on the fulltrack of the lane.

Step 5: Once the process is completed you can find a "runs" directory in your working directory. This contains report of the training and weights of your trained model.