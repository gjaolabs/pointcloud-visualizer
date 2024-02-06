import numpy as np


def get_matching_points(point_cloud_data, point_data):

    # Check and return matching points
    matching_indices = np.where(np.all(point_cloud_data == point_data[:, None, :], axis=-1))

    matching_points = point_data[matching_indices[0]]

    return matching_points


def check_matching_points(point_cloud_data, point_data):

    # Get matching points
    matching_points = get_matching_points(point_cloud_data, point_data)

    # Filter duplicates
    unique_matching_points = np.unique(matching_points)

    # Return TRUE if all points belong to the cloud
    return unique_matching_points.size == point_data.size


def load_data(point_cloud_file_path, point_file_path):

    # Load the point cloud data from the .asc file as a numpy array
    point_cloud_data = np.loadtxt(point_cloud_file_path, delimiter=' ')

    # Extract XYZ coordinates from the numpy array
    point_cloud_data = point_cloud_data[:, :3]

    # Load numpy array
    point_data = np.load(point_file_path)

    # Return the point cloud and (potential) matching point numpy arrays
    return point_cloud_data, point_data


def assign_color(points, color):
    return np.full_like(points, color)
