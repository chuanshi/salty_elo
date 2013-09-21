import glob
import os

files = glob.glob('*.png')
for i, file in enumerate(files):
	os.system('mv ' + file + ' ' + str(i) + ".png")