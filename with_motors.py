from ultralytics import YOLO
import numpy as np
import os
import cv2

import RPi.GPIO as GPIO
# Initialize the camera
camera = cv2.VideoCapture(0)  # 0 for the default camera

cwd = os.getcwd()
model_path = os.path.join(cwd, 'sbin_best.pt')

model = YOLO(model_path)

image = 'define-ypur-image'
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


# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # Motor 1 connected to GPIO 17
GPIO.setup(18, GPIO.OUT)  # Motor 2 connected to GPIO 18

motor1 = GPIO.PWM(17, 50)  # 50 Hz frequency for Motor 1
motor2 = GPIO.PWM(18, 50)  # 50 Hz frequency for Motor 2

# Start the motors
motor1.start(0)
motor2.start(0)

# Adjust the motor direction based on the predicted class
if predicted_class_idx == 0:  # Organic
    motor1.ChangeDutyCycle(25)  # Motor 1 clockwise at 25% speed
elif predicted_class_idx == 1:  # Inorganic
    motor1.ChangeDutyCycle(75)  # Motor 1 anti-clockwise at 75% speed
elif predicted_class_idx == 2:  # Metal
    motor2.ChangeDutyCycle(50)  # Motor 2 at 50% speed

# Clean up GPIO
motor1.stop()
motor2.stop()
GPIO.cleanup()