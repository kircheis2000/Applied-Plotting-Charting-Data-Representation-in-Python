
# coding: utf-8

# # Practice Assignment: Understanding Distributions Through Sampling
# 
# ** *This assignment is optional, and I encourage you to share your solutions with me and your peers in the discussion forums!* **
# 
# 
# To complete this assignment, create a code cell that:
# * Creates a number of subplots using the `pyplot subplots` or `matplotlib gridspec` functionality.
# * Creates an animation, pulling between 100 and 1000 samples from each of the random variables (`x1`, `x2`, `x3`, `x4`) for each plot and plotting this as we did in the lecture on animation.
# * **Bonus:** Go above and beyond and "wow" your classmates (and me!) by looking into matplotlib widgets and adding a widget which allows for parameterization of the distributions behind the sampling animations.
# 
# 
# Tips:
# * Before you start, think about the different ways you can create this visualization to be as interesting and effective as possible.
# * Take a look at the histograms below to get an idea of what the random variables look like, as well as their positioning with respect to one another. This is just a guide, so be creative in how you lay things out!
# * Try to keep the length of your animation reasonable (roughly between 10 and 30 seconds).

# In[140]:

import matplotlib.pyplot as plt
import numpy as np

get_ipython().magic('matplotlib notebook')

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)

# plot the histograms
plt.figure(figsize=(9,3))
plt.hist(x1, normed=True, bins=20, alpha=0.5)
plt.hist(x2, normed=True, bins=20, alpha=0.5)
plt.hist(x3, normed=True, bins=20, alpha=0.5)
plt.hist(x4, normed=True, bins=20, alpha=0.5);
plt.axis([-7,21,0,0.6])

plt.text(x1.mean()-1.5, 0.5, 'x1\nNormal')
plt.text(x2.mean()-1.5, 0.5, 'x2\nGamma')
plt.text(x3.mean()-1.5, 0.5, 'x3\nExponential')
plt.text(x4.mean()-1.5, 0.5, 'x4\nUniform')


# In[141]:

import matplotlib.animation as animation
# random seed:random.randint(100,1000)
titles = ['Normal','Gamma', 'Exponential','Uniform']
anno = [-1, 8.5, 13.5, 17.5]
fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2, 2, sharex=False, sharey=True)
ax = [ax1,ax2,ax3,ax4]
x = [x1,x2,x3,x4]
axis1 = [-7.5,2.5,0,0.6]
axis2 = [-1,15,0,0.6]
axis3 = [6,18,0,0.6]
axis4 = [12,22,0,0.6]
axis = [axis1, axis2, axis3, axis4]

bin1 = np.arange(-7.5,2.5,0.2)
bin2 = np.arange(0,12,0.2)
bin3 = np.arange(6,18,0.2)
bin4 = np.arange(14,20,0.2)
bins = [bin1, bin2, bin3, bin4]

#n = np.random.randint(100,1000)
n = 10000
for i in range(4):
    ax[i].hist(x[i][:n],normed=True, bins=bins[i], alpha=0.5)
    ax[i].axis(axis[i])
    ax[i].set_title(titles[i], fontsize= 15)
    ax[i].annotate('n = {}'.format(n), [anno[i],0.5])
    ax[i].set_xlabel('Value', fontsize = 8)
    ax[i].set_ylabel('Normal Frequency', fontsize = 8)
    
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5,wspace=0.35)


# In[142]:

n = np.random.randint(100,1000)
fig2, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2, 2, sharex=False, sharey=True)
ax = [ax1,ax2,ax3,ax4]
def update(curr):
    if curr == n:
        a.event_source.stop()
    for i in range(len(ax)):
        ax[i].cla()
        ax[i].hist(x[i][:curr],normed=True, bins=bins[i], alpha=0.5)
        ax[i].axis(axis[i])
        ax[i].set_title(titles[i], fontsize= 15)
        ax[i].annotate('n = {}'.format(curr), [anno[i],0.5])
        ax[i].set_xlabel('Value', fontsize = 8)
        ax[i].set_ylabel('Normal Frequency', fontsize = 8)
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5,wspace=0.35)
    #plt.tight_layout()

a = animation.FuncAnimation(fig2, update, interval = 10)
n

