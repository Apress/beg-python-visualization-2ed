from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager
W = 400
dx = 20
img = Image.new('L', (W*2+dx, W), 255)
draw = ImageDraw.Draw(img)
font_str = font_manager.findfont('Vera')
ttf = ImageFont.truetype(font_str, 28)
s = 'A long string'


draw.ellipse((0, 0, W, W), fill=128)
draw.ellipse((W+dx, 0, 2*W+dx, W), fill=128)
# draw.text((W//2, W//2), 'A long string')

(w, h) = draw.textsize(s, font = ttf)
draw.text((W//2, W//2), s, font = ttf)
draw.text((3*W//2-w//2, (W-h)//2), s, font=ttf)

img.show()
img.save('../images/figure9-2.png')