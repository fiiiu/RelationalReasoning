import model_alphabeta as m
import data
import numpy as np
import scipy.optimize

m.initialize()

pcorr_1s=data.truepsamesameE1 #0.46
pcorr_2s=data.truepsamesameE2 #0.78
pcorr_1d=data.truepdiffdiffE1 #0.44
pcorr_2d=data.truepdiffdiffE2 #0.5

manual=True
auto=False
test=True

def run_model(a,b,g,e):
	#print 'running with alpha={0}, beta={1}, gamma={2}, gain={3}'.format(m.alpha,m.beta,m.gamma,m.gain)
	m.change_parameters(a,b,g,e)		
	print 'running with alpha={0}, beta={1}, gamma={2}, epsilon={3}'.format(m.alpha,m.beta,m.gamma,m.epsilon)

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
if manual:
	epsilons=[0.001, 0.01, 0.05, 0.1, 0.25]
	alphas=[0.01, 0.05, 0.2, 0.33, 0.5, 0.9]
	betas=[0.01, 0.05, 0.2, 0.33, 0.5, 0.9]
	gammas=[0.01, 0.1, 0.5, 0.9, 0.99]
	#gains=[1]#[0.7,1,1.8]
	if test:
		epsilons=[0.01]
		alphas=[0.05]
		betas=[0.05]
		gammas=[0.1, 0.5, 0.9]

	mindist=100
	stars=(0,0,0)
	pstars=(0,0,0,0)
	for e in epsilons:
		for a in alphas:
			for b in betas:
				if a+b>1:
					continue
				for g in gammas:
					pc1s,pc1d,pc2s,pc2d =run_model(a,b,g,e)
					dist=(pc1s-pcorr_1s)**2+(pc1d-pcorr_1d)**2+(pc2s-pcorr_2s)**2+(pc2d-pcorr_2d)**2
					if dist<mindist:
						stars=(a,b,g,e)
						pstars=pc1s,pc1d,pc2s,pc2d
						mindist=dist

	print stars
	print pstars
	print mindist



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

if auto:
	import scipy
	x0=np.array([1,0.9,0.3,0.01])
	x0=np.array([0.3])

	res=scipy.optimize.minimize(model_dist,x0)

	print res