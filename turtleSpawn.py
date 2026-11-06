import rclpy
from turtlesim.srv import Spawn
from rclpy.node import Node
import sys

#server
class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv=self.create_service(Spawn,'/spawn',self.spawn_callback)
        
    def spawn_callback(self, request, response):
        response=request      
        return response
    
def main():
    rclpy.init()
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

#client
class MinimalClientAsync(Node):

    def __init__(self):
        super.__init__('minimal_client_async')
        self.cli=self.create_client(Spawn,'/spawn')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available,waiting again...')
        self.request=Spawn.Request()

    def send_request(self,x,y,theta):
        self.request.x=x
        self.request.y=y
        self.request.theta=theta
        return self.cli.call_async(self.request)       

def main():
    rclpy.init()

    minimal_client=MinimalClientAsync
    future=minimal_client.send_request(x=5.0, y=5.0, theta=0.0)
    rclpy.spin_until_future_complete(minimal_client, future)
    response= future.result()

    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()