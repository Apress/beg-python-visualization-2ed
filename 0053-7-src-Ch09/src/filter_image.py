# filter images
from PIL import Image, ImageChops, ImageFilter

img = Image.open('../images/nightsky.png')
inv_img = ImageChops.invert(img)
filt_img = inv_img.filter(ImageFilter.MinFilter(15))
# filt_img = inv_img.filter(ImageFilter.Kernel(15, ImageFilter.FIND_EDGES))

w, h = img.size
delta = 1
col_img = Image.new('RGB', (w*2+delta, h))
col_img.paste(inv_img, (0, 0))
col_img.paste(filt_img, (w+delta, 0))
col_img.show()
col_img.save('../images/figure9-10.png', dpi=(150, 150))