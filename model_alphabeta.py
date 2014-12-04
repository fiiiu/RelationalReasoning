import scipy.misc
import itertools
import numpy as np
from copy import deepcopy

gain=1.8
n_shapes=6
shapes=range(n_shapes)
t_space=[0,1,2]
#n_comb2=int(scipy.misc.comb(n_shapes,2))
h_space=[]

#parameters
initialized=False
alpha=0.3#0.33
beta=0.3#0.01
gamma=0.5
epsilon=0.01#1e-1
hypotheses={}
norms=[0,0,0]


###TOOLS
def print_normalized(f, space):
	norm=0
	vals=[]
	for x in space:
		vals.append(f(x))
		norm+=vals[-1]
	print [val/norm for val in vals]
	return vals 


###INFERENCE
def p_data_data_SLOW(d_new,d_old):#inefficient, could take p_hs out of the loop..
	p=0
	for t in t_space:
		for h in h_space:
			p+=p_data_hypothesis(d_new,h)*p_data_hypothesis(d_old,h)/p_data(d_old)*\
				p_hypothesis_theory(h,t)*p_theory(t)
	return p


# def p_data_data(d_new,d_old):#optimized, but CHECK! WRONG! can't multiply there.
# 	p=0
# 	for t in t_space:
# 		for h in h_space:
# 			p+=p_data_hypothesis(d_new,h)*p_data_hypothesis(d_old,h)*\
# 				p_hypothesis_theory(h,t)
# 		p*=p_theory(t)
# 	p/=p_data(d_old)
# 	return p

def p_data_data(d_new,d_old):#optimized, but CHECK! --slightly inneficient calling p_theory too much
	p=0
	for h in h_space:
		this_factor=p_data_hypothesis(d_new,h)*p_data_hypothesis(d_old,h)
		for t in t_space:
			p+=p_hypothesis_theory(h,t)*p_theory(t)*this_factor
	p/=p_data(d_old)
	return p



def p_data_data_binormalized(d_new,d_old): #INEFFICENT
	d_plus=[[],0]
	d_plus[0]=d_new[0][0]
	d_minus=[[],0]
	d_minus[0]=d_new[0][0]
	d_plus[1]=True
	d_minus[1]=False
	p_plus=p_data_data([d_plus],d_old)
	p_minus=p_data_data([d_minus],d_old)
	return p_data_data(d_new,d_old)/(p_plus+p_minus)



def p_data(d):
	p=0
	for t in t_space:
		this_factor=p_theory(t)
		for h in h_space:
			if h[0]!=t: #efficency, x2
				continue
			p+=p_data_hypothesis(d,h)*p_hypothesis_theory(h,t)*this_factor
	return p 

# def choose(p1,p2):
# 	return 1./(1+np.exp(-gain*(p1-p2)))

def choose(p1,p2,sigmoid=False):
	p=p1/(p1+p2)
	if not sigmoid:
		return p
	else:
		x=p/(1-p)
		return 1./(1+np.exp(-gain*x))


def p_theory_data(t,d):
	p=0
	for h in h_space:
		p+=p_data_hypothesis(d,h)*p_hypothesis_theory(h,t)
	p/=p_data(d)
	p*=p_theory(t)
	return p


###BLOCKS
def p_theory(t):
	if t==0:
		return 1-alpha-beta
	elif t==1:
		return alpha
	elif t==2:
		return beta


def unnormalized_p_hypothesis_theory(h,t):
	#removing check for efficiency
	#if h not in h_space:
	#	print 'invalid h!'
	#	return 

	h0,h1,h2=h
	if t==h0:
		return gamma**h1
	else:
		return 0


def p_hypothesis_theory(h,t):
	#removing this check for efficiency, 10x gain
	# if h not in h_space:
	# 	print 'invalid h!'
	# 	return 

	h0,h1,h2=h
	if t==h0:
		return (gamma**h1)/norms[t]
	else:
		return 0


def p_data_hypothesis(dlist,h):
	p=1
	for d in dlist:
		p*=p_singledata_hypothesis(d,h)
	return p


def initialize():
	build_hypotheses()
	compute_htnormalizers()
	initialized=True


def compute_htnormalizers():
	for t in t_space:
		norms[t]=sum([unnormalized_p_hypothesis_theory(h,t) for h in h_space])


def build_hypotheses():
	h0=0 #single shape
	for h1 in range(n_shapes+1):
		h2=0
		for these_shapes in itertools.combinations(shapes, h1):
			hypotheses[(h0,h1,h2)]=these_shapes
			h_space.append((h0,h1,h2))
			h2+=1

	h0=1 #same double shape
	for h1 in range(1, n_shapes+1):
		h2=0
		for these_shapes in itertools.combinations(shapes, h1):
			hypotheses[(h0,h1,h2)]=these_shapes
			h_space.append((h0,h1,h2))
			h2+=1

	h0=2 #diff double shape
	different_pairs=[pair for pair in itertools.combinations(shapes, 2)]
	for h1 in range(1, n_shapes+1):
		h2=0
		for these_pairs in itertools.combinations(different_pairs,h1):
			hypotheses[(h0,h1,h2)]=these_pairs
			h_space.append((h0,h1,h2))
			h2+=1


def p_singledata_hypothesis(d,h):
	#removing this check for efficiency, 5x gain
	# if h not in h_space:
	# 	print 'invalid h'
	# 	return

	#h0,h1,h2=h

	if h[0]==0: #single shape
		if (d[1] and (d[0][0] in hypotheses[h] or d[0][1] in hypotheses[h])) or\
		   (not d[1] and (d[0][0] not in hypotheses[h] and d[0][1] not in hypotheses[h])):
			return 1.
		else:
			return epsilon

	elif h[0]==1: #same double shape
		if (d[1] and d[0][0]==d[0][1] and d[0][0] in hypotheses[h]) or\
		   (not d[1] and ((d[0][0]!=d[0][1]) or d[0][0] not in hypotheses[h])):
		    return 1.
		else:
			return epsilon

	elif h[0]==2: #diff double shape
		if (d[1] and d[0] in hypotheses[h]) or\
		   (not d[1] and d[0] not in hypotheses[h]):
			return 1.
		else:
			return epsilon








