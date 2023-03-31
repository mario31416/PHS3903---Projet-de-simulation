from hexalattice.hexalattice import *
import numpy as np
from fonctions_frontieres import *
from fonctions_plot import *

# ---------PARAMETRES--------------------

rho = 0.3       # Densite
kappa = 0.5     # Freezing parameter
iterations = 5 # Number of iterations 


# ----------RESEAU -------------------
N=7# Taille de la grille 
hex_centers, _ = create_hex_grid(nx=N,          # Création du résau 
                                 ny=N,
                                 do_plot=False)
                                 
x_hex_coords = hex_centers[:, 0]
y_hex_coords = hex_centers[:, 1]

color_vapor = np.full((N ** 2,3), [1, 0, 0]) # ROUGE pour la vapeur 
color_ice = np.full((N ** 2,3), [0, 0, 1]) # BLEU pour la glace 
color_quasi = np.full((N ** 2,3), [0, 1, 0]) # VERT pour quasi-liquid 

colors_init = color_ice + color_vapor + color_quasi 

# --------------------------- MASK INITIAL --------------------
mask_tot = np.full((N ** 2,4), [0, 0, 0, rho])    # Mask totale a=(0 ou 1 si dans cristal) b : boundary mass (quasi-liquid)
                                    # c : cristal mass (ice) d : diffusive mass (vapor)


mask_tot[int((len(mask_tot) / 2)-N/2)] = [1, 0, 1, 0]       # On fixe au milieu une cellule gelée 
centre = int((len(mask_tot) / 2)-N/2 )
# ----------------------FONCTIONS ÉVOLUTION---------------------------


def freezing(mask0, N, centre, kappa) :
    ## b0, d0 = masques initiaux 
    # centre = index
    mask1 = mask0
    idxa,idxb,idxc,idxd,idxe,idxf,idxg = alentours_idx(N,centre)


    idx = [idxb,idxc,idxd,idxe,idxf,idxg]
    for i in range(len(idx)) :
        mask1[idx[i],1] = mask0[idx[i], 1] + ((1-kappa)*mask0[idx[i], 3])

        mask1[idx[i],2]= mask0[idx[i], 1] + (kappa*mask0[idx[i], 3])

        mask1[idx[i],3] = 0

    return mask1



# -----------------------UDPDATE MASK ------------------------------

for t in range(15):
    
    mask_change = mask_tot
    for i in range(len(mask_tot)):
        case = mask_tot[i]
        if i%N == 0 or (i+1)%N == 0 or i < N or i > N*(N-1):    
            continue   

        elif case[0]==1:
            continue

        elif prox_crystal(mask_tot,i) != 0: # est a proximité du cristal, condition réfléchie
            new_value = somme_vap_voisin_cristal(mask_tot, i, N) #Laplacien condition réfléchie
            mask_change[i,3] = new_value

        else:  
            ele = alentours(mask_tot,i) #
            new_value = somme_vap(ele)
            mask_change[i,3] = new_value  
    mask_tot = mask_change





# ---------------------PLOT RESULTS------------------------------------

""""
TUTO PLOT :    
    - Pour  plot tout : plot_total(mask_tot, color_ice, color_vapor, color_quasi, x_hex_coords, y_hex_coords, N)

    POUR UNE SEULE PHASE AJOUTER plt.show()

    - Pour plot glace : plot_ice(mask_tot, color_ice, x_hex_coords, y_hex_coords, N)
    - Pour plot vapeur : plot_vapeur(mask_tot, color_vapor, x_hex_coords, y_hex_coords, N)
    - pour plot QLL : plot_quasi(mask_tot, color_quasi, x_hex_coords, y_hex_coords, N)
"""
plot_total(mask_tot, color_ice, color_vapor, color_quasi, x_hex_coords, y_hex_coords, N)




