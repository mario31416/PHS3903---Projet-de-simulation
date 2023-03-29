from hexalattice.hexalattice import *
import numpy as np
from fonctions_frontieres import *

# ---------PARAMETRES--------------------

rho = 0.3       # Densite
kappa = 0.5     # Freezing parameter
iterations = 5 # Number of iterations 


# ----------RESEAU -------------------
N=10# Taille de la grille 
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







# ---------------------PLOT RESULTS------------------------------------

mask_tot = freezing(mask_tot, N, centre, 0.05)

# GLACE 
ice = mask_tot[:,2]
final_mask_ice = []
for i in range(len(mask_tot)):
    for j in range(3):
        final_mask_ice.append(ice[i])

final_mask_ice_reshaped = np.reshape(final_mask_ice, (N**2, 3))
final_color_ice = (color_ice * final_mask_ice_reshaped) 
# VAPEUR
vapor = mask_tot[:,3]
final_mask_vapor = []
for i in range(len(mask_tot)):
    for j in range(3):
        final_mask_vapor.append(vapor[i])

final_mask_vapor_reshaped = np.reshape(final_mask_vapor, (N**2, 3))
final_color_vapor = (color_vapor * final_mask_vapor_reshaped) 


# QUASI-LIQUIDE
quasi_liquid = mask_tot[:,1]
final_mask_quasi_liquid = []
for i in range(len(mask_tot)):
    for j in range(3):
        final_mask_quasi_liquid.append(quasi_liquid[i])

final_mask_quasi_liquid_reshaped = np.reshape(final_mask_quasi_liquid, (N**2, 3))
final_color_quasi_liquid = (color_quasi * final_mask_quasi_liquid_reshaped) 



final_colors = final_color_ice + final_color_vapor + final_color_quasi_liquid

# PLOT

plt.figure(1)
plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,       # Plot total des 3 phases 
                                      face_color= final_colors,
                                      edge_color=final_colors,
                                      min_diam=1,
                                      plotting_gap=0.0,
                                      rotate_deg=0)
plt.title('Mask total')
plt.figure(2)

plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,       
                                      face_color= final_color_ice,
                                      edge_color=final_color_ice,
                                      min_diam=1,
                                      plotting_gap=0.0,
                                      rotate_deg=0)
plt.title('Mask glace')

plt.figure(3)

plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,       
                                      face_color=final_color_vapor,
                                      edge_color=final_color_vapor,
                                      min_diam=1,
                                      plotting_gap=0.0,
                                      rotate_deg=0)

plt.title('Mask vapeur')

plt.figure(4)

plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,       
                                      face_color=final_color_quasi_liquid,
                                      edge_color=final_color_quasi_liquid,
                                      min_diam=1,
                                      plotting_gap=0.0,
                                      rotate_deg=0)

plt.title('Mask quasi liquid')




plt.show()

