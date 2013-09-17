import glob
import os

files = glob.glob('*.png')
counter = 0
for i in range(200):
	file = 'eng.salty.exp' + str(i) + ".png"
	if file in files:
		counter += 1
		print counter, file