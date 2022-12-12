import os
import sys
import argparse
import copyTemplate

if getattr(sys, 'frozen', False):
	path = os.path.dirname(sys.executable)
else:
	path = os.path.dirname(__file__)
template = copyTemplate.copyTemplate(path)

main_parser = argparse.ArgumentParser(
	description = "Create a new file"
)

main_parser.add_argument(
	"File",
	metavar = "file",
	type = str,
	nargs = "+",
	help = "Name file will be created"
)

main_parser.add_argument(
	"--cpp",
	dest = "copyTemplate",
	action = "store_const",
	const = template.templateCpp,
	help = "make file .cpp with your template."
)

def main():
	args = main_parser.parse_args()
	files : list[str] = args.File

	for file in files:
		try:
			f = open(file, 'x')
			if(args.copyTemplate != None):
				# print()
				args.copyTemplate(f)
			f.close()
		except Exception as e:
			print(e)


if __name__ == "__main__":
	main()
