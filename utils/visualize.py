import numpy as np
import open3d as o3d
from utils import helpers
import asyncio

# point_cloud_file_path = "../test_data/point_cloud_data.asc"
# point_file_path = "../test_data/points.npy"


def visualizer_function(point_cloud_file_path, point_file_path):
    # Load the point cloud and the point to be checked and return modified(xyz) point cloud and matching points
    point_cloud_data, matching_points, flag = helpers.check_points(point_cloud_file_path, point_file_path)

    # Create Open3D point cloud
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(point_cloud_data)

    # Assign color for matching points (black)
    matching_color = [0, 0, 0]
    matching_colors = np.full_like(matching_points, matching_color)

    # Create an Open3D point cloud for matching points
    matching_cloud = o3d.geometry.PointCloud()
    matching_cloud.points = o3d.utility.Vector3dVector(matching_points)
    matching_cloud.colors = o3d.utility.Vector3dVector(matching_colors)

    # Visualize the point cloud and matching points
    o3d.visualization.draw_geometries([matching_cloud, point_cloud])

    return flag

# Example usage:
# visualizer_function(point_cloud_file_path, point_file_path)
