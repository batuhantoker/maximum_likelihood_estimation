#Import an library for a large collection of high-level mathematical functions
import numpy as np
from matplotlib import pyplot as plt

def likelihood(theta):
    return np.power(theta,alpha_h) * np.power((1-theta),alpha_t)

def plotLikelihood(theta):
    x = theta
    #alpha_h=alphah
    #alpha_t=alphat
    N=alpha_h+alpha_t
    y = np.array(likelihood(x))
    mle=np.argmax((np.array(likelihood(x))))
    plt.title("Likelihood for N={}".format(N)) 
    plt.xlabel(r'$\hat{\theta}$') 
    plt.ylabel("Likelihood") 
    plt.plot(x,y) 
    plt.plot([x[mle] ,x[mle]], [0, y[mle]])
    plt.savefig("figure_1.eps", format="eps", dpi=1000)
    plt.show()

theta_hat=np.array(np.arange(0,1.01,0.01),dtype=float)

alpha_h=6
alpha_t=4
plotLikelihood(theta_hat)
alpha_h=3
alpha_t=2
plotLikelihood(theta_hat)
alpha_h=60
alpha_t=40
plotLikelihood(theta_hat)
alpha_h=5
alpha_t=5
plotLikelihood(theta_hat)
