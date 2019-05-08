
import numpy as np
import matplotlib.pyplot as plt
import random
import math


def exibir_funcao(elementox,elementoy):
    x = np.arange(0.0, 5.0, 0.0090)
    #sin(X^2)/(3-cos(e)-x)
    y = []
    for absissa in x:
        y.append(math.sin(absissa*absissa)/(3-math.cos(math.e)-absissa))
    
    plt.plot((3.9094984426873,3.9094984426873),(0,elementoy),'k--')

    plt.plot(x,y)
    plt.plot(elementox,elementoy,'o') 
 
    plt.plot(3.9, +np.inf, linewidth=3, color='red') 

    plt.show()

    
    # t = np.arange(0.0, 5.0, 0.01)
    # s = np.sin(math.pow(t,2))/(3-math.cos(math.e)-t)
    # line, = plt.plot(t, s, lw=2)

    # plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
    #             arrowprops=dict(facecolor='black', shrink=0.05),
    #             )

    # plt.ylim(-2,2)
    # plt.show()
