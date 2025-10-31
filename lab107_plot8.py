from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm

mu = 80
sigma = 8
x = mu + sigma * np.random.randn(1000000)
num_bins = 50
n, bins, patches = plt.hist(x, num_bins, density=Tsrue, facecolor='g', alpha=0.5)

y = norm.pdf(bins, mu, sigma)
plt.plot(bins, y, 'r*-')
plt.show()
