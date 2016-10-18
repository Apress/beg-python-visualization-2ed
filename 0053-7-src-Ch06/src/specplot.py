from pylab import *

Fs = 256
times = [3, 7, 5]
frequencies = [ 100, 20, 80]

y = array([])
for t, f in zip(times, frequencies):
    x = cos(2*pi*arange(t*Fs)/Fs*f)
    y = append(y, x)

specgram(y, 256, Fs)
xlabel('Time [sec]')
ylabel('Frequency [Hz]')
axis([0, 14.5, 0, 128])

savefig('../images/figure6-15.png',dpi=150)