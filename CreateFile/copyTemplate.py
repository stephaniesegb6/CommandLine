class copyTemplate:
	def __init__(self, path):
		self.path = path

	def templateCpp(self, file):
		source = open(f"{self.path}/templateTouch/cpp.txt", "r")
		for line in source:
			file.writelines(line)

