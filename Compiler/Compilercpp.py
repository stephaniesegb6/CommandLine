import os

class Compiler:
	def __init__(self, files : list[str]):
		self.files = files
		self.name = self.files[0]
		# self.formatName()
	
class CompilerCpp(Compiler):
	def __init__(self, files : list[str]):
		super().__init__(files)
		self.formatName()
	def formatName(self):
		if self.name[len(self.name) - 4 : len(self.name)] == '.cpp' : self.name = self.name[0 : len(self.name) - 3]
		self.name = self.name.translate({ord(c) : None for c in "/\."})
	def compile(self):
		command = "g++ "
		for i in range(len(self.files)):
			command += f"{self.files[i]} "
		command += f"-o {self.name}.exe -std=c++11 -static-libgcc -static-libstdc++"
		# print(command)
		os.system(command)
		print("Finish compiling!")
	def run(self):
		print("Running...")
		os.system(f"timer .\{self.name}.exe")

def findLanguageOfFile(file : str):
	if(file[len(file) - 4 : len(file)] == '.cpp'):
		return 'cpp'

def checkLanguages(files : list[str]):
	CountLanguage = 0
	Language = ""
	for file in files :
		Language = findLanguageOfFile(file)
		# print(Language)
		CountLanguage += 1
		if(CountLanguage > 1):
			raise ValueError("Too many languages!")
	return Language