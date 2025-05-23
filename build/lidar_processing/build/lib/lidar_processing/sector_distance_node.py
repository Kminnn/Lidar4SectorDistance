import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class SectorDistanceNode(Node):
    def __init__(self):
        super().__init__('sector_distance_node')
        self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)

    def scan_callback(self, msg):
        ranges = list(msg.ranges)
        n = len(ranges)

        def min_distance(start_idx, end_idx):
            """Get the minimum valid distance in the given index range."""
            sector = ranges[start_idx:end_idx]
            sector = [r for r in sector if 0.05 < r < msg.range_max]
            return min(sector) if sector else float('inf')

        front = min_distance(0, 10) + min_distance(n - 10, n)
        left = min_distance(n // 4 - 5, n // 4 + 5)
        right = min_distance(3 * n // 4 - 5, 3 * n // 4 + 5)
        back = min_distance(n // 2 - 10, n // 2 + 10)

        self.get_logger().info(f'Front: {front:.2f} m | Left: {left:.2f} m | Right: {right:.2f} m | Back: {back:.2f} m')

def main(args=None):
    rclpy.init(args=args)
    node = SectorDistanceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
