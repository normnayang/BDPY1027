from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
plt.plot(np.random.randn(20).cumsum(), 'r--')
_ = ax1.hist(np.random.randn(200), bins=20, color='c', alpha=1)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
plt.show()

fig, axes = plt.subplots(2, 2)
axes[0, 0].hist(np.random.randn(50), bins=20, color='c', alpha=1)
axes[1, 1].scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
plt.show()
