
import model_alphabeta as m
import data_sobel as data
import numpy as np
import scipy.optimize as optimize


def run(parameters):
	m.alpha=parameters[0]
	m.beta=parameters[1]
	m.gamma=0.99#parameters[2]
	m.epsilon=0.1#parameters[3]
	print 'Running with alpha={0}, beta={1}, gamma={2}, epsilon={3}.'\
			.format(m.alpha, m.beta, m.gamma, m.epsilon)
	m.initialize()
	p_NegPos_CorrectActive=m.p_singledata_data(data.test_NegPos[0], data.train_NegPos)
	p_NegPos_WrongActive=m.p_singledata_data(data.test_NegPos[1], data.train_NegPos)
	p_PosOnly_CorrectActive=m.p_singledata_data(data.test_PosOnly[0], data.train_PosOnly)
	p_PosOnly_WrongActive=m.p_singledata_data(data.test_PosOnly[1], data.train_PosOnly)
	return (m.choose(p_NegPos_CorrectActive, p_NegPos_WrongActive),\
		   m.choose(p_PosOnly_CorrectActive, p_PosOnly_WrongActive))

def compare(p_model):
	exp_data=(data.e_NegPos_Correct, data.e_PosOnly_Correct)
	return np.linalg.norm(p_model-exp_data)	

def model_error(parameters):
	p_model = np.array(run(parameters))
	exp_data=np.array((data.e_NegPos_Correct, data.e_PosOnly_Correct))
	return np.linalg.norm(p_model-exp_data)
	
#init_params=np.array([0.25, 0.25, 0.9, 0.05])
#res=optimize.minimize(model_error, init_params)
rranges = (slice(0.01, 0.99, 0.24), slice(0.01, 0.99, 0.24))#, slice(0.99, 0.99, 0.1), slice(0.05, 0.05, 0.5))
res=optimize.brute(model_error, rranges)
print(res)
