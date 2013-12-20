# -*- coding: utf-8 -*-
import PIL, os
from PIL import Image
from ftsrt.settings import MEDIA_ROOT
basewidth = 300


def resize(img_name):
    img_path = os.path.join(MEDIA_ROOT, img_name)
    if not os.path.isfile(img_path):
        return
    img = Image.open(img_path)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save(img_path)