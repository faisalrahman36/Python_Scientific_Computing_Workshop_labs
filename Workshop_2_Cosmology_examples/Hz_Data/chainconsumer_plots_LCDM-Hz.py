import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm as cm


szdat=np.genfromtxt("E:\\NumericalMethod_Statistics_Cosmology_Workshop\Workshop_labs_2\Hz_Data\Hz_chisq_likelihood_reduced-Chisq_omegaLambda_LCDM_H0_parallel_numba.csv",delimiter=",")

likelihood=szdat[:,1]
#olv=szdat[:,3]
#H0v=szdat[:,4]
#chi2=szdat[:,0]

from chainconsumer import ChainConsumer

c = ChainConsumer()

c.add_chain([szdat[:,3],szdat[:,4]], weights=likelihood, grid=True, parameters=[r"$\Omega_\Lambda$",r"H0"]).configure(statistics='mean')

#c.configure(smooth=3)
#c.configure(summary=False)
#bestfit=[0.7,70]
#c.plotter.plot(truth=bestfit)
#c.plotter.plot_distributions()
c.plotter.plot()

#c.plotter.plot_distributions()
#c.plotter.plot_summary()
#print(c.analysis.get_summary())
#print(c.analysis.get_correlations())
#print(c.analysis.get_covariance())


plt.show()