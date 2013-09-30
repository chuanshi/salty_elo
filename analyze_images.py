import os
import glob
import sys
import pickle
import json
from ocr_clean import *
from elo_funcs import *

def ocr_match_from_image(image_path, cleanup=False):
	clean_image(image_path)
	path = os.path.dirname(image_path)
	basename = os.path.basename(image_path)
	red_image = os.path.join(path, "cleaned_red_" + basename)
	blue_image = os.path.join(path, "cleaned_blue_" + basename)
	winner = basename[4]  # assumes image file name of the form 902w1001.png
	os.system('tesseract -l eng+eng2 ' + red_image + ' /tmp/red')
	f = open('/tmp/red.txt')
	text = f.readlines()
	if len(text) > 0:
		red_text = str(text[0]).rstrip("\n")
	else:
		os.system('rm -f /tmp/red.txt')
		return []
	f.close()
	os.system('tesseract -l eng+eng2 ' + blue_image + ' /tmp/blue')
	f = open('/tmp/blue.txt')
	text = f.readlines()
	if len(text) > 0:
		blue_text = str(text[0]).rstrip("\n")
	else:
		os.system('rm -f /tmp/blue.txt')
		return []
	f.close()
	os.system('rm -f /tmp/red.txt')
	os.system('rm -f /tmp/blue.txt')
	match = [red_text, blue_text, winner]

	if cleanup:
		os.remove(red_image)
		os.remove(blue_image)

	return match

if __name__ == '__main__':
	path = sys.argv[1]

	images = glob.glob(os.path.join(path, "[0-9]*.png"))
	images.sort()

	db = pickle.load(open('db.pickle'))
	matches = json.load(open('matches.json', 'r'))

	for image in images:
		match = ocr_match_from_image(image, cleanup=True)
                if len(match) == 0:
                        continue
		if match[0] in db.keys() and match[1] in db.keys():
			print "Found both!", match
			matches.append(match)
			os.remove(image)

	db = regenerate_db(matches, 'db.pickle')
	save_db(db, matches)
