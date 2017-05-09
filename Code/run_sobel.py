import model_alphabeta_strongsampling as model
#import model_alphabeta as model
#import model_delta as model
#import model_onepar as model
import data_sobel as data


model.alpha=0.25
model.beta=0.25
#model.delta=0.1
model.epsilon=0.01
model.gamma=0.7

model.initialize()

# Experiment 1 
print("\nModel for Sobel Exp 1 - NegPos Condition")
p_NegPos_CorrectActive=model.p_singledata_data(data.test_NegPos[0], data.train_NegPos)
p_NegPos_WrongActive=model.p_singledata_data(data.test_NegPos[1], data.train_NegPos)
print("p Correct choice activates machine: {0}, p Wrong choice activates machine: {1}"\
		.format(p_NegPos_CorrectActive, p_NegPos_WrongActive))

print("\nModel for Sobel Exp 1 - PosOnly Condition")
p_PosOnly_CorrectActive=model.p_singledata_data(data.test_PosOnly[0], data.train_PosOnly)
p_PosOnly_WrongActive=model.p_singledata_data(data.test_PosOnly[1], data.train_PosOnly)
print("p Correct choice activates machine: {0}, p Wrong choice activates machine: {1}"\
		.format(p_PosOnly_CorrectActive, p_PosOnly_WrongActive))


print("\nModel Choice Exp 1")
print("p correct choice NegPos={0}, p correct choice PosOnly={1}"\
		.format(model.choose(p_NegPos_CorrectActive, p_NegPos_WrongActive),\
		        model.choose(p_PosOnly_CorrectActive, p_PosOnly_WrongActive)))


# Experiment 2
print("\nModel for Sobel Exp 2 - Unique Condition")
p_Unique_CorrectActive=model.p_singledata_data(data.test_Unique[0], data.train_Unique)
p_Unique_WrongActive=model.p_singledata_data(data.test_Unique[1], data.train_Unique)
print("p Correct choice activates machine: {0}, p Wrong choice activates machine: {1}"\
		.format(p_Unique_CorrectActive, p_Unique_WrongActive))


print("\nModel Choice Exp 2")
print("p correct choice Unique={0}"\
		.format(model.choose(p_Unique_CorrectActive, p_Unique_WrongActive)))
