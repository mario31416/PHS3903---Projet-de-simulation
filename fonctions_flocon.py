import numpy as np
import matplotlib.pyplot as plt

from hexalattice.hexalattice import *

N = 10
hex_centers, _ = create_hex_grid(nx=N,
                                 ny=N,
                                 do_plot=False)
                                 

x_hex_coords = hex_centers[:, 0]
y_hex_coords = hex_centers[:, 1]



plt.show()
# masse frontière (qtité quasi-liquide) b(t+1) = b(t) + (1-κ)d(t) 
def quasi_liquide(b0, kappa, d0, a) :
    ## b0, d0 = masques initiaux 
    for i in range(len(b0-1)) :
        if a[i] == 1 :
            b0[i] = b0[i] + (1-kappa)*d0[i]
    return b0


# masse cristal (qtité de glace) c(t+1) = c(t) + κd(t) 
def glace(c0, kappa, d0, a) :
    for i in range(len(b0-1)) :
        if a[i] == 1 :
            c0[i] = c0[i] + kappa*d0[i]
    return c0


# masse diffusive
def vapeur(d0, m, grid, N) :

    d = (grid[m] + grid[m+N]+ grid[m+N-1]+grid[m-N-1]+grid[m-N]+grid[m+1]+grid[m-1]) / 7
    return d
#initialisation
b0 = 0

c0=1
kappa = 0.05



# Creation matrice 10 x 10
# Pour naviguer : grid[ligne, colonne], compage à partir de 0
# Ex : grid[4,3] = 4eme col (colonne #3), 5eme ligne (ligne #4), on compte à partir de 0

grid = np.ones((100))
#grid[44] = quasi_liquide(b0, kappa, d0)

# for t in range(99) :
#     grid[t] = 5



#     grid = np.reshape(grid,(10,10))
#     print(grid)

#     plt.imshow(grid)
#     plt.show()
#     grid = np.reshape(grid,(100))



# plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,
#                                       face_color=grid,
#                                       edge_color=grid*0,
#                                       min_diam=1,
#                                       plotting_gap=0.0,
#                                       rotate_deg=0)










