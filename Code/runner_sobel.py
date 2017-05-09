
import model_alphabeta as mab
import model_alphabeta_strongsampling as mss
import data_sobel as data
import numpy as np
import scipy.optimize as optimize


def run1(model, parameters):
	m=model
	m.alpha=parameters[0]
	m.beta=parameters[1]
	m.gamma=0.75#parameters[2]
	m.epsilon=0.05#parameters[3]
	print 'Running with alpha={0}, beta={1}, gamma={2}, epsilon={3}.'\
			.format(m.alpha, m.beta, m.gamma, m.epsilon)
	m.initialize()
	p_NegPos_CorrectActive=m.p_singledata_data(data.test_NegPos[0], data.train_NegPos)
	p_NegPos_WrongActive=m.p_singledata_data(data.test_NegPos[1], data.train_NegPos)
	p_PosOnly_CorrectActive=m.p_singledata_data(data.test_PosOnly[0], data.train_PosOnly)
	p_PosOnly_WrongActive=m.p_singledata_data(data.test_PosOnly[1], data.train_PosOnly)
	return (m.choose(p_NegPos_CorrectActive, p_NegPos_WrongActive),\
		   m.choose(p_PosOnly_CorrectActive, p_PosOnly_WrongActive))

def run2(model, parameters):
	m=model
	m.alpha=parameters[0]
	m.beta=parameters[1]
	m.gamma=0.75#parameters[2]
	m.epsilon=0.05#parameters[3]
	print 'Running with alpha={0}, beta={1}, gamma={2}, epsilon={3}.'\
			.format(m.alpha, m.beta, m.gamma, m.epsilon)
	m.initialize()
	p_Unique_CorrectActive=m.p_singledata_data(data.test_Unique[0], data.train_Unique)
	p_Unique_WrongActive=m.p_singledata_data(data.test_Unique[1], data.train_Unique)
	return (m.choose(p_Unique_CorrectActive, p_Unique_WrongActive))

def compare(p_model):
	exp_data=(data.e_NegPos_Correct, data.e_PosOnly_Correct)
	return np.linalg.norm(p_model-exp_data)	

def model_error(parameters):
	p_model = np.array(run1(parameters))
	exp_data=np.array((data.e_NegPos_Correct, data.e_PosOnly_Correct))
	return np.linalg.norm(p_model-exp_data)
	
#init_params=np.array([0.25, 0.25, 0.9, 0.05])
#res=optimize.minimize(model_error, init_params)
# rranges = (slice(0.01, 0.99, 0.24), slice(0.01, 0.99, 0.24))#, slice(0.99, 0.99, 0.1), slice(0.05, 0.05, 0.5))
# res=optimize.brute(model_error, rranges)
# print(res)

#print(run1(mab,(0.25, 0.25)))
#print(run1(mss,(0.25, 0.25)))

alphabetas=[(0.01,0.97)]#,(0.25, 0.25),(0.5, 0.5)]#, (0.01, 0.25), (0.25, 0.01), (0.25, 0.25), (0.5, 0.5)]
for ab in alphabetas:
	print(run2(mab,ab))
	print(run2(mss,ab))

