import glob
import os

files = glob.glob('eng.salty.exp*.png')
for i in range(300):
	file = 'eng.salty.exp' + str(i) + ".png"
	if file in files:
		os.system('tesseract -l eng+eng1 ' + file + ' eng.salty.exp' + str(i) + ' box.train.stderr')