import os
import glob
import sys
from ocr_clean import *

path = sys.argv[1]

images = glob.glob(os.path.join(path, "[0-9]*.png"))
images.sort()

for image in images:
	clean_image(image)
	basename = os.path.basename(image)
	red_image = os.path.join(path, "cleaned_red_" + basename)
	blue_image = os.path.join(path, "cleaned_blue_" + basename)
	os.system('tesseract -l eng+eng1 ' + red_image + ' /tmp/red')
	print "done"
	f = open('/tmp/red.txt')
	text = f.readlines()
	if len(text) > 0:
		red_text = text[0]
	else:
		os.system('rm -f /tmp/red.txt')
		continue
	f.close()
	os.system('tesseract -l eng+eng1 ' + blue_image + ' /tmp/blue')
	f = open('/tmp/blue.txt')
	text = f.readlines()
	if len(text) > 0:
		blue_text = text[0]
	else:
		os.system('rm -f /tmp/blue.txt')
		continue
	f.close()
	os.system('rm -f /tmp/red.txt')
	os.system('rm -f /tmp/blue.txt')
	print red_text, blue_text

