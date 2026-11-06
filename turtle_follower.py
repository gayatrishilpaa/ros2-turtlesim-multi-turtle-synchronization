import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import time

class Create_Turtle(Node):
    def __init__(self):
        super().__init__('spawn_Turtle')
        self.cli=self.create_client(Spawn,'/spawn')
        self.current_angle=0.0
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /spawn service...')
        self.spawn_turtle2()
        self.subs=self.create_subscription(Pose, '/turtle1/pose',self.get_turtle1,10)
        self.pubs=self.create_publisher(Twist, '/turtle2/cmd_vel',10)

    def spawn_turtle2(self):
        req=Spawn.Request()
        req.x=5.444445
        req.y=5.444445
        req.theta=0.0
        req.name='turtle2'
        future = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)

    def get_turtle1(self,msg):
        time.sleep(0.5)
        vel=Twist()
        vel.linear.x=msg.linear_velocity 
        vel.angular.z=msg.angular_velocity
        self.pubs.publish(vel)
        self.current_angle=msg.theta 

def main():
    rclpy.init()
    spawn_Turtle=Create_Turtle()
    rclpy.spin(spawn_Turtle)
    spawn_Turtle.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

   