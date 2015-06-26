import model_alphabeta as model
import data

model.initialize()
model.change_parameters(0.28711,1.4863e-08,0.9,0.01)

print len(model.hypotheses)

upsamesame=model.p_data_data([data.tests], data.data_same)
updiffsame=model.p_data_data([data.testd], data.data_same)


normsamesame=model.p_data_data([data.testsnorm], data.data_same)
normdiffsame=model.p_data_data([data.testdnorm], data.data_same)

psamesame=upsamesame/(upsamesame+normsamesame)
pdiffsame=updiffsame/(updiffsame+normdiffsame)


upsamediff=model.p_data_data([data.tests], data.data_diff)
updiffdiff=model.p_data_data([data.testd], data.data_diff)

normsamediff=model.p_data_data([data.testsnorm], data.data_diff)
normdiffdiff=model.p_data_data([data.testdnorm], data.data_diff)

psamediff=upsamediff/(upsamediff+normsamediff)
pdiffdiff=updiffdiff/(updiffdiff+normdiffdiff)


print "SAME:\n p same={0}, p diff={1}, ps/pd={2}".format(psamesame,pdiffsame,psamesame/pdiffsame)
print "DIFF:\n p same={0}, p diff={1}, pd/ps={2}".format(psamediff,pdiffdiff,pdiffdiff/psamediff)


print "\np correct choice SAME={0}, p correct choice DIFF={1}"\
      .format(model.choose(psamesame,pdiffsame), model.choose(pdiffdiff,psamediff))

# print "SAME\n p same/p diff={0}".format(psamesame/pdiffsame)
# print "DIFF\n p diff/p dsame={0}".format(pdiffdiff/psamediff)

#now the magic

print "\nEXPERIMENT 2:\n"

psameplussame=model.p_data_data_binormalized([data.tests],data.data_same_plus)
pdiffplussame=model.p_data_data_binormalized([data.testd],data.data_same_plus)

psameplusdiff=model.p_data_data_binormalized([data.tests],data.data_diff_plus)
pdiffplusdiff=model.p_data_data_binormalized([data.testd],data.data_diff_plus)

print "SAME:\n p same={0}, p diff={1}".format(psameplussame,pdiffplussame)
print "DIFF:\n p same={0}, p diff={1}".format(psameplusdiff,pdiffplusdiff)


print "\np correct choice SAME={0}, p correct choice DIFF={1}"\
      .format(model.choose(psameplussame,pdiffplussame), model.choose(pdiffplusdiff,psameplusdiff))





