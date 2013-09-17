import glob
import os

files = glob.glob('*.box')

box_list = []

for i in range(200):
	file = 'eng.salty.exp' + str(i) + ".box"
	if file in files:
		box_list.append(file)

boxes = ' '.join(box_list)
os.system('unicharset_extractor ' + boxes)