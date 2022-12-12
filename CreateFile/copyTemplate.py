import os

currentDir = os.path.dirname(os.path.realpath(__file__))

def templateCpp(file):
	source = open(f"{currentDir}/templateTouch/cpp.txt", "r")
	for line in source:
		file.writelines(line)

