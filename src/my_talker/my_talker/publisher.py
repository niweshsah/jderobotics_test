import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):
    
    def __init__(self):
        super().__init__('minimal_publisher') # Node name
        self.publisher_ = self.create_publisher(String, 'jde_test', 10) # Topic name is jde_test and queue size is 10
        self.timer = self.create_timer(1.0, self.timer_callback) 
        # Creates a timer that triggers every 1.0 seconds.
        # Calls the function self.timer_callback each time the timer triggers.
        # Returns a Timer object, which is stored in self.timer.


    def timer_callback(self):
        msg = String()
        msg.data = 'Hello! ROS2 is fun.'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
    

def main(args=None):
    rclpy.init(args=args)
    node = MinimalPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
