

import model_delta as m
import data

#init
#m.gamma=1.
m.initialize()


#prelim checks
m.p_hypothesis_theory((0,0,0),0)
m.h_space
len(m.h_space)

#normalization checks
probs=[0]*len(m.t_space)
for t in m.t_space:
	probs[t]=[m.p_hypothesis_theory(h,t) for h in m.h_space]
	print sum(probs[t])



#print m.gamma

