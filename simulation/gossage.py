from hexalattice.hexalattice import *
import numpy as np
import math

rho = 0.3       # Densite
N = 6

color_vapor = np.full((N ** 2,3), [1, 0, 0]) # ROUGE pour la vapeur 
color_ice = np.full((N ** 2,3), [0, 0, 1]) # BLEU pour la glace 
color_quasi = np.full((N ** 2,3), [0, 1, 0]) # VERT pour quasi-liquid 

colors_init = color_ice + color_vapor + color_quasi 

# --------------------------- MASK INITIAL --------------------
mask_tot = np.full((N ** 2,4), [0, 0, 0, rho])    # Mask totale a=(0 ou 1 si dans cristal) b : boundary mass (quasi-liquid)
                                    # c : cristal mass (ice) d : diffusive mass (vapor)
mask_tot[int((len(mask_tot) / 2) + N / 2)] = [0, 0, 0, 1]       # On fixe au milieu une cellule gelée


def update_vapeur(mask_vap,N):
    for i in range(len(mask_vap)):
        mask_final = mask_vap
        if i%N == 0 :       # left side
            continue
        if (i+1)%N == 0 :   # right side
            continue
        elif i < N:         # bottom side
            continue
        elif i > N*(N-1):   # top side
            continue     

        # Laplacien !!
        if math.floor(i/N)%2 == 0:
            print('a')
            mask_final[i][3]=(mask_vap[i][3]+mask_vap[i+1][3]+mask_vap[i-1][3]+mask_vap[i+N][3]+mask_vap[i+N-1][3]+mask_vap[i-N][3]+mask_vap[i-N-1][3])/7
        else :
            print('b')
            mask_final[i][3]=(mask_vap[i][3]+mask_vap[i+1][3]+mask_vap[i-1][3]+mask_vap[i+N][3]+mask_vap[i+N+1][3]+mask_vap[i-N][3]+mask_vap[i-N+1][3])/7
        return mask_final
    
#print(mask_tot)

for t in range(5):
    mask_tot = update_vapeur(mask_tot,N)
    #print(mask_tot)