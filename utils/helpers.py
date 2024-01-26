import numpy as np


def check_points(point_cloud_file_path, point_file_path):
    # Flag for use in API
    is_point = True
    # Load the point cloud data from the .asc file
    point_cloud_data = np.loadtxt(point_cloud_file_path, delimiter=' ')

    # Extract XYZ coordinates from the loaded data
    point_cloud_data = point_cloud_data[:, :3]
    # Load points
    point_data = np.load(point_file_path)

    # Check and return matching points
    matching_indices = np.where(np.all(point_cloud_data == point_data[:, None, :], axis=-1))
    matching_points = point_data[matching_indices[0]]

    # Filter duplicates
    unique_matching_points = np.unique(matching_points)

    # Check if any of the points are not matching, and update flag
    for item in point_data:
        if item not in unique_matching_points:
            is_point = False
            break

    return point_cloud_data, matching_points, is_point

