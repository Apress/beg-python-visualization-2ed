from pylab import *
from mpl_toolkits.mplot3d import Axes3D

x = linspace(-1, 1, 100)
y = linspace(-1, 1, 100)
u, v = meshgrid(x, y)

fig = figure()
z = 1-u**2-v**2
z[nonzero(z<0)] = 0
ax = fig.gca(projection='3d')
ax.plot_surface(u, v, z)
title('A sphere on a plane')
savefig('../images/figure6-21.png', dpi=150, transparent=True)

fig = figure()
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
title('3-D contour plot')
ax1.contour(u, v, z)

ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.contourf(u, v, z)
title('Filled 3-D contour plot')
savefig('../images/figure6-22.png', dpi=150, transparent=True)
