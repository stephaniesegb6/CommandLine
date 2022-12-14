import os

class Compiler:
	def __init__(self, files : list[str]):
		self.files = files
		self.name = self.files[0]
		self.formatName()
	def formatName(self):
			if self.name[len(self.name) - 4 : len(self.name)] == '.cpp' : self.name = self.name[0 : len(self.name) - 3]
			self.name = self.name.translate({ord(c) : None for c in "/\."})
	def run(self):
		command = "g++ "
		for i in range(len(self.files)):
			command += f"{self.files[i]} "
		command += f"-o {self.name}.exe"
		# print(command)
		os.system(command)
		print("Finish compiling!")
		print("Running...")
		os.system(f"timer {self.name}.exe")
