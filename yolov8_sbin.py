from ultralytics import YOLO
model = YOLO('yolov8n-cls.pt')
model.train(data='/Users/maniksinghsarmaal/Downloads/dataset', epochs=30)