import os
import glob

vid_dir = "vid_dir"

files = glob.glob(vid_dir + "/*.flv")
for file in files:
    img_path = os.path.join(vid_dir, os.path.splitext(os.path.basename(file))[0])
    os.system("ffmpeg -i " + file + " -r 1 -t 1 " + img_path + "%3d.png")
