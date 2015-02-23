

truepsamesameE1=0.46428571
truepdiffdiffE1=0.42857143

truepsamesameE2=0.78571429
truepdiffdiffE2=0.5



t1s=[(0,0),True]
t2s=[(1,2),False]

t1d=[(1,2),True]
t2d=[(0,0),False]

#large world
#t3s=[(3,3),True]
#t4s=[(4,5),False]
#t3d=[(4,5),True]
#t4d=[(3,3),False]

# tests=[(6,6),True]
# testd=[(7,8),True]

# testsnorm=[(6,6),False]
# testdnorm=[(7,8),False]

# data_same=[t1s,t2s,t3s,t4s]
# data_diff=[t1d,t2d,t3d,t4d]
# test=[tests,testd]


#small world
tests=[(3,3),True]
testd=[(4,5),True]

testsnorm=[(3,3),False]
testdnorm=[(4,5),False]

data_same=[t1s,t2s]
data_diff=[t1d,t2d]
test=[tests,testd]

#magic EXP2
plus0=[(0,None),False]
plus1=[(1,None),False]
plus2=[(2,None),False]
plus3=[(3,None),False]

data_same_plus=[plus0,plus1,t1s,plus2,plus3,t2s]

data_diff_plus=[plus0,plus1,t1d,plus2,plus3,t2d]


