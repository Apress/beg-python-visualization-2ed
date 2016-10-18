from pylab import *

x = arange(-5, 5, 0.1)
y = arange(-5, 5, 0.1)
u, v = meshgrid(x, y)

z = 2*u**2+v**2-u*v+10*u
contour(x, y, z, 10)
title('A contour map')
show()

savefig('../images/figure6-17.png',dpi=150)