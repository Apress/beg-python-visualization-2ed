from PIL import Image

# import the fractal function, from fractal.py file
from fractal import fractal

fsize = 200     # small fractal image width and height
nx = 3          # number of images, width
ny = 3          # number of images, height

collage = Image.new("RGB", (fsize*nx, fsize*ny))
for i in range(ny):
    for j in range(nx):
        im = fractal(0.000001, fsize, i*nx+j+1)
        print("Processing image %d of %d" % (i*nx+j+1, nx*ny))
        collage.paste(im, (fsize*j, fsize*i))
collage.save('../images/collage.png')
