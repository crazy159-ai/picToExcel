import open3d as o3d
import numpy as np

filename = './res/light.pcd'
pcd = o3d.io.read_point_cloud(filename)
pcd.paint_uniform_color([0.5,0.5,0.5])
pcd_tree = o3d.geometry.KDTreeFlann(pcd)

pcd.colors[200] = [1,0,0]
# o3d.visualization.draw_geometries([pcd])

# K
[k,idx,_] = pcd_tree.search_knn_vector_3d(pcd.points[200],200)
np.asarray(pcd.colors)[idx[1:],:]=[0,1,0]
# o3d.visualization.draw_geometries([pcd])
print(np.asarray(pcd.colors)[:,:])