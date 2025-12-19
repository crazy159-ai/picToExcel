import open3d as o3d

filename = './res/lena_color.jpg'
img = o3d.io.read_image(filename)
print(img)
o3d.visualization.draw_geometries([img], window_name="Open3D显示img",
                                  width=1024, height=768,
                                  left=50, top=50,
                                  mesh_show_back_face=False  # 是否显示面片背景
                                  ) 