def templateCpp(file):
	source = open("./templateTouch/cpp.txt", "r")
	for line in source:
		file.writelines(line)

