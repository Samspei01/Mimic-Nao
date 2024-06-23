# Mimic-Nao

This project uses pose estimation to mimic movements using a NAO robot. The goal is to demonstrate how pose estimation techniques can be applied to control the NAO robot's movements in real-time.

## Project Structure

- `pose estimation.py`: Performs real-time pose estimation using the MediaPipe library and OpenCV. Captures video from the webcam, processes each frame to detect human body landmarks, and records the positions of key points (shoulders, elbows, and wrists) in a text file.
- `NAO.py`: Connects to a NAO robot and uses pre-recorded body landmark coordinates to control the robot's arm movements. The script reads the coordinates from a text file and sends commands to the robot to move its arms accordingly.
- `video.mp4`: Demonstration video of the NAO robot mimicking movements.
- `Mimic_Nao.pdf`: Detailed documentation of the project, including setup instructions, code explanations, and usage guidelines.

## How It Works

1. **Pose Estimation**: 
    - The pose estimation algorithm detects the human body parts and their movements.
    - The detected poses are translated into commands that the NAO robot can understand.

2. **NAO Robot**:
    - The NAO robot receives the commands and mimics the movements of the person.
    - The communication between the pose estimation software and the NAO robot is handled via NAOqi SDK.

## Requirements

- Python 3.x
- Python 2.7
- OpenCV
- MediaPipe
- NAOqi SDK
- [Other dependencies]

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Samspei01/Mimic-Nao.git
    cd Mimic-Nao
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the pose estimation script:
    ```bash
    python pose estimation.py
    ```

4. Connect and control the NAO robot:
    ```bash
    python2 Nao.py
    ```

## Demonstration Video

Here is a demonstration of the project in action:

[![Mimic NAO Demonstration](https://i.vimeocdn.com/video/1418704725_640.jpg)](https://vimeo.com/965895468)


## Documentation

For detailed information about the project, including setup instructions, code explanations, and usage guidelines, please refer to the [documentation](Mimic_Nao.pdf).

## Instructions for Working with NAO

1. **Connect to NAO**:
    - Ensure NAO is connected to the same network as your computer.
    - Use NAOqi SDK to establish a connection:
      ```python
      from naoqi import ALProxy
      motion = ALProxy("ALMotion", "NAO_IP", 9559)
      ```

2. **Sending Commands to NAO**:
    - Use the motion proxy to send movement commands:
      ```python
      motion.moveTo(x, y, theta)
      ```
    - Example to make NAO wave:
      ```python
      names = ["RShoulderPitch", "RShoulderRoll"]
      angles = [0.5, -0.5]
      times = [1.0, 1.0]
      motion.angleInterpolation(names, angles, times, True)
      ```

3. **Safety Precautions**:
    - Always supervise NAO during operation.
    - Ensure the operating area is clear of obstacles.

## Contributing

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.
