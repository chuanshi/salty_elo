import glob
import os

files = glob.glob('*.png')
for i in range(300):
	file = "eng.salty.exp" + str(i) + ".png"
	if file in files:
		os.system('tesseract -l eng1+eng ' + file + ' eng.salty.exp' + str(i) + ' batch.nochop makebox')