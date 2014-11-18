
t1s=[[0,0],True]
t2s=[[1,2],False]
t3s=[[3,3],True]
t4s=[[4,5],False]

t1d=[[1,2],True]
t2d=[[0,0],False]
t3d=[[4,5],True]
t4d=[[3,3],False]

tests=[[6,6],True]
testd=[[7,8],True]

testsnorm=[[6,6],False]
testdnorm=[[7,8],False]

data_same=[t1s,t2s,t3s,t4s]
data_diff=[t1d,t2d,t3d,t4d]
test=[tests,testd]


#smallspace
tests=[[3,3],True]
testd=[[4,5],True]

testsnorm=[[3,3],False]
testdnorm=[[4,5],False]

data_same=[t1s,t2s]
data_diff=[t1d,t2d]
test=[tests,testd]

#magic EXP2
plus0=[[0],False]
plus1=[[1],False]
plus2=[[2],False]
plus3=[[3],False]

data_same_plus=[plus0,plus1,t1s,plus2,plus3,t2s]

data_diff_plus=[plus0,plus1,t1d,plus2,plus3,t2d]


