import open3d as o3d
import numpy as np

class cfg:
    filepath = './res/'
    filename = filepath + 'bunny.ply'

pcd = o3d.io.read_point_cloud(cfg.filename)
print(pcd)