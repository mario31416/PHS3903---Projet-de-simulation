from hexalattice.hexalattice import *
import numpy as np
from fonctions_frontieres import *
N = 10
hex_centers, _ = create_hex_grid(nx=N,
                                 ny=N,
                                 do_plot=False)
                                 

x_hex_coords = hex_centers[:, 0]
y_hex_coords = hex_centers[:, 1]


rho=0.7
vecteur_d=[]

for i in range(N**2):
    vecteur_d.append(rho)

center=round(N**2*0.5)

#vecteur_d[center] = 0.2

colors = [[1,1,1]]
for i in range(N**2-1) :
    colors.append([1,1,1])

vecteur_d[N] = 0.1
vecteur_d[3*N-1] = 1


for i in range(len(vecteur_d)):
    

    if i > 0 and i < (N**2-1-(N-1)) and i% N == 0: # Frontières gauche en excluant les coins
        print('gauche', i)
        a,b,c,d,e,f,g = frontiere_g(vecteur_d, i)
        vecteur_d[i]=(a+ b+ c+ d+e+f+g)/7
        print(vecteur_d[i])
        colors[i] = [0, 1, vecteur_d[i]]  

        
        continue

    if i > (N-1) and i < (N**2-1) and (i+1) % N == 0: # Frontières droite 
        print('droite', i)
        print(vecteur_d[i])
        a,b,c,d,e,f,g = frontiere_d(vecteur_d, i)
        print(a,b,c,d,e,f,g)
        vecteur_d[i]=(a+ b+ c+ d+e+f+g)/7
        print(vecteur_d[i])
        colors[i] = [1, 0, vecteur_d[i]]
        print('ici')
        continue


    # elif i <= N-1: # Frontière inférieure
    #     colors[i] = [1, 0, vecteur_d[i]]
    #     print('ici')
    #     continue
    # elif i >= N**2-1-(N-1): # Frontière supérieure
    #     colors[i] = [1, 0, vecteur_d[i]]
    #     print('là')
    #     continue 

    # else:
    #     print('calcul')
    #     a,b,c,d,e,f,g = alentours(vecteur_d, i)
    #     vecteur_d[i]=(a+ b+ c+ d+ e+ f+ g)/7
    #     colors[i] = [0, 0, vecteur_d[i]]
    #     print('couleur',colors[i])


colors = np.array(colors)


plot_single_lattice_custom_colors(x_hex_coords,     
                            y_hex_coords,
                            face_color=colors,
                            edge_color=colors*0,
                            min_diam=1,
                            plotting_gap=0.0,
                            rotate_deg=2*np.pi/6)

plt.show()
    