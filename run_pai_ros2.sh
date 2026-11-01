#!/bin/bash
docker run -d --name pai_ros2 \
--platform linux/amd64 \
-p 6080:80 --shm-size=1024m \
-p 9090:9090 -p 9876:9876 \
-v "$(pwd)":/workspace \
airobotbook/ros2-desktop-ai-robot-book-humble:latest
