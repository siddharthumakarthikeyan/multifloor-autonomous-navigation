import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TwistStamped

class Stamper(Node):
    def __init__(self):
        super().__init__('twist_stamper')
        self.pub = self.create_publisher(TwistStamped, '/diff_drive_controller/cmd_vel', 10)
        self.sub = self.create_subscription(Twist, '/cmd_vel', self.cb, 10)
    def cb(self, msg):
        out = TwistStamped()
        out.header.stamp = self.get_clock().now().to_msg()
        out.twist = msg
        self.pub.publish(out)

rclpy.init(); rclpy.spin(Stamper()); rclpy.shutdown()
