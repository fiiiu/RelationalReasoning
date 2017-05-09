# Experiment 1
# Conditions: NegPos, PosOnly

# Experimental Data
p_NegPos=[.77, .23]
p_PosOnly=[.48, .52]

# Stimuli
# NegPos Condition
# Evidence
train_NegPos=[None]*7
train_NegPos[0]=[(0,None),False]
train_NegPos[1]=[(0,0),True]
train_NegPos[2]=[(1,None),False]
train_NegPos[3]=[(1,1),True]
train_NegPos[4]=[(2,None),False]
train_NegPos[5]=[(2,2),True]
train_NegPos[6]=[(3,None),False]
#Test
test_NegPos=[None]*2
test_NegPos[0]=[(3,3),True]
test_NegPos[1]=[(3,1),True]

# PosOnly Condition
# Evidence
train_PosOnly=[None]*3
train_PosOnly[0]=[(0,0),True]
train_PosOnly[1]=[(1,1),True]
train_PosOnly[2]=[(2,2),True]
#Test
test_PosOnly=[None]*2
test_PosOnly[0]=[(3,3),True]
test_PosOnly[1]=[(3,1),True]



