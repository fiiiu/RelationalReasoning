import model_alphabeta as model
#import model_alphabeta_strongsampling as model
#import model_delta as model
#import model_onepar as model
import data


model.alpha=0.1
model.beta=0.1
#model.delta=0.1
model.epsilon=0.05
model.gamma=0.5

model.initialize()

upsamesame=model.p_singledata_data(data.tests, data.data_same)
updiffsame=model.p_singledata_data(data.testd, data.data_same)


normsamesame=model.p_singledata_data(data.testsnorm, data.data_same)
normdiffsame=model.p_singledata_data(data.testdnorm, data.data_same)

psamesame=upsamesame/(upsamesame+normsamesame)
pdiffsame=updiffsame/(updiffsame+normdiffsame)


upsamediff=model.p_singledata_data(data.tests, data.data_diff)
updiffdiff=model.p_singledata_data(data.testd, data.data_diff)

normsamediff=model.p_singledata_data(data.testsnorm, data.data_diff)
normdiffdiff=model.p_singledata_data(data.testdnorm, data.data_diff)

psamediff=upsamediff/(upsamediff+normsamediff)
pdiffdiff=updiffdiff/(updiffdiff+normdiffdiff)


#Detailed print
#print "SAME:\n p same={0}, p diff={1}, ps/pd={2}".format(psamesame,pdiffsame,psamesame/pdiffsame)
#print "DIFF:\n p same={0}, p diff={1}, pd/ps={2}".format(psamediff,pdiffdiff,pdiffdiff/psamediff)

print "\nEXP 1"

print "\nMODEL: p correct choice SAME={0}, p correct choice DIFF={1}"\
      .format(model.choose(psamesame,pdiffsame), model.choose(pdiffdiff,psamediff))

print "EXP: p correct choice SAME={0}, p correct choice DIFF={1}"\
	  .format(data.pe_1s, data.pe_1d)

#now the magic

psameplussame=model.p_singledata_data_binormalized(data.tests,data.data_same_plus)
pdiffplussame=model.p_singledata_data_binormalized(data.testd,data.data_same_plus)

psameplusdiff=model.p_singledata_data_binormalized(data.tests,data.data_diff_plus)
pdiffplusdiff=model.p_singledata_data_binormalized(data.testd,data.data_diff_plus)

#Detailed print
#print "SAME:\n p same={0}, p diff={1}".format(psameplussame,pdiffplussame)
#print "DIFF:\n p same={0}, p diff={1}".format(psameplusdiff,pdiffplusdiff)

print "\nEXP 2"

print "\nMODEL: p correct choice SAME={0}, p correct choice DIFF={1}"\
      .format(model.choose(psameplussame,pdiffplussame), model.choose(pdiffplusdiff,psameplusdiff))

print "EXP: p correct choice SAME={0}, p correct choice DIFF={1}"\
	  .format(data.pe_2s, data.pe_2d)


print "\n"


