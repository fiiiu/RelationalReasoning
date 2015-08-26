import numpy as np

import runner
import data

filename='distances3'

alphas=[0.01, 0.1, 0.33, 0.5, 0.66, 0.9, 0.99]
betas=[0.01, 0.1, 0.33, 0.5, 0.66, 0.9, 0.99]
deltas=[0.01, 0.1, 0.33, 0.5, 0.66, 0.9, 0.99]
distances=np.zeros((len(alphas),len(betas),len(deltas)))

mindist=100
stars=(0,0,0)
pstars=(0,0,0,0)
for i,alpha in enumerate(alphas):
	for j,beta in enumerate(betas):
		for k,delta in enumerate(deltas):
			if alpha+beta+delta>1:
				continue
			p_model=runner.run(alpha, beta, delta)
			dist=runner.compare(p_model)
			distances[i,j,k]=dist
			if dist<mindist:
				stars=(alpha,beta,delta)
				pstars=p_model
				mindist=dist


np.save(filename,distances)

print 'minimizing alpha, beta, delta: {0}'.format(stars)
print 'minimized probabilities: {0}'.format(pstars)
print 'minimized distance: {0}'.format(mindist)


