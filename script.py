#Rename image files
import os 
import argparse

def main():
	'''
	Rename files eg: image_0001.jpg to fixed index length say 7 as image_0000001.jpg
	'''

	parser = argparse.ArgumentParser(description = "Renaming the images in uniform index format")
	parser.add_argument("path", help = "Path of the file containing the images")
	parser.add_argument("index", help = "Number of the fixed indexes the file will be")
	args = parser.parse_args()

	_, _, files = next(os.walk(args.path))

	files = sorted(files)
	
	for file in files:
		fp = file 
		fp = int(fp.split("_")[1][:-4])
		os.rename(os.path.join(args.path,file),os.path.join(args.path,"image_{num:0{size}d}".format(num = fp, size = args.index)))




if __name__ == '__main__':
	main()
	
