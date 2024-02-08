# PointCloud Visualizer

## Overview

This repository contains a PointCloud Visualizer that allows you to visualize point clouds efficiently. Follow the steps below to set up and run the application.

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone git@github.com:gjaolabs/pointcloud-visualizer.git
```

### 2. Install Python

Ensure you have Python installed on your machine. Note that the latest version may not be compatible with Open3D. Version 3.11 is recommended for compatibility.

### 3. Install pip

If you don't have pip (Python package manager) installed, you can follow the instructions on the official website: [Installing pip](https://pip.pypa.io/en/stable/installation/)

### 4. Setup Virtual Environment

Create and activate a virtual environment (venv) to isolate the project dependencies. This helps to maintain a clean and reproducible environment. Use the following commands:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 5. Install Dependencies

Run the following command to install the required dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 6. Setup Endpoint Tool (e.g., Postman)

Configure an endpoint tool like Postman to interact with the PointCloud Visualizer API.

### 7. Make a POST Request

Using Postman, make a POST request to the specified endpoint and port (Flask default is port 5000; for this current implementation we use port 5050) with the `/test` endpoint, sending a JSON object in the request body as specified in `post.json`.

## Example Usage
An alternative to sending the request with Postman, can be achieved by using the cURL command line tool:
```bash
curl -X POST http://localhost:5050/test -H "Content-Type: application/json" -d @post.json
```

Feel free to replace `http://localhost:5050` with your actual server information.

Now you're ready to visualize your point clouds with the PointCloud Visualizer! If you encounter any issues, please refer to the documentation or raise an issue on the repository.

## Important Notes

Due to the technical capabilities of the Open3D library, it is advised to be aware of the following considerations:

- **Visualization Restart:** You may need to restart the visualization process a few times to achieve the desired output. This is a known behavior due to the intricacies of handling point clouds within the Open3D framework.

- **Platform Variability:** The visualization may exhibit variations when running on different machines with distinct GPUs and environments. It's recommended to be mindful of potential differences in performance and rendering across platforms.

## Development Environment

This version of the PointCloud Visualizer was developed on a system running Windows 11, utilizing PyCharm as the integrated development environment (IDE), and Python 3.11. These specific versions were chosen for compatibility with the Open3D library and to provide a stable development environment. If you encounter any issues or have specific requirements, consider adjusting your development environment accordingly. Feel free to explore the Open3D documentation for platform-specific considerations.