# Experiment 1
# Conditions: NegPos, PosOnly

# Experimental Data
e_NegPos_Correct=.77
e_PosOnly_Correct=.48

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
# # Evidence
# train_PosOnly=[]
train_PosOnly=[None]*3
train_PosOnly[0]=[(0,0),True]
train_PosOnly[1]=[(1,1),True]
train_PosOnly[2]=[(2,2),True]
#Test
test_PosOnly=[None]*2
test_PosOnly[0]=[(3,3),True]
test_PosOnly[1]=[(3,1),True]


# Experiment 2
# Single Condition, various age ranges

# Experimental Data
e_1830_Correct=.48
e_3042_Correct=.58
e_4254_Correct=.75

# Unique Condition
# Evidence
# train_Unique=[]
train_Unique=[None]*3
train_Unique[0]=[(0,0),True]
train_Unique[1]=[(1,1),True]
train_Unique[2]=[(2,2),True]
#Test
test_Unique=[None]*2
test_Unique[0]=[(3,3),True]
test_Unique[1]=[(2,1),True]

#test_Unique[0]=[(0,0),True]
#test_Unique[1]=[(2,1),True]
#test_Unique[0]=[(1,2),True]


