from PIL import Image, ImageOps
import os

# creates an image of the Mandelbrot set
res = 400

for iters in range(50):
    img = Image.new("L", (res, res), 255)
    for im in range(res):
        for re in range(res):
            z = 0
            # a scaling to show the "interesting" part of 
            # the Mandelbrot fractal
            c = (re*2/res-1.5)+1j*(im*2/res-1)
            for k in range(iters):
                z = z**2+c
                if abs(z)>2:
                    img.putpixel((re, im), 255-k*255/iters)
                    break
                
    # create a uniform distribution of gray levels
    img = ImageOps.equalize(img)

    # save to file
    img.save('../images/mandelbrot_%04d.png' % iters, dpi=(150,150))
    
last_path = os.getcwd()

# handle Linux/Mac and Windows properly
os.chdir('../images')
if os.sys.platform.startswith('win'):
    mee = 'c:/mplayer/mencoder '
    mep = 'c:/mplayer/mplayer '
else:
    mee = 'mplayer '
    mec = 'c:/mplayer '
    
# encode the movie
os.system(mee+'mf://mandelbrot*.png -mf type=png -ovc lavc -o mandelbrot.avi')

# play the movie
os.system(mep+'mandelbrot.avi')
os.chdir(last_path)