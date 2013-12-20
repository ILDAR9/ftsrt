import os
from PIL import Image

new_width = 75
out = 'min' # folder for scaled images

if not os.path.isdir(out):
    os.mkdir(out)

for itm in os.listdir('./'):
    ext = itm.split('.')[-1]
    if os.path.isfile(itm) and ext in ['jpg', 'gif', 'png']:
        img = Image.open(itm)
    width, height = img.size
    new_height = 100#height * new_width / width
    if img.mode != "RGB":
        img = img.convert("RGB")
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save(os.path.join(out, itm))