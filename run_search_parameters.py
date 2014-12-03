import model_alphabeta as m
import data
import numpy as np
import scipy.optimize

pcorr_1s=0.46
pcorr_2s=0.78
pcorr_1d=0.44
pcorr_2d=0.5


def run_model():
	#print 'running with alpha=beta={0}, gamma={1}, gain={2}'.format(m.alpha,m.gamma,m.gain)
	m.initialize()

	upsamesame=m.p_data_data([data.tests], data.data_same)
	updiffsame=m.p_data_data([data.testd], data.data_same)
	normsamesame=m.p_data_data([data.testsnorm], data.data_same)
	normdiffsame=m.p_data_data([data.testdnorm], data.data_same)
	psamesame=upsamesame/(upsamesame+normsamesame)
	pdiffsame=updiffsame/(updiffsame+normdiffsame)
	upsamediff=m.p_data_data([data.tests], data.data_diff)
	updiffdiff=m.p_data_data([data.testd], data.data_diff)
	normsamediff=m.p_data_data([data.testsnorm], data.data_diff)
	normdiffdiff=m.p_data_data([data.testdnorm], data.data_diff)
	psamediff=upsamediff/(upsamediff+normsamediff)
	pdiffdiff=updiffdiff/(updiffdiff+normdiffdiff)
	psameplussame=m.p_data_data_binormalized([data.tests],data.data_same_plus)
	pdiffplussame=m.p_data_data_binormalized([data.testd],data.data_same_plus)
	psameplusdiff=m.p_data_data_binormalized([data.tests],data.data_diff_plus)
	pdiffplusdiff=m.p_data_data_binormalized([data.testd],data.data_diff_plus)

	return m.choose(psamesame,pdiffsame), m.choose(pdiffdiff,psamediff),\
		m.choose(psameplussame,pdiffplussame), m.choose(pdiffplusdiff,psameplusdiff)

#manual minimization
# m.epsilon=0.05
# alphas=[0.1,0.3]
# gammas=[0.5,0.9]
# gains=[0.7,1,1.8]

# mindist=100
# stars=(0,0,0)
# for gain in gains:
# 	m.gain=gain
# 	for alpha in alphas:
# 		m.alpha=alpha
# 		m.beta=alpha
# 		for gamma in gammas:
# 			m.gamma=gamma

# 			pc1s,pc1d,pc2s,pc2d =run_model()
# 			dist=(pc1s-pcorr_1s)**2+(pc1d-pcorr_1d)**2+(pc2s-pcorr_2s)**2+(pc2d-pcorr_2d)**2
# 			if dist<mindist:
# 				stars=(gain,alpha,gamma)
# 				pstars=pc1s,pc1d,pc2s,pc2d
# 				mindist=dist

# print stars
# print pstars
# print mindist

def model_dist((alpha)):#((gain,gamma,alpha,epsilon)):
	m.gain=1#gain
	m.gamma=0.9#gamma
	m.alpha=alpha
	m.beta=alpha
	m.epsilon=0.01#epsilon
	#m.initialize()
	pc1s,pc1d,pc2s,pc2d =run_model()
	dist=(pc1s-pcorr_1s)**2+(pc1d-pcorr_1d)**2+(pc2s-pcorr_2s)**2+(pc2d-pcorr_2d)**2
	return dist		

import scipy
x0=np.array([1,0.9,0.3,0.01])
x0=np.array([0.3])

res=scipy.optimize.minimize(model_dist,x0)

print res