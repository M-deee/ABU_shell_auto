#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node 

class PlanningNode(Node):  
    def __init__(self):
        super().__init__("planning") 

def main(args=None):
    rclpy.init(args=args)
    node = PlanningNode()  
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()