import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class TurtleTriangle(Node):
    def __init__(self):
        super().__init__('turtle_triangle')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.get_logger().info("Triangle movement started")
        self.draw_triangle()

    def draw_triangle(self):
        for i in range(3):
            self.move_forward(2.0)
            self.turn(120)

    def move_forward(self, duration):
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 0.0
        end_time = self.get_clock().now().seconds_nanoseconds()[0] + duration
        while self.get_clock().now().seconds_nanoseconds()[0] < end_time:
            self.publisher_.publish(msg)
            time.sleep(0.1)

    def turn(self, degree):
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = math.radians(60)
        duration = 2.0
        end_time = self.get_clock().now().seconds_nanoseconds()[0] + duration
        while self.get_clock().now().seconds_nanoseconds()[0] < end_time:
            self.publisher_.publish(msg)
            time.sleep(0.1)

        # หยุดหมุน
        self.publisher_.publish(Twist())

def main(args=None):
    rclpy.init(args=args)
    node = TurtleTriangle()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()