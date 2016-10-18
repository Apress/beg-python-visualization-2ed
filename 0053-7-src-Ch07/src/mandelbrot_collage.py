from PIL import Image, ImageOps

# creates an image of the Mandelbrot set
res = 400
iterations = [4, 8, 16, 128]

for iters in iterations:
    img = Image.new("L", (res, res), 255)
    for im in range(res):
        for re in range(res):
            z = 0
            # a scaling to show the "interesting" part of the Mandelbrot fractal
            c = (re*2/res-1.5)+1j*(im*2/res-1)
            for k in range(iters):
                z = z**2+c
                if abs(z)>2:
                    img.putpixel((re, im), 255-k*255/iters)
                    break
                    
    # create a uniform distribution of gray levels
    img = ImageOps.equalize(img)

    # save to file
    img.save('../images/mandelbrot_%d_%d.png' % (iters, res), dpi=(150,150))
    
collage = Image.new("L", (res*2, res*2))
for x in range(2):
    for y in range(2):
        im = Image.open('../images/mandelbrot_%d_%d.png' % (iterations[x*2+y], res))
        collage.paste(im, (res*y, res*x))
collage.save('../images/figure7-2.png', dpi=(150,150))
