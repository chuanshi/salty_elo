from glob import glob
import os

files = glob("2*.png")

for file in files:
	os.rename(file, "eng.salty.exp" + file)
