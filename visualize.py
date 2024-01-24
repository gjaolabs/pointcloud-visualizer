import numpy as np
import open3d as o3d

# Step 1: Load the point cloud from the .asc file
file_path = 'test_data/point_cloud_data.asc'
point_cloud_data = np.loadtxt(file_path, delimiter=' ')

# Step 2: Extract XYZ coordinates from the loaded data
xyz = point_cloud_data[:, :3]

# Step 3: Create an Open3D point cloud
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(xyz)

# Step 4: Visualize the point cloud
o3d.visualization.draw_geometries([point_cloud])
