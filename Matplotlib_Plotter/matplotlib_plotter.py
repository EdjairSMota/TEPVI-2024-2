# matplotlib_plotter.py
import numpy as np
import matplotlib.pyplot as plt
d=np.loadtxt('/home/pi/A0.dat',delimiter=' ')
plt.plot(d[:,0]-d[0,0],d[:,1])
plt.xlabel('Time [s]')  # identificacao do eixo X
plt.ylabel('A0')        # identificacao do eixo Y
plt.show()              # mostra o grafico

