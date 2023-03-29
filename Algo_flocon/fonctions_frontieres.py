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

def somme_vap(paquet):
    som = 0 
    for ele in paquet:
        som = som + ele[3]
    return som/7 

def somme_vap_voisin_cristal(vecteur , center, N):
    som = 0 
    prox = []               #la fonction est qd meme dumb 
    pas_prox =[]            #elle doit fonctionner avec voisin_crystal ahahah
    idx_cristal = voisin_crystal(vecteur, center, N)[0]
    idx_non_voisin = voisin_crystal(vecteur, center, N)[1]
    for idx in idx_cristal:
        prox.append(vecteur[idx])
    
    for i in range(len(prox)):
        prox[i] = vecteur[center,3]

    for idx in idx_non_voisin:
        pas_prox.append(vecteur[idx,3])

    som = (sum(prox)+sum(pas_prox))

    return som/7 

def prox_crystal(vecteur, center):
    is_voisin = 0
    voisin = alentours(vecteur,center)[1:]

    for ele in voisin:
        if ele[0] == 1:
            is_voisin = 1

    return is_voisin

def voisin_crystal(vecteur, center, N):

    idx_voisin = []
    idx_pas_voisin = []
    idx_pts = alentours_idx(N, center)

    for idx in idx_pts:
        un_voisin = vecteur[idx]
        if un_voisin[0] == 1:       # est dans le cristal
            idx_voisin.append(idx)
        else:
            idx_pas_voisin.append(idx)
    
    return idx_voisin, idx_pas_voisin



# Code pour updater Diffusion 

# for t in range(15):
    
#     mask_change = mask_tot
#     for i in range(len(mask_tot)):
#         case = mask_tot[i]
#         if i%N == 0 or (i+1)%N == 0 or i < N or i > N*(N-1):    
#             continue   

#         elif case[0]==1:
#             continue

#         elif prox_crystal(mask_tot,i) != 0: # est a proximité du cristal, condition réfléchie
#             new_value = somme_vap_voisin_cristal(mask_tot, i) #Laplacien condition réfléchie
#             mask_change[i,3] = new_value

#         else:  
#             ele = alentours(mask_tot,i) #
#             new_value = somme_vap(ele)
#             mask_change[i,3] = new_value  
#     mask_tot = mask_change
    
