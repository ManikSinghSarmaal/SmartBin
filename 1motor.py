from ultralytics import YOLO
import numpy as np
import os
import cv2
import RPi.GPIO as GPIO
import time

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
STEP_PIN = 17  # Replace with the actual GPIO pin number for the step pin
DIR_PIN = 18   # Replace with the actual GPIO pin number for the direction pin
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# Initialize the camera
camera = cv2.VideoCapture(0)  # 0 for the default camera

cwd = os.getcwd()
model_path = os.path.join(cwd, 'sbin_best.pt')

model = YOLO(model_path)

while True:
    # Capture a frame from the camera
    ret, frame = camera.read()

    # Perform inference on the frame
    results = model.predict(frame)

    # Get the predicted class probabilities
    probs = results[0].probs

    # Get the index of the top predicted class
    predicted_class_idx = probs.top1

    # Map the index to the corresponding class name
    class_names = results[0].names
    predicted_class_name = class_names[predicted_class_idx]

    print(f"Predicted class index: {predicted_class_idx}")
    print(f"Predicted class name: {predicted_class_name}")

    # Display the frame with the predicted class
    cv2.putText(frame, predicted_class_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('frame', frame)

    # Control the stepper motor based on the predicted class
    if predicted_class_idx == 0:  # Organic
        GPIO.output(DIR_PIN, GPIO.HIGH)  # Set the direction (e.g., clockwise)
        for i in range(200):  # Adjust the number of steps as needed
            GPIO.output(STEP_PIN, GPIO.HIGH)
            time.sleep(0.01)  # Adjust the delay as needed
            GPIO.output(STEP_PIN, GPIO.LOW)
            time.sleep(0.01)  # Adjust the delay as needed
    elif predicted_class_idx == 1:  # Inorganic
        GPIO.output(DIR_PIN, GPIO.LOW)  # Set the direction (e.g., anti-clockwise)
        for i in range(200):  # Adjust the number of steps as needed
            GPIO.output(STEP_PIN, GPIO.HIGH)
            time.sleep(0.01)  # Adjust the delay as needed
            GPIO.output(STEP_PIN, GPIO.LOW)
            time.sleep(0.01)  # Adjust the delay as needed

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and clean up GPIO
camera.release()
cv2.destroyAllWindows()
GPIO.cleanup()