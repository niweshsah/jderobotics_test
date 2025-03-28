import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber') # Node name
        self.subscription = self.create_subscription(String, 'jde_test', self.listener_callback, 10) # Topic name
        # Creates a subscriber that listens to the topic named 'jde_test'.

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"') # Prints the received message to the console.

def main(args=None):
    rclpy.init(args=args)
    node = MinimalSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
# This code snippet creates a subscriber node that listens to the topic named 'topic' and prints the received message to the console.