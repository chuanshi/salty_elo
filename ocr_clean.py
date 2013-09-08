import Image



filename = "imgtemp/sinestro_vs_hwa_jai/608w1001.png"
im = Image.open(filename)
box = (100, 0, 750, 250)
region = im.crop(box)
region.show()