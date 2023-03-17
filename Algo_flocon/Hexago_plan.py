from hexalattice.hexalattice import *
import numpy as np

N = 10
hex_centers, _ = create_hex_grid(nx=N,
                                 ny=N,
                                 do_plot=False)
                                 

x_hex_coords = hex_centers[:, 0]
y_hex_coords = hex_centers[:, 1]

# image_path = '/Users/marielafontaine/Desktop/PHS3903-Simulation/Algo_flocon/emoji_snowflake_thumb.jpg'     # Works with .png, .jpg, .tif
# colors = sample_colors_from_image_by_grid(image_path, x_hex_coords, y_hex_coords)

a = [[1,1,1]]
for i in range(N**2-1) :
    a.append([1,1,1])

colors = np.array(a)
print('a', a)

M = [25, 63, 66]
for m in M:
    colors[m] = [0, 0, 0]
    colors[m+N] = [1, 0, 1]
    colors[m+N-1] = [1, 0, 1]
    colors[m-N-1] = [1, 0, 1]
    colors[m-N] = [1, 0, 1]
    colors[m+1] = [1, 0, 1]
    colors[m-1] = [1, 0, 1]


plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,
                                      face_color=colors,
                                      edge_color=colors*0,
                                      min_diam=1,
                                      plotting_gap=0.0,
                                      rotate_deg=0)
plt.show()