import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TurtleSquare(Node):
    def __init__(self):
        super().__init__('turtle_square')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def move(self):
        msg = Twist()
        msg.linear.x = 2.0
        start = time.time()
        while time.time() - start < 2.0:
            self.pub.publish(msg)
            rclpy.spin_once(self, timeout_sec=0.05)

    def turn(self):
        msg = Twist()
        msg.angular.z = 1.57
        start = time.time()
        while time.time() - start < 1.0:
            self.pub.publish(msg)
            rclpy.spin_once(self, timeout_sec=0.05)

    def stop(self):
        self.pub.publish(Twist())

def main():
    rclpy.init()
    node = TurtleSquare()

    for _ in range(4):
        node.move()
        node.stop()
        node.turn()
        node.stop()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
