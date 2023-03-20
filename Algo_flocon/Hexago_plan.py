from hexalattice.hexalattice import *
import numpy as np

N = 25
hex_centers, _ = create_hex_grid(nx=N,
                                 ny=N,
                                 do_plot=False)
                                 

x_hex_coords = hex_centers[:, 0]
y_hex_coords = hex_centers[:, 1]


rho=0.7
vecteur_d=[]
for i in range(N**2-1):
    vecteur_d.append(rho)
center=round(25**2*0.5)
vecteur_d[center]=0
vecteur_d[center+N]=0.1
vecteur_d[center-N]=0.1
vecteur_d[center+N+1]=0.1
vecteur_d[center-N-1]=0.1
vecteur_d[center+1]=0.1
vecteur_d[center-1]=0.1
vecteur_d[center+2*N]=0.1
vecteur_d[center+2*N-1]=0.1
vecteur_d[center+2*N+1]=0.1
vecteur_d[center+N+2]=0.1
vecteur_d[center+N-1]=0.1
vecteur_d[center-2]=0.1
vecteur_d[center+2]=0.1
vecteur_d[center-2*N]=0.1
vecteur_d[center-2*N-1]=0.1
vecteur_d[center-2*N+1]=0.1
vecteur_d[center-N+2]=0.1
vecteur_d[center-N-1]=0.1


# image_path = '/Users/marielafontaine/Desktop/PHS3903-Simulation/Algo_flocon/emoji_snowflake_thumb.jpg'     # Works with .png, .jpg, .tif
# colors = sample_colors_from_image_by_grid(image_path, x_hex_coords, y_hex_coords)
colors=[]


for m in range(N**2-1):
    colors.append([0, 0, 0])

for t in range(50):
    for i in range(len(vecteur_d)):
        if i % N == 0: # on est sur un boundary
            break
        elif i <= N-1:
            break
        elif i >= N**2-1-(N-1):
            break 
        else:
            vecteur_d[i]=(vecteur_d[i]+vecteur_d[i+1]+vecteur_d[i-1]+vecteur_d[i+N]+vecteur_d[i+N+1]+vecteur_d[i-N]+vecteur_d[i-N+1])/7
    for m in range(N**2-1):
        colors[m] = [0, 0, vecteur_d[m]]

    print(colors)
    plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,face_color=colors,edge_color=colors*0,min_diam=1,plotting_gap=0.0,rotate_deg=2*np.pi/6)

plt.show()
    