from ultralytics import YOLO
import numpy as np
import os
import cv2
import RPi.GPIO as GPIO
import time

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
STEP_PIN_1 = 17  # Replace with the actual GPIO pin number for the step pin of Motor 1
DIR_PIN_1 = 18   # Replace with the actual GPIO pin number for the direction pin of Motor 1
STEP_PIN_2 = 22  # Replace with the actual GPIO pin number for the step pin of Motor 2
DIR_PIN_2 = 23   # Replace with the actual GPIO pin number for the direction pin of Motor 2
GPIO.setup(STEP_PIN_1, GPIO.OUT)
GPIO.setup(DIR_PIN_1, GPIO.OUT)
GPIO.setup(STEP_PIN_2, GPIO.OUT)
GPIO.setup(DIR_PIN_2, GPIO.OUT)

# Initialize the camera
# camera = cv2.VideoCapture(0)  # 0 for the default camera

cwd = os.getcwd()
model_path = os.path.join(cwd, 'sbin_best.pt')
model = YOLO(model_path)

image = '/Users/maniksinghsarmaal/Downloads/GitHub/yolov8_sbin/testing/r1.jpg'
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

# Control the stepper motors based on the predicted class
if predicted_class_idx == 0:  # Inorganic
    GPIO.output(DIR_PIN_1, GPIO.HIGH)  # Set the direction of Motor 1 (clockwise)
    for i in range(200):  # Adjust the number of steps as needed
        GPIO.output(STEP_PIN_1, GPIO.HIGH)
        time.sleep(0.01)  # Adjust the delay as needed
        GPIO.output(STEP_PIN_1, GPIO.LOW)
        time.sleep(0.01)  # Adjust the delay as needed

    GPIO.output(DIR_PIN_1, GPIO.LOW)  # Set the direction of Motor 1 (anti-clockwise)
    for i in range(200):  # Adjust the number of steps as needed
        GPIO.output(STEP_PIN_1, GPIO.HIGH)
        time.sleep(0.01)  # Adjust the delay as needed
        GPIO.output(STEP_PIN_1, GPIO.LOW)
        time.sleep(0.01)  # Adjust the delay as needed

elif predicted_class_idx == 2:  # Metal
    GPIO.output(DIR_PIN_1, GPIO.LOW)  # Set the direction of Motor 1 (anti-clockwise)
    for i in range(200):  # Adjust the number of steps as needed
        GPIO.output(STEP_PIN_1, GPIO.HIGH)
        time.sleep(0.01)  # Adjust the delay as needed
        GPIO.output(STEP_PIN_1, GPIO.LOW)
        time.sleep(0.01)  # Adjust the delay as needed

    GPIO.output(DIR_PIN_1, GPIO.HIGH)  # Set the direction of Motor 1 (clockwise)
    for i in range(200):  # Adjust the number of steps as needed
        GPIO.output(STEP_PIN_1, GPIO.HIGH)
        time.sleep(0.01)  # Adjust the delay as needed
        GPIO.output(STEP_PIN_1, GPIO.LOW)
        time.sleep(0.01)  # Adjust the delay as needed

elif predicted_class_idx == 1:  # Organics
    GPIO.output(DIR_PIN_2, GPIO.HIGH)  # Set the direction of Motor 2 (clockwise)
    for i in range(200):  # Adjust the number of steps as needed
        GPIO.output(STEP_PIN_2, GPIO.HIGH)
        time.sleep(0.01)  # Adjust the delay as needed
        GPIO.output(STEP_PIN_2, GPIO.LOW)
        time.sleep(0.01)  # Adjust the delay as needed

    GPIO.output(DIR_PIN_2, GPIO.LOW)  # Set the direction of Motor 2 (anti-clockwise)
    for i in range(200):  # Adjust the number of steps as needed
        GPIO.output(STEP_PIN_2, GPIO.HIGH)
        time.sleep(0.01)  # Adjust the delay as needed
        GPIO.output(STEP_PIN_2, GPIO.LOW)
        time.sleep(0.01)  # Adjust the delay as needed

# Clean up GPIO
GPIO.cleanup()