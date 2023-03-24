from hexalattice.hexalattice import *
import numpy as np
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

N = 25
hex_centers, _ = create_hex_grid(nx=N,
                                 ny=N,
                                 do_plot=False)
                                 

x_hex_coords = hex_centers[:, 0]
y_hex_coords = hex_centers[:, 1]

# image_path = '/Users/marielafontaine/Desktop/PHS3903-Simulation/Algo_flocon/emoji_snowflake_thumb.jpg'     # Works with .png, .jpg, .tif
# colors = sample_colors_from_image_by_grid(image_path, x_hex_coords, y_hex_coords)


rho = 0.1
vecteur_d = []

rgb_ini = [0,0,rho]

for i in range(N**2):
    vecteur_d.append(rgb_ini)
center_pts=round(25**2*0.5)
spot1 = 112
spot2 = 320
M = [center_pts,spot1,spot2]
for center in M:
    vecteur_d[center]=[0,0,1]
    vecteur_d[center+N]=[0,0,0.9]
    vecteur_d[center-N]=[0,0,0.9]
    vecteur_d[center-N-1]=[0,0,0.9]
    vecteur_d[center+N-1]=[0,0,0.9]
    vecteur_d[center+1]=[0,0,0.9]
    vecteur_d[center-1]=[0,0,0.9]
    vecteur_d[center+2*N]=[0,0,0.7]
    vecteur_d[center+2*N-1]=[0,0,0.7]
    vecteur_d[center+2*N+1]=[0,0,0.7]
    vecteur_d[center+N+1]=[0,0,0.7]
    vecteur_d[center-2]=[0,0,0.7]
    vecteur_d[center+2]=[0,0,0.7]
    vecteur_d[center-2*N]=[0,0,0.7]
    vecteur_d[center-2*N-1]=[0,0,0.7]
    vecteur_d[center-2*N+1]=[0,0,0.7]
    vecteur_d[center-N+1]=[0,0,0.7]
    vecteur_d[center+N-2] = [0,0,0.7]
    vecteur_d[center-N-2] = [0,0,0.7]

vecteur_d = np.array(vecteur_d)
for i in range(len(vecteur_d)):

    if i%N == 0 :       # left side
        vecteur_d[i][0] = 0.5
    if (i+1)%N == 0 :   # right side
        vecteur_d[i][0] = 0.5
    elif i < N:         # bottom side
        vecteur_d[i][0] = 0.5
    elif i > N*(N-1):   # top side
        vecteur_d[i][0] = 0.5

plot_single_lattice_custom_colors(x_hex_coords, 
                            y_hex_coords,
                            face_color=vecteur_d,
                            edge_color=vecteur_d*0,
                            min_diam=1,
                            plotting_gap=0.0,
                            rotate_deg=0)
plt.show()

for t in range(10):
    for i in range(len(vecteur_d)):

        if i%N == 0 :       # left side
            continue
        if (i+1)%N == 0 :   # right side
            continue
        elif i < N:         # bottom side
            continue
        elif i > N*(N-1):   # top side
            continue    
        else:  
            vecteur_d[i][2]=(vecteur_d[i][2]+vecteur_d[i+1][2]+vecteur_d[i-1][2]+vecteur_d[i+N][2]+vecteur_d[i+N+1][2]+vecteur_d[i-N][2]+vecteur_d[i-N+1][2])/7






# print(vecteur_d)
print("vecd",len(vecteur_d))
print('x_hex shape', x_hex_coords.shape)

plot_single_lattice_custom_colors(x_hex_coords, 
                                  y_hex_coords,
                                    face_color=vecteur_d,
                                    edge_color=vecteur_d*0,
                                    min_diam=1,
                                    plotting_gap=0.0,
                                    rotate_deg=0)
plt.show()