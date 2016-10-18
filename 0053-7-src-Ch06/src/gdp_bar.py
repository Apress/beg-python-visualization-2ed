# a script to plot GDP bar chart
from pylab import *
from read_world_data import read_world_data

# initialize variables, N is the number of countries
N = 5

gdp, labels = read_world_data(N)

# plot the bar chart
bar(arange(N), gdp, align='center')

# annotate with text
xticks(arange(N), labels, rotation=-10)
for i, val in enumerate(gdp):
    text(i, val/2, str(val), va='center', ha='center', color='yellow')
ylabel('$ (Billions)')
title('GDP rank, data from CIA World Factbook')


savefig('../images/figure6-9.png', dpi=150)