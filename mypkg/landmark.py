#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Junsei Iimori <craftboy0228@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LandMarkGPS(Node):
    def __init__(self):
        super().__init__('landmark_gps')
        self.publisher_ = self.create_publisher(String, 'landmark_gps_topic', 10)
        self.timer = self.create_timer(2.0, self.publish_landmark_coordinates)
        self.landmarks = [
            {"name": "エッフェル塔", "latitude": 48.8583, "longitude": 2.2944},
            {"name": "自由の女神", "latitude": 40.6892, "longitude": -74.0445},
            {"name": "東京タワー", "latitude": 35.6586, "longitude": 139.7454},
            {"name": "シドニー・オペラハウス", "latitude": -33.8568, "longitude": 151.2153},
            {"name": "ギザのピラミッド", "latitude": 29.5845, "longitude": 31.0803},
            {"name": "モン・サン=ミシェル", "latitude": 48.3810, "longitude": -1.511111},
]
        self.index = 0

    def publish_landmark_coordinates(self):
        landmark = self.landmarks[self.index]
        message = String()

        message.data = (f'{landmark["name"]}: 緯度 {landmark["latitude"]}, 'f'経度 {landmark["longitude"]}')

        self.get_logger().info(f'Publishing: {self.index}')
        self.publisher_.publish(message)
        self.index = (self.index + 1) % len(self.landmarks)

def main(args=None):
    rclpy.init(args=args)
    landmark_gps = LandMarkGPS()
    rclpy.spin(landmark_gps)
    landmark_gps.destroy_node()
    rclpy.shutdow

if __name__ == '__main__':
    main()
