from website_extract import read_state
import os
import time
import shutil
import re
import json
import pickle
from ocr_clean import *
from analyze_images import *
from salty_elo import predict

state = read_state()

def wait_for_bets():
	global state

	while state['status'] != 'open':  
		state = read_state()
		time.sleep(13)

def video_to_png(video_path):
	"""converts a .flv video to a .png"""
	img_path = re.sub(r"flv", r"png", video_path)
	os.system("ffmpeg -i " + video_path + " -r 1 -t 1 " + img_path)
	return img_path


if __name__ == "__main__":
        db = pickle.load(open('db.pickle'))
        matches = json.load(open('matches.json', 'r'))

	wait_for_bets()

	for i in range(1000):
		wait_for_bets()

		vid_path = os.path.join('vid_dir', str(i).zfill(3) + ".flv")
		os.system("timeout 2.0 livestreamer www.twitch.tv/saltybet Source -o " + vid_path)

		if not os.path.exists(vid_path):
			print "missed a betting round.  skipping"
			time.sleep(30)
			continue
		img_path = video_to_png(vid_path)
		match = ocr_match_from_image(img_path, cleanup=True)
                if len(match) > 1:
                        predict(match[0], match[1], db, matches)
		time.sleep(25)
		while state['status'] not in ['1', '2']:  # wait for result
			state = read_state()
			time.sleep(13)
		winner = state['status']

		# rename video and images with winner
		vid_name = os.path.join('vid_dir', str(i).zfill(3) + 'w' + winner + '.flv')
		img_name = os.path.join('vid_dir', str(i).zfill(3) + 'w' + winner + '.png')
		shutil.move(vid_path, vid_name)
		shutil.move(img_path, img_name)

		match = ocr_match_from_image(img_name)
		print match


