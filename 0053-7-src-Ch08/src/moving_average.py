from pylab import *
from scipy import signal

figure()
N = 512
t = linspace(0, 10, N)
x = 1-exp(-t) +randn(N)/10

W = 32  # num points in moving average
xf = zeros(len(x)-W+1)
for i in range(len(x)-W+1):
    xf[i] = mean(x[i:i+W])

plot(t, x)
hold(True)
# plot(t[W-1:], xf, lw=3)
title('Moving average')
xlabel('t [seconds]')
ylabel('x []')

xf = signal.lfilter(ones(W)/ W, 1, x)
plot(t, xf, lw=3)
legend(['signal with noise', 'filtered signal'])
savefig('../images/figure8-16', dpi=150)
