 # Intelligent Waste Segregation System

This project aims to develop an intelligent waste segregation system that can automatically classify and sort different types of waste materials into three categories: organic, inorganic, and metal. The system utilizes computer vision and machine learning techniques to analyze captured images of waste items and direct them into the appropriate bin section using a mechanical sorting mechanism.

## Table of Contents

- [Introduction](#introduction)
- [Components](#components)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)

## Introduction

Improper waste management and disposal have become critical environmental issues. This project addresses these challenges by automating the waste segregation process, reducing the burden on manual labor and improving the overall efficiency of waste management practices.

The proposed solution involves the integration of several key components: image acquisition using a Raspberry Pi camera module, object detection and classification using the YOLO (You Only Look Once) model, Raspberry Pi integration for inference and control, a mechanical sorting mechanism with stepper motors and flaps, and a user-friendly web interface.

## Components

1. **Raspberry Pi 4 Model B**
2. **Raspberry Pi Camera Module**
3. **Stepper Motors and Motor Drivers**
4. **Mechanical Sorting Mechanism (Flaps and Bins)**
5. **Printed Circuit Boards (PCBs) for motor drivers and control circuits**
6. **Power supply units**
7. **Enclosure materials (e.g., acrylic, metal sheets)**

## Installation

1. Install the required libraries and dependencies on the Raspberry Pi:
   - Python (usually pre-installed on Raspbian)
   - Ultralytics YOLO library: `pip install ultralytics`
   - Other required libraries (e.g., numpy, opencv-python)

2. Transfer the trained YOLO model (`sbin_best.pt`) to the Raspberry Pi.

3. Set up the mechanical sorting mechanism and connect the stepper motors to the appropriate GPIO pins.

4. Clone the project repository and navigate to the project directory.

## Usage

1. Run the main script (`motors_come_back.py`) to start the waste segregation system.
2. The Raspberry Pi camera will capture images of waste items as they are introduced into the system.
3. The captured images will be processed by the YOLO model to classify the waste into organic, inorganic, or metal categories.
4. Based on the predicted category, the mechanical sorting mechanism will be activated to direct the waste item into the corresponding bin section.
5. The real-time classification results and insights will be displayed on the web interface.

## Results

- The intelligent waste segregation system has been successfully developed and integrated with the Raspberry Pi and mechanical sorting mechanism.
- The trained YOLO model achieves an accuracy of [X%] in classifying waste items into the three categories.
- The system can process and sort [Y] waste items per minute.
- [https://drive.google.com/file/d/14Xc3c1qOiZjQKldAli8NWx0QTQpTw1aF/view?usp=sharing]

## Prototype
<div align="center">
  <img src="Images/IMG_4918.HEIC" width="45%" />
  <em>Circuit Diagram</em>
</div>
<div align="center">
  <img src="Images/IMG_4948.HEIC" width="45%" />
  <em>Prototype</em>
</div>

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.


