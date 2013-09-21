import glob
import os

files = glob.glob('*.png')
files = list(set(files) - set(['1.png', '2.png', '3.png', '4.png']))
for i in range(200):
	file = str(i) + ".png"
	if file in files:
		os.system('tesseract ' + file + ' eng.salty.exp' + str(i) + ' batch.nochop makebox')