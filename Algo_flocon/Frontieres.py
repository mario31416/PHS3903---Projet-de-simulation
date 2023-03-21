from hexalattice.hexalattice import *
import numpy as np

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



def alentours(vecteur_p, center) :
    # Fonction qui donne accès aux cellules àvoisinant une cellule centrale 
    # selon la définition de la librairie
    ## 
    #      b   c
    #    d   a   e  
    #      f   g   
    # 
    # ##
    N = int(np.sqrt(len(vecteur_p)))

    a = vecteur_p[center]
    b = vecteur_p[center+N-1]
    c = vecteur_p[center+N]
    d = vecteur_p[center-1]
    e =vecteur_p[center+1]
    f =vecteur_p[center-N-1] 
    g =vecteur_p[center-N] 
    return a,b,c,d,e,f,g





colors = [[1,1,1]]
for i in range(N**2-1) :
    colors.append([1,1,1])



#for t in range(2*N-1):
for i in range(len(vecteur_d)):
    print(i)
    

    if i % N == 0: # Frontières gauche 
        print('allo')
        continue

    if (i+1) % N == 0: # Frontières droite 
        print('allo')
        continue


    elif i <= N-1: # Frontière inférieure
        print('ici')
        continue
    elif i >= N**2-1-(N-1): # Frontière supérieure
        print('là')
        continue 

    else:
        print('calcul')
        a,b,c,d,e,f,g = alentours(vecteur_d, i)
        vecteur_d[i]=(a+ b+ c+ d+ e+ f+ g)/7
        colors[i] = [0, 0, vecteur_d[i]]


colors = np.array(colors)


plot_single_lattice_custom_colors(x_hex_coords,     
                            y_hex_coords,
                            face_color=colors,
                            edge_color=colors*0,
                            min_diam=1,
                            plotting_gap=0.0,
                            rotate_deg=2*np.pi/6)

plt.show()
    