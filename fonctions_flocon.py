import numpy as np

# masse frontière (qtité quasi-liquide) b(t+1) = b(t) + (1-κ)d(t) 
def quasi_liquide(b0, kappa, d0) :
    return b0 + (1-kappa)*d0

# masse cristal (qtité de glace) c(t+1) = c(t) + κd(t) 
def glace(c0, kappa, d0) :
    return c0 + kappa*d0

# masse diffusive

def vapeur(d0) :
    
    return d0

# Creation matrice 10 x 10
grid = np.ones((10,10))
print(grid)




