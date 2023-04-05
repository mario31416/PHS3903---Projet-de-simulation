from hexalattice.hexalattice import *
def plot_ice(mask_tot, color_ice, x_hex_coords, y_hex_coords, N):

    # RESHAPE

    ice = mask_tot[:,2]
    final_mask_ice = []
    for i in range(len(mask_tot)):
        for j in range(3):
            final_mask_ice.append(ice[i])

    final_mask_ice_reshaped = np.reshape(final_mask_ice, (N**2, 3))
    final_color_ice = (color_ice * final_mask_ice_reshaped) / np.max((color_ice * final_mask_ice_reshaped))

    # PLOT

    # plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,       
    #                                     face_color= final_color_ice,
    #                                     edge_color=final_color_ice,
    #                                     min_diam=1,
    #                                     plotting_gap=0.0,
    #                                     rotate_deg=0)
    # plt.title('Mask glace')
    return final_color_ice


def plot_vapeur(mask_tot, color_vapor, x_hex_coords, y_hex_coords, N):
    # RESHAPE
    vapor = mask_tot[:,3]
    final_mask_vapor = []
    for i in range(len(mask_tot)):
        for j in range(3):
            final_mask_vapor.append(vapor[i])

    final_mask_vapor_reshaped = np.reshape(final_mask_vapor, (N**2, 3))
    
    final_color_vapor = (color_vapor * final_mask_vapor_reshaped)  / np.max((color_vapor * final_mask_vapor_reshaped))
    print('final color vaport', final_color_vapor)
    # PLOT

    # plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,       
    #                                   face_color=final_color_vapor,
    #                                   edge_color=final_color_vapor,
    #                                   min_diam=1,
    #                                   plotting_gap=0.0,
    #                                   rotate_deg=0)

    # plt.title('Mask vapeur')
    return final_color_vapor

def plot_quasi(mask_tot, color_quasi, x_hex_coords, y_hex_coords, N):

    # RESHAPE

    quasi_liquid = mask_tot[:,1]
    final_mask_quasi_liquid = []
    for i in range(len(mask_tot)):
        for j in range(3):
            final_mask_quasi_liquid.append(quasi_liquid[i])

    final_mask_quasi_liquid_reshaped = np.reshape(final_mask_quasi_liquid, (N**2, 3))
    final_color_quasi_liquid = (color_quasi * final_mask_quasi_liquid_reshaped) / np.max((color_quasi * final_mask_quasi_liquid_reshaped))

    #PLOT

    # plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,       
    #                                     face_color=final_color_quasi_liquid,
    #                                     edge_color=final_color_quasi_liquid,
    #                                     min_diam=1,
    #                                     plotting_gap=0.0,
    #                                     rotate_deg=0)

    # plt.title('Mask quasi liquid')
    return final_color_quasi_liquid

def plot_total(mask_tot, color_ice, color_vapor, color_quasi, x_hex_coords, y_hex_coords, N):
    #title = input('filename : ')
    final_color_ice = plot_ice(mask_tot, color_ice, x_hex_coords, y_hex_coords, N)
    #plt.savefig(f"{title} ice")
    final_color_vapor = plot_vapeur(mask_tot, color_vapor, x_hex_coords, y_hex_coords, N)
    #plt.savefig(f"{title} vapeur")
    final_color_quasi = plot_quasi(mask_tot, color_quasi, x_hex_coords, y_hex_coords, N)
    #plt.savefig(f"{title} qll")
    final_colors = final_color_ice + final_color_vapor + final_color_quasi
    final_colors_norm = final_colors  / np.max(final_colors)


    plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,       # Plot total des 3 phases 
                                      face_color= final_colors_norm,
                                      edge_color=final_colors_norm,
                                      min_diam=1,
                                      plotting_gap=0.0,
                                      rotate_deg=0)
    plt.title('Mask total')
    #plt.savefig(f"{title} total")
    

def animate_from_jpgs(file_prefix, amount, filetype='.png', animation_name = 'animation.gif', fps=None, duration=None, delete = False):
    '''
    Vous pouvez changer les valeurs des variables en entrée pour avoir un fichier avec le nom et les FPS que vous préférez.
    '''
    
    import imageio
    import os
    
    images = []
    images_path = [file_prefix + str(frame) + filetype for frame in amount]
    for filename in images_path:
        images.append(imageio.imread(filename))

    if (fps and duration) is not None: raise(ValueError('Cannot give both fps and duration values. Choose one.'))
    
    elif fps is not None: imageio.mimsave(animation_name, images, fps=fps)
    
    elif duration is not None: imageio.mimsave(animation_name, images, duration=duration)
    
    else: imageio.mimsave(animation_name, images)

    if delete: 
        for file in images_path:
            if os.path.isfile(file):
                os.remove(file)