## Instructions

1. Add this repository as a container in Docker Container
2. Press the start button for the container and wait a few seconds.
3. View the log files of the image to view the flagged data

## Purpose

The purpose of this code is to show potentially non-human traffic in a log of traffic data from the provided log file. It counts the repeated occurences of IP addresses, user agents, requested http paths and timestamps. It will then calculate an upper bound for when a count would be consider too high, flagging values that appear too much and adding them to the code's output. 

## For Devs 

### Installed Dependencies

- Python 3.11.9
- Python Libraries: numpy, pytz
- Docker Container

### Setup instructions 

This code should be run by using the Docker container that I have provided. 

Although you should not need to, to run it from a terminal, enter the following command:

docker compose up --build 

Note: If you're running this with a local IDE, you may edit the container CONSTANTS near the start of analyseLogs.py to use thresholds other than the default value. 

### Unit Testing

To run the unit tests that check some of the basic functions of analyseLogs.py, run it directly in an IDE or use the following command from the root directory.

python tests/test_analyseLogs.py

### Limitations

My code notably relies on thresholds within the code, so less frequent outliers in another log file might not be flagged.

My code only checks for repetitions so if many requests were made within the same few seconds then no outliers would be identified, but it could still identify many repetitions at the exact same timestamp.

### Installation Guide

Should you lack the dependencies to successfully run this code, here is a brief installation guide for each dependency:

- To install Python 3.11.9, go to https://www.python.org/downloads/release/python-3119/ and select Windows installer (64-bit), then follow the on-screen instructions.

- Given that Python 3.11.9 is installed, to install the relevant libraries, enter the following commands into a terminal:

    - pip install numpy
    - pip install pytz 

- To install Docker Container, go to https://docs.docker.com/get-started/get-docker/ and select Docker Desktop for Windows, then follow the on-screen instructions.


