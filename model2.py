import scipy.misc
import itertools
import numpy as np

gain=1.8
n_shapes=6
shapes=range(n_shapes)
t_space=[0,1]
n_comb2=int(scipy.misc.comb(n_shapes,2))
#h_space=range(2**n_shapes+n_shapes+n_comb2)
h_space=range(2**n_shapes+2)
individual_bias=0.99	#0.999#0.999#0.99997
epsilon=0.01#1e-1
simplehypotheses=[]
shape_pairs=[pair for pair in itertools.combinations(shapes,2)]


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
def p_data_data(d_new,d_old):#inefficient, could take p_hs out of the loop..
	p=0
	for t in t_space:
		for h in h_space:
			p+=p_data_hypothesis(d_new,h)*p_data_hypothesis(d_old,h)/p_data(d_old)*\
				p_hypothesis_theory(h,t)*p_theory(t)
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
		for h in h_space:
			p+=p_data_hypothesis(d,h)*p_hypothesis_theory(h,t)
		p*=p_theory(t)
	return p 

def choose(p1,p2):
	return 1./(1+np.exp(-gain*(p1-p2)))

def p_theory_data(t,d):
	p=0
	for h in h_space:
		p+=p_data_hypothesis(d,h)*p_hypothesis_theory(h,t)
	p/=p_data(d)
	p*=p_theory(t)
	return p


###BLOCKS

def p_theory(t):
	return individual_bias if t==0 else 1-individual_bias

def p_hypothesis_theory(h,t):
	if t==0:
		if h<2**n_shapes:
			return 1./(2**n_shapes) #looks like I need norm here..
		else:
			return 0

	elif t==1:
		if h>=2**n_shapes:
			return 1./2#(n_shapes+n_comb2) #...and here
		else:
			return 0

def p_data_hypothesis(dlist,h):
	p=1
	for d in dlist:
		p*=p_singledata_hypothesis(d,h)
	return p


def produce_simplehypotheses():
	if simplehypotheses==[]:
		count=0
		for i in range(n_shapes+1):
			for u in itertools.combinations(shapes, i):
				simplehypotheses.append([])
				simplehypotheses[count]=[0]*n_shapes
				for j in u:
					simplehypotheses[count][j]=1
				count+=1
	return simplehypotheses


def p_singledata_hypothesis(d,h):

	#hypotheses=
	produce_simplehypotheses()
	#print 'yoyo', simplehypotheses

	if h < len(simplehypotheses): #produce_simplesimplehypotheses
		if (len(d[0])==1 and simplehypotheses[h][d[0][0]]==1 and d[1]) or\
		   (len(d[0])==1 and simplehypotheses[h][d[0][0]]==0 and not d[1]) or\
		   (len(d[0])==2 and (simplehypotheses[h][d[0][0]]==1 or simplehypotheses[h][d[0][1]]==1)\
		   	and d[1]) or\
		   (len(d[0])==2 and (simplehypotheses[h][d[0][0]]==0 and simplehypotheses[h][d[0][1]]==0)\
		   	and not d[1]):
			return 1.#/len(simplehypotheses)
		else:
			return epsilon
	

	elif len(simplehypotheses) == h: #same
		if d[1]:
			if (len(d[0])==2 and d[0][0]==d[0][1]):
				return 1.
			else:
				return epsilon
		else:
			if (len(d[0])==2 and d[0][0]==d[0][1]):
				return epsilon
			else:
				return 1.
	
	elif len(simplehypotheses)+1 == h: #different
		if d[1]:
			if (len(d[0])==2 and d[0][0]!=d[0][1]):
				return 1.
			else:
				return epsilon
		else:
			if (len(d[0])==2 and d[0][0]!=d[0][1]):
				return epsilon
			else:
				return 1.

	else:
		print 'why here?'

