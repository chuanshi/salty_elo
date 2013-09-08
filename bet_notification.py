from website_extract import read_state
from twitch_dump import wait_for_bets
import time
import os

while True:
    wait_for_bets()

    try:  # for ubuntu desktop sound playing
        os.system("/usr/bin/canberra-gtk-play --id='bell'")
    except:
        pass

    print "bet time!"
    time.sleep(60)
