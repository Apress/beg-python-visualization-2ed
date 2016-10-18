# a script to plot GDP pie chart
from pylab import *
from read_world_data import read_world_data

# initialize variables, N is the number of countries
N = 10

gdp, tags = read_world_data(N)

# plot the bar chart
pie(gdp, labels=tags)
axis('equal')
title('GDP rank, data from CIA World Factbook')


savefig('../images/figure6-11.png', dpi=150)
show()