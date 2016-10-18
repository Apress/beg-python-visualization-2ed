# a scratchpad script for the examples in Chapter 6
from pylab import *

# a helper function to move subplots in the y range so they don't hide titles
def nudge_subplot(subp, deltay):
    sp_ax = subp.get_position()
    sp.set_position([sp_ax.x0, sp_ax.y0+deltay, 
        sp_ax.x1-sp_ax.x0, sp_ax.y1-sp_ax.y0])


figure()
example = 14
if example == 2:
    # values to plot
    t = arange(10, 15)
    y = array([1,  2, -1,  1, -2])

    plot_cmds = [
        "plot(y)",
        "plot(t, y)",
        "plot(t, y, 'o')",
        "plot(t, y, 'D-.')"
        ]

    for i, plot_cmd in enumerate(plot_cmds):
        sp = subplot(2, 2, i+1)
        exec(plot_cmd)
        title(plot_cmd, fontsize='large')
        nudge_subplot(sp, 0.02-i/2*0.04)

elif example == 3:
    I = arange(6)
    plot(I, sin(I), 'o', I, cos(I), '-', lw=3, ms=8)
    title("plot(I, sin(I), 'o', I, cos(I), '-', lw=3, ms=8)")
    
elif example == 4:
    I = arange(0, 2*pi, 0.01)
    plot_cmds = [
        [ 'plot(sin(I)*1.2, cos(I)*1.2)', 'auto' ],
        [ 'plot(sin(I)*1.2, cos(I)*1.2)', 'equal' ],
        [ 'plot(sin(I)*1.2, cos(I)*1.2)', 'tight' ],
        [ 'plot(sin(I)*1.2, cos(I)*1.2)', 'scaled' ]
        ]

    for i, plot_cmd in enumerate(plot_cmds):
        sp = subplot(2, 2, i+1)
        exec(plot_cmd[0])
        axis(plot_cmd[1])
        title(plot_cmd[1], fontsize='large')
        nudge_subplot(sp, 0.02-i/2*0.04)
    
if example == 5:
    R = 1.2
    I = arange(0, 4*pi, 0.01)

    for i in range(2):
        subplot(2, 2, i+1)
        plot(sin(I)*R, cos(0.5*I)*R)
        axhline(color='gray')
        axvline(color='gray')
        grid()
  
    xticks([-1, 0, 1], ('Negative', 'Neutral', 'Positive'))
    yticks(arange(-1.5, 2.0, 1))

if example == 6:
    subplot(2, 1, 1)
    title('Upper half')
    subplot(2, 2, 3)
    title('Lower half, left side')
    subplot(2, 2, 4)
    title('Lower half, right side')
    
if example == 7:
    I = arange(0, 2*pi, 0.1)
    plot(I, sin(I), '+-', label='sin(I)')
    plot(I, cos(I), 'o-', label='cos(I)')
    legend()
    
if example == 8:
    I = arange(0, 2*pi+0.1, 0.1)
    plot(I, sin(I), label='sin(I)')
    title('Function f(x)=sin(x)')
    xlabel('x [rad]', va='bottom')
    ylabel('sin(x)')
    text(pi/2, 1, 'Max value', ha='center', va='bottom')
    text(3*pi/2, -1, 'Min value', ha='center', va='top')
    xticks(linspace(pi/2, 2*pi, 4), (r'$\frac{\pi}{2}$', r'$\pi$', \
        r'$\frac{3\pi}{2}$', r'$2 \pi$'), fontsize=20)
    xlim([0, 2*pi])
    ylim([-1.2, 1.2])
    grid()
    
if example == 12:
    from pylab import *
    I = 2*logspace(1,5,5)
    semilogx(I, [20, 19, 8, 2, 2], 's-', lw=2)
    grid()
    title('Logarithmic plot, semilogx()')
    xlabel('Frequency [Hz]')
    ylabel('Amplitude [dB]')
    ylim([1, 21])
    
if example == 14:
    theta = arange(0, 2*pi, 0.01)
    polar(theta, cos(theta), theta, -cos(theta))
    rgrids([0.5, 1.0], ['Half', 'Full'])
    theta_labels = ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$']
    thetagrids(arange(0, 360, 90), theta_labels, fontsize=20)
    title(r'A polar plot of $\pm cos(\theta)$', va='bottom')
    
if example == 14:
    from pylab import *
    N = [4, 8, 16, 64]
    for i, n in enumerate(N):
        subplot(2,2,i+1)
        stem(arange(n), hamming(n))
        xticks(arange(0,n+1,n/4))
        yticks([0, 0.5, 1])
        xlim(-0.5, n+0.5)
        title('N=%d' % n)
        
if example == 19:
    x = arange(10)
    y = x**2
    plot(x, y)
    ars = [(x0, y0, dx, dy) for (x0, y0, dx, dy) in zip(x, y, diff(x), diff(y))]
    cur_axes=gca()
    for x0, y0, dx, dy in ars:
        cur_axes.add_patch(Arrow(x0, y0, dx, dy))
    title('Arrows!')


savefig('../images/figure6-%d.png' % example, dpi=150)
show()