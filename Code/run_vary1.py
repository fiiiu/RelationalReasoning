import numpy as np
import runner_onepar as runner
import data
import time

filename='distances101'

#alphas=[0.01, 0.1, 0.25, 0.33, 0.5]
alphas=np.linspace(0,0.5,101)
print alphas
#alphas=[0.1,0.1,0.1]
#alphas=[0.1, 0.2]
distances=np.zeros((len(alphas)))


mindist=100
stars=(0,0)
pstars=(0,0,0,0)
for i,alpha in enumerate(alphas):
	print 'running with alpha={0}'.format(alpha)
	stime=time.clock()
	p_model=runner.run(alpha)
	print 'took {0:.2f}s'.format(time.clock()-stime)
	dist=runner.compare(p_model)
	distances[i]=dist
	if dist<mindist:
		stars=(alpha)
		pstars=p_model
		mindist=dist


np.save(filename,(alphas,distances))

print 'minimizing alpha, beta: {0}'.format(stars)
print 'minimized probabilities: {0}'.format(pstars)
print 'minimized distance: {0}'.format(mindist)


