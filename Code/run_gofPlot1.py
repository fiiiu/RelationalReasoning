
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


alphas,distances=np.load('/Users/alejo/Projects/RelationalReasoning/Code/distances101.npy')


plt.plot(alphas, 1-distances)
plt.xlabel(r'$\alpha = \beta$')
plt.ylabel('Goodness of Fit')
plt.show()
