import numpy as np
import runner_onepar as run
import data
import scipy.optimize as optimize


def distance(alpha):
	p_model=run.run(alpha)
	return run.compare(p_model)


print optimize.minimize_scalar(distance, bounds=[0,.5], method='bounded')


