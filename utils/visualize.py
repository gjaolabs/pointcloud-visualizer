import open3d as o3d
from utils import functions


# point_cloud_file_path = "../test_data/point_cloud_data.asc"
# point_file_path = "../test_data/points.npy"


def visualizer_function(point_cloud_file_path, point_file_path):
    # Load points
    point_cloud_data, point_data = functions.load_data(point_cloud_file_path, point_file_path)

    # Create Open3D point cloud
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(point_cloud_data)

    # Check and return matching points
    matching_points = functions.check_matching_points(point_cloud_data, point_data)

    # Assign color for matching points (black)

    matching_colors = functions.assign_color(matching_points, [0, 0, 0])

    # Create an Open3D point cloud for matching points
    matching_cloud = o3d.geometry.PointCloud()
    matching_cloud.points = o3d.utility.Vector3dVector(matching_points)
    matching_cloud.colors = o3d.utility.Vector3dVector(matching_colors)

    # Visualize the point cloud and matching points
    o3d.visualization.draw_geometries([matching_cloud, point_cloud])

# Example usage:
# visualizer_function(point_cloud_file_path, point_file_path)
