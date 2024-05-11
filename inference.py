from ultralytics import YOLO
import numpy as np
import os

cwd = os.getcwd()
model_path = os.path.join(cwd,'sbin_best.pt')

image = "/Users/maniksinghsarmaal/Downloads/GitHub/yolov8_sbin/testing/r1.jpg"
model = YOLO('/Users/maniksinghsarmaal/Downloads/yolov8_sbin/runs/classify/train/weights/best.pt')
results = model.predict(image)

# Get the predicted class probabilities
probs = results[0].probs

# Get the index of the top predicted class
predicted_class_idx = probs.top1

# Map the index to the corresponding class name
class_names = results[0].names
predicted_class_name = class_names[predicted_class_idx]

print(f"Predicted class index: {predicted_class_idx}")
print(f"Predicted class name: {predicted_class_name}")
print(model_path)