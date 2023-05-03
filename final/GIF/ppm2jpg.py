from PIL import Image
import os
import re

for filename in os.listdir("./"):
    if (re.findall(".ppm", filename)):
        im = Image.open(filename)
        im.save(re.findall("(.+).ppm", filename)[0] + ".png")
        os.remove(filename)