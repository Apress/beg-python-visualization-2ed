# a helper function to move subplots in the y range so they don't hide titles
def nudge_subplot(subp, deltay):
    sp_ax=subp.get_position()
    subp.set_position([sp_ax.x0, sp_ax.y0+deltay, 
        sp_ax.x1-sp_ax.x0, sp_ax.y1-sp_ax.y0])
sx=4
if sx == 1:
    from scipy.interpolate import spline
    from pylab import *

    xp = linspace(0, 1, 6)
    yp = sqrt(1-xp**2)
    xi = linspace(0, 1, 100)
    yi = interp(xi, xp, yp)
    ys = spline(xp, yp, xi)
    figure()
    hold(True)
    plot(xi, yi, '--', label='piecewise linear', lw=2)
    plot(xi, ys, '-', label='spline', lw=2)
    legend(loc='best')
    grid()
    title(r'Spline interpolation of $y=\sqrt{1-x^2}$')
    xlabel('x')
    ylabel('y')
    axis('scaled')
    axis([0, 1.2, 0, 1.2])
    savefig('../images/figure8-7', dpi=150)
    
if sx == 2:
    from pylab import *
    from scipy import signal

    N = 2**9   # we prefer powers of 2
    F = 25     # a wave at 25 Hz
    t = arange(N)/float(N)  # sampled over 1 second
    x = cos(2*pi*t*F)   # the signal
    figure()
    p = subplot(2, 1, 1)
    nudge_subplot(p, 0.04)
    plot(t, x)
    ylabel('x []')
    xlabel('t [seconds]')
    title('A cosine wave')
    grid()

    p = subplot(2, 1, 2)
    nudge_subplot(p, -0.02)
    f = t*N
    xf = fft(x)
    plot(f, abs(xf))
    title('Fourier transform of a cosine wave')
    xlabel('f [Hz]')
    ylabel('xf []')
    xlim([0, N])
    grid()
    savefig('../images/figure8-12', dpi=150)
    
if sx==3:
    N = 2**9   # we prefer powers of 2
    F = 25.5   # wave frequency
    t = arange(N)/float(N)  # sampled over 1 second
    f = t*N
    x = cos(2*pi*t*F)   # the signal
    xh = x*hamming(512) # multiply with a hamming window
    figure()
    plot(f, abs(fft(x)), 's-', label='original')
    plot(f, abs(fft(xh)), 'o-', label='with Hamming')
    xlim([0, 50])
    xticks(arange(0, 55, 5))
    legend()
    grid()
    title('Signal with Hamming window')
    xlabel('Frequency [Hz]')
    ylabel('Amplitude []')
    savefig('../images/figure8-13', dpi=150)

    
if sx ==4:
    # heart signal simulation
    N = 256     # number of samples per second
    T = 2       # number of seconds
    hr = 1.67   # 100 beats per minutes
    F1 = 0.5    # movement frequency

    t = arange(T*N)/float(N)    
    y1 = 5*sin(2*pi*t*F1)     # movement artifact

    # add heart signals
    y2 = zeros(size(y1))
    for i in range(int(T*hr)):
        y2[i*N/hr:i*N/hr+10] = signal.triang(10)
        
    # combine movement with beats
    y = y1+y2

    # create a high-pass filter
    [b, a] = signal.butter(3, 0.05, 'high')

    # filter the signal
    yn = signal.lfilter(b, a, y)

    # plot the graphs
    figure()

    p = subplot(2, 1, 1)
    nudge_subplot(p, 0.04)
    title('Heart signal with movement artifact (simulation)')
    plot(t, y, lw=2)
    xlabel('t [seconds]')
    ylabel('Amplitude []')

    p = subplot(2, 1, 2)
    nudge_subplot(p, -0.02)
    title('Filtered signal')
    plot(t, yn, lw=2)
    xlabel('t [seconds]')
    ylabel('Amplitude []')
    savefig('../images/figure8-15', dpi=150)
    
if sx==5:
    from pylab import *
    from scipy import signal

    cycles = 10
    t = arange(0, 2*pi*cycles, pi/10)

    waveforms = ['sawtooth', 'square']

    figure()
    for i, waveform in enumerate(waveforms):
        subplot(2, 2, i+1)
        exec('y = signal.' + waveform + '(t)')
        plot(t, y)
        title(waveform)
        axis([0, 2*pi*cycles, -1.1, 1.1])
            
        savefig('../images/figure8-11', dpi=150)

    
if sx==6:

    N = 256     # number of points for freqz
    Wc = 0.2    # 3dB point
    Order = 3   # filter order

    # design a Butterworth filter
    [b, a] = signal.butter(Order, Wc)

    # calculate the frequency repsonse
    [w, h] = signal.freqz(b, a, N)

    # plot the results
    figure()

    p = subplot(2, 1, 1)
    nudge_subplot(p, 0.04)
    plot(arange(N)/float(N), 20*log10(abs(h)), lw=2)
    title('Frequency response')
    xlabel('Frequency (normalized)')
    ylabel('dB')
    ylim(ylim()[0], ylim()[1]+5)
    grid()

    p = subplot(2, 1, 2)
    nudge_subplot(p, -0.02)
    plot(arange(N)/float(N), 20*log10(abs(h)), lw=2)
    title('Frequency response (3dB point)')
    xlabel('Frequency (normalized)')
    ylabel('dB')
    text(Wc+.02, -3, '3dB point', va='bottom')
    ylim([-3, 0.1])
    grid()
        
    savefig('../images/18432f08-14', dpi=150)
        
if sx == 7:
    figure()
    N = 7
    x = linspace(-1, 1, N)
    y = sqrt(1-x**2)
    dx = x[1] - x[0]
    for i in range(len(x)-1):
        rect = Rectangle((x[i], 0), dx, 0.5*(y[i]+y[i+1]), fc='lightblue')
        gca().add_patch(rect)
    title('Approximating the area of half a circle')
    axis('equal')

    for N in [ 5, 10, 20, 100]:
        x = linspace(-1, 1, N)
        dx = x[1] - x[0]
        y = sqrt(1-x**2)
        est_pi = dx*sum(y[0:-1]+y[1:])
        print("N=%d, estimated pi is %f" % (N, est_pi))

 
if sx==8:
    figure()
    hold(True)
    x = linspace(0, 1, 500)
    y = sqrt(1-x**2) 
    xp = linspace(0, 1, 6)
    yp = sqrt(1-xp**2)
    xi = arange(0.1, 1.0, 0.2)
    yi = interp(xi, xp, yp)
    plot(x, y, 'b', label='ideal') 
    plot(xp, yp, 'or', label='interpolation points')
    plot(xp, yp, '--r', label='piecewise linear function')
    plot(xi, yi, 'sg', label='interpolated values')
    legend(loc='best')
    grid()
    axis('scaled')
    axis([0, 1.1, 0, 1.1])
    title('Piecewise linear interpolation')
    savefig('../images/figure8-3', dpi=150)

if sx==9:
    values = [0, pi/6, pi/4, pi/3, pi/2]
    sines = sqrt(arange(5))/2
    p = polyfit(values, sines, len(values)-1)
    figure()
    x = linspace(0, pi/2, 100)
    plot(x, polyval(p, x)-sin(x), label='error', lw=3)
    grid()
    ylabel('polyval(p, x)-sin(x)')
    xlabel('x')
    title('Error approximating sin(x) using polyfit()')
    xlim(0, pi/2)
    savefig('../images/figure8-6', dpi=150)
    