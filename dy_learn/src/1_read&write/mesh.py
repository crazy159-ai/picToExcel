import open3d as o3d
import numpy as np

filename = './res/frag_115.ply'
mesh = o3d.io.read_triangle_mesh(filename)
print(type(mesh))
# print(np.asarray(mesh.vertices))
# print(np.asarray(mesh.triangles))

mesh.compute_vertex_normals()
print(np.asarray(mesh.triangle_normals))

mesh.paint_uniform_color([1, 0.7, 0])  # 给mesh渲染颜色
o3d.visualization.draw_geometries([mesh], window_name="Open3D显示mesh模型",
                                  width=1024, height=768,
                                  left=50, top=50,
                                  mesh_show_wireframe=True,  # 是否以格网线的形式显示
                                  mesh_show_back_face=False  # 是否显示面片背景
                                  )  # 显示mesh模型


