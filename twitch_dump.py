from website_extract import read_state
import os
import time
import shutil
import re

state = read_state()

def wait_for_bets():
	global state
	while state['status'] != 'open':  
		state = read_state()
		time.sleep(15)

wait_for_bets()

for i in range(200):
	wait_for_bets()
	vid_path = os.path.join('vid_dir', str(i).zfill(3))
	os.system("timeout 1.5 livestreamer www.twitch.tv/saltybet Source -o " + vid_path + ".flv")
	
	time.sleep(25)
	while state['status'] not in ['1', '2']:  # wait for result
		state = read_state()
		time.sleep(15)
	winner = str(state['status'])

	try:
		vid_name = vid_path + 'w' + winner + '.flv'
		shutil.move(vid_path + '.flv', vid_name)
		img_path = re.sub(r"\.flv", r"%3d.png", vid_name)
		os.system("ffmpeg -i " + vid_name + " -r 1 -t 1 " + img_path)
	except:
		print "missed a betting round.  skipping"
		wait_for_bets()
		continue

