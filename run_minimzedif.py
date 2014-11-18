import model
import data

epsilons=[0.001,0.005,0.01,0.02,0.05,0.1,0.2,0.5]
biases=[0.5,0.6,0.75,0.9,0.95,0.98,0.99]

msofar=1000
for epsilon in epsilons:
	for bias in biases:
		model.epsilon=epsilon
		model.individual_bias=bias
		ps=model.p_data_data_binormalized([data.tests],data.data_same)
		pd=model.p_data_data_binormalized([data.testd],data.data_same)
		psd=model.p_data_data_binormalized([data.tests],data.data_diff)
		pdf=model.p_data_data_binormalized([data.testd],data.data_diff)
		if abs(ps-pd)+abs(psd-pdf)<msofar:
			epstar=epsilon
			bistar=bias
			psstar=ps
			pdstar=pd
			psdstar=psd
			pdfstar=pdf
			msofar=abs(ps-pd)+abs(psd-pdf)

print "ps: {0}, pd: {1}, absdif: {2}\n epsilon: {3}, bias: {4}".format(psstar,pdstar,msofar,epstar, bistar)