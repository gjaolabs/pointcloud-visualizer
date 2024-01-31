import numpy as np


def check_matching_points(point_cloud_data, point_data):
    # Check and return matching points
    matching_indices = np.where(np.all(point_cloud_data == point_data[:, None, :], axis=-1))
    matching_points = point_data[matching_indices[0]]

    return matching_points


def return_flag(point_cloud_file_path, point_file_path):
    # Flag for use in API
    is_point = True
    # Load point cloud and point
    point_cloud_data, point_data = load_data(point_cloud_file_path, point_file_path)
    # Get matching points
    matching_points = check_matching_points(point_cloud_data, point_data)

    # Filter duplicates
    unique_matching_points = np.unique(matching_points)

    for item in point_data:
        if item not in unique_matching_points:
            is_point = False
            break

    return is_point


def load_data(point_cloud_file_path, point_file_path):
    # Load the point cloud data from the .asc file
    point_cloud_data = np.loadtxt(point_cloud_file_path, delimiter=' ')

    # Extract XYZ coordinates from the loaded data
    point_cloud_data = point_cloud_data[:, :3]

    point_data = np.load(point_file_path)

    return point_cloud_data, point_data


def assign_color(points, color):
    return np.full_like(points, color)
