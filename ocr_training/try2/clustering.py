import glob
import os

files = glob.glob('*.tr')

tr_list = []

for i in range(300):
	file = 'eng.salty.exp' + str(i) + ".tr"
	if file in files:
		tr_list.append(file)

trs = ' '.join(tr_list)
os.system('mftraining -F font_properties -U unicharset ' + trs)
os.system('cntraining ' + trs)