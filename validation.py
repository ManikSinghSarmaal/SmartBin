# Validate the model
from ultralytics import YOLO
model = YOLO('/Users/maniksinghsarmaal/Downloads/yolov7_sbin/runs/classify/train/weights/best.pt')
metrics = model.val() # no arguments needed, dataset and settings remembered
metrics.top1 # top1 accuracy
metrics.top5 # top5 accuracy