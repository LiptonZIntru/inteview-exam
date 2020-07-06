import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.linspace(0, 2 * np.pi, 3), [np.sin(i) for i in np.linspace(0, 2 * np.pi, 3)])
plt.show()
