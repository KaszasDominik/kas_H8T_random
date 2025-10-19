#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray


class ArraySorterNode(Node):

    def __init__(self):
        super().__init__('array_sorter')
        self.subscriber = self.create_subscription(
            Float32MultiArray,
            '/input_array',
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(Float32MultiArray, '/sorted_array', 10)

    def listener_callback(self, msg):
        sorted_data = sorted(msg.data)
        sorted_msg = Float32MultiArray()
        sorted_msg.data = sorted_data
        self.publisher.publish(sorted_msg)
        self.get_logger().info(f"Received array: {msg.data}")
        self.get_logger().info(f"Published sorted array: {sorted_data}")


def main(args=None):
    rclpy.init(args=args)
    node = ArraySorterNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
