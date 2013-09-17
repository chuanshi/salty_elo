import glob
import os

files = glob.glob('*.png')
for i in range(200):
	file = str(i) + ".png"
	if file in files:
		new_file = 'eng.salty.exp' + str(i) + '.png'
		os.system('mv ' + str(i) + '.png ' + new_file)
		os.system('tesseract ' + new_file + ' eng.salty.exp' + str(i) + ' box.train.stderr')