import Image
import os

# the near_orange_or_black functions returns white if it matches orange and
# black if it matches black

def match_fuzziness(input1, input2, fuzziness):
	diff = [abs(input1[i] - input2[i]) for i in range(3)]  # input1 and 2 assumed to be len 3 arraylikes
	if max(diff) < fuzziness:
		return True
	return False

def clean_image(input_filename, out_red_filename=None, out_blue_filename=None, outdir=None):
	orange = [212, 69, 47]
	blue = [47, 156, 251]
	black = [0, 0, 0]
	fuzziness = 20

	filename = os.path.basename(input_filename)

	if not outdir:
		outdir = os.path.dirname(input_filename)
	if not out_red_filename:
		out_red_filename = os.path.join(outdir, "cleaned_red_" + filename)
	if not out_blue_filename:
		out_blue_filename = os.path.join(outdir, "cleaned_blue_" + filename)

	im = Image.open(input_filename)
	red_box = (110, 0, 740, 40)
	blue_box = (110, 417, 740, 457)
	red_region = im.crop(red_box)
	blue_region = im.crop(blue_box)

	red_out = Image.new(red_region.mode, red_region.size, "white")
	blue_out = Image.new(blue_region.mode, blue_region.size, "white")

	for x in range(red_region.size[0]):
		for y in range(red_region.size[1]):
			pix = red_region.getpixel((x,y))
			if match_fuzziness(pix, black, fuzziness):
				red_out.putpixel((x,y), (255, 255, 255))
			elif match_fuzziness(pix, orange, fuzziness):
				red_out.putpixel((x,y), (0, 0, 0))

	for x in range(blue_region.size[0]):
		for y in range(blue_region.size[1]):
			pix = blue_region.getpixel((x,y))
			if match_fuzziness(pix, black, fuzziness):
				blue_out.putpixel((x,y), (255, 255, 255))
			elif match_fuzziness(pix, blue, fuzziness):
				blue_out.putpixel((x,y), (0, 0, 0))

	# out.show()
	red_out.save(out_red_filename)
	blue_out.save(out_blue_filename)

if __name__=="__main__":
	import sys
	filename = sys.argv[1]
	clean_image(filename)