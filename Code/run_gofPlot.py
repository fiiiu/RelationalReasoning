import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.cm as cm
from matplotlib import cm
plt.rc('text', usetex=True)
import seaborn as sns

distances=np.load('/Users/mac/Projects/RelationalReasoning/Output/distancesX.npy')



#alphas=np.array([0.01, 0.1, 0.33, 0.5, 0.66, 0.9, 0.99])
#betas=np.array([0.01, 0.1, 0.33, 0.5, 0.66, 0.9, 0.99])
ngrid=11
alphas=np.linspace(0,1,ngrid)
betas=np.linspace(0,1,ngrid)

mdists=np.ma.masked_values(distances,0)

#plt.imshow(distances,cmap=cm.jet)
fig, ax=plt.subplots(1,1)#,figsize=(8,6))

#p=ax.pcolor(alphas, betas, distances, cmap=cm.RdBu)
p=ax.contourf(alphas, betas, 1-mdists.T, cmap=cm.jet)#, interpolation='bicubic')
#p=ax.contour(alphas, betas, mdists, cmap=cm.RdBu, interpolation='cubic')


cb=fig.colorbar(p, ax=ax)

plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\beta$')


plt.show()

