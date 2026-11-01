import time
import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

def move(pub, linear, angular, duration):
    msg = Twist()
    msg.linear.x = linear
    msg.angular.z = angular
    end = time.time() + duration
    while time.time() < end:
        pub.publish(msg)
        time.sleep(0.1)
    pub.publish(Twist())

def main():
    rclpy.init()
    node = Node("turtle_controller")
    pub = node.create_publisher(Twist, "/turtle1/cmd_vel", 10)
    time.sleep(1.0)

    # Move back 2 meters (speed -1.0 m/s for 2 seconds)
    move(pub, -1.0, 0.0, 2.0)
    time.sleep(0.5)

    # Draw a square with sides of 2 meters
    # Side length = 2.0 meters, speed = 1.0 m/s -> duration = 2.0 seconds
    # Turn angle = pi/2 radians (90 degrees), speed = 1.5708 rad/s -> duration = 1.0 second
    for _ in range(4):
        move(pub, 1.0, 0.0, 2.0)
        time.sleep(0.5)
        move(pub, 0.0, math.pi / 2.0, 1.0)
        time.sleep(0.5)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()