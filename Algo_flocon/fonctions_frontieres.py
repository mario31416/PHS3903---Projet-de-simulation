import numpy as np

 

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
    if int(np.ceil((center+1)/10)) % 2 == 0 :
        a = vecteur_p[center]
        b = vecteur_p[center+N]
        c = vecteur_p[center+N+1]
        d = vecteur_p[center-1]
        e =vecteur_p[center+1]
        f =vecteur_p[center-N+1] 
        g =vecteur_p[center-N] 

    
    else :
        a = vecteur_p[center]
        b = vecteur_p[center+N-1]
        c = vecteur_p[center+N]
        d = vecteur_p[center-1]
        e =vecteur_p[center+1]
        f =vecteur_p[center-N-1] 
        g =vecteur_p[center-N] 
    return a,b,c,d,e,f,g


def alentours_idx(N, center) :
    if int(np.ceil((center+1)/10)) % 2 == 0 :
        a = center
        b = center+N
        c =  center+N+1
        d =  center-1
        e = center+1
        f = center-N+1
        g = center-N
    else : 
        a = center
        b = center+N-1
        c = center+N
        d = center-1
        e = center+1
        f = center-N-1
        g = center-N

    return  a,b,c,d,e,f,g

def frontiere_g(p, centre) :

    # Fonction qui donne accès aux cellules àvoisinant une cellule sur la frontière gauche 
    # selon la définition de la librairie
    ## a = centre
    # Configuration paire
    #         c             b
    #       a   e         d
    #         g             f
    # 
    # ##

    # Configuration impaire
    #     b   f
    #       a   c              e
    #     d   g
    # 
    # ##
    N = int(np.sqrt(len(p)))
    if centre % 2 == 0 : # On est à la 0eme, 2eme, 4eme, ... ligne (configuration paire)
        a = p[centre]
        b = p[centre + 2*N-1]
        c = p[centre+N]
        d = p[centre + N -1]
        e = p[centre+1]
        f = p[centre - 1]
        g = p[centre-N]

    else : # On est à la 1eme, 3eme, 5eme, ... ligne (Configuration impaire)
        a = p[centre]
        b = p[centre+N]
        c = p[centre+1]
        d = p[centre-N]
        e = p[centre + N -1]
        f = p[centre + N+1]
        g = p[centre - N+1]

    return a,b,c,d,e,f,g




def frontiere_d(p, centre) :

    #      b   c
    #    d   a   e  
    #      f   g   

    # Fonction qui donne accès aux cellules avoisinant une cellule sur la frontière droite 
    # selon la définition de la librairie
    ## a = centre
    # Configuration paire
    #                   b   c
    #       e         d   a
    #                   f   g
    # 
    # ##

    # Configuration impaire
    #       c           b
    #         e       d   a  
    #       g           f 
    # 
    # ##
    N = int(np.sqrt(len(p)))
    if centre % 2 == 0 : # On est à la 0eme, 2eme, 4eme, ... ligne (configuration paire)
        a = p[centre]
        b = p[centre + N-1]
        c = p[centre+N]
        d = p[centre  -1]
        e = p[centre+N-1]
        f = p[centre - N-1]
        g = p[centre-N]

    else : # On est à la 1eme, 3eme, 5eme, ... ligne (Configuration impaire)
        a = p[centre]
        b = p[centre+N]
        c = p[centre+1]
        d = p[centre-1]
        e = p[centre - N +1]
        f = p[centre -N]
        g = p[centre - 2*N+1]

    return a,b,c,d,e,f,g

