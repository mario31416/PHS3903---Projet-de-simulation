rho = 0.9
N=25
vecteur_d=[]
for i in range(N**2-1):
    vecteur_d.append(rho)
center=round(25**2*0.5)
vecteur_d[center]=0
vecteur_d[center+N]=0.1
vecteur_d[center-N]=0.1
vecteur_d[center+N+1]=0.1
vecteur_d[center-N-1]=0.1
vecteur_d[center+1]=0.1
vecteur_d[center-1]=0.1
vecteur_d[center+2*N]=0.1
vecteur_d[center+2*N-1]=0.1
vecteur_d[center+2*N+1]=0.1
vecteur_d[center+N+2]=0.1
vecteur_d[center+N-1]=0.1
vecteur_d[center-2]=0.1
vecteur_d[center+2]=0.1
vecteur_d[center-2*N]=0.1
vecteur_d[center-2*N-1]=0.1
vecteur_d[center-2*N+1]=0.1
vecteur_d[center-N+2]=0.1
vecteur_d[center-N-1]=0.1

for t in range(50):
    for i in range(len(vecteur_d)):
        vecteur_d[i]=(vecteur_d[i]+vecteur_d[i+1]+vecteur_d[i-1]+vecteur_d[i+N]+vecteur_d[i+N+1]+vecteur_d[i-N]+vecteur_d[i-N+1])/7

