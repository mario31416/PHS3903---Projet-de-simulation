from hexalattice.hexalattice import *
import numpy as np

# ---------PARAMETRES--------------------

rho = 0.3       # Densite


# ----------RESEAU -------------------
N = 10      # Taille de la grille 
hex_centers, _ = create_hex_grid(nx=N,          # Création du résau 
                                 ny=N,
                                 do_plot=False)
                                 
x_hex_coords = hex_centers[:, 0]
y_hex_coords = hex_centers[:, 1]

color_vapor = np.full((N ** 2,3), [1, 0, 0]) # ROUGE pour la vapeur 
color_ice = np.full((N ** 2,3), [0, 0, 1]) # BLEU pour la glace 
color_quasi = np.full((100,3), [0, 1, 0]) # VERT pour quasi-liquid 

colors = color_ice + color_vapor + color_quasi 


mask_tot = np.full((100,4), [0, 0, 0, rho])    # Mask totale a=(0 ou 1 si dans cristal) b : boundary mass (quasi-liquid)
                                    # c : cristal mass (ice) d : diffusive mass (vapor)
mask_tot[int((len(mask_tot) / 2) + N / 2)] = [1, 0, 0, 0]
print(mask_tot)

final_ice = []
for i in range(len(mask_tot)):
    for j in range(3):
        final_ice.append(mask_tot[i])


#colors = np.full((100, 3), [0, 0, 1])
#final_ice_reshaped = np.reshape(final_ice, (N**2, 3))
#final_color = (colors + final_ice_reshaped) / np.max(colors + final_ice_reshaped)

colors = color_ice + color_vapor + color_quasi

plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,       # Plot total des 3 phases 
                                      face_color= colors,
                                      edge_color=colors,
                                      min_diam=1,
                                      plotting_gap=0.0,
                                      rotate_deg=0)


plt.show()


