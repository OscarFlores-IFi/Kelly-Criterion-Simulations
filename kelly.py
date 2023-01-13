# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 18:08:01 2022

@author: 52331
"""

import numpy as np
import matplotlib.pyplot as plt
import cycler
import matplotlib as mpl

n_time = 100
n_individuals = 100

t = np.random.normal(0.01,0.015,n_time) # market returns at time t

kellyfractions = np.linspace(0.05,70,n_individuals) # portfolio exposition
temp_t = np.ones((t.size,kellyfractions.size)) 

loss_gain = t*(temp_t*kellyfractions).T 

# exp_loss_gain = np.exp(loss_gain)
# cum_loss_gain = np.cumprod(exp_loss_gain,axis = 1) # used for log returns. 

simple_loss_gain = loss_gain + 1 
simple_loss_gain[loss_gain < -1] = 0
cum_loss_gain = np.cumprod(simple_loss_gain,axis = 1)

# plt.hist(t, bins=10)
# plt.show()


color = plt.cm.viridis(np.linspace(0, 1,n_individuals))
mpl.rcParams['axes.prop_cycle'] = cycler.cycler('color', color)

fig, ax = plt.subplots()
ax.plot(cum_loss_gain.T)

# cb = plt.colorbar(orientation='horizontal', shrink=.75) 
# cb.set_label('iteration count') 
plt.show()

# plt.imshow(cum_loss_gain)

# plt.plot(loss_gain.T)
# plt.show()