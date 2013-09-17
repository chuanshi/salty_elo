import glob
import os

files = glob.glob('*.png')
for i in range(200):
	file = str(i) + ".png"
	if file in files:
		f = open('eng.salty.exp' + str(i) + '.box')
		lines = f.readlines()
		text_list = []
		for line in lines:
			text_list.append(line[0])
		text = ''.join(text_list)
		print file, text
