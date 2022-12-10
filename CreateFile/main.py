import argparse
import copyTemplate

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
	const = copyTemplate.templateCpp,
	help = "make file .cpp with your template."
)

def main():
	args = main_parser.parse_args()
	files : list[str] = args.File

	for file in files:
		try:
			f = open(file, 'x')
			if(args.copyTemplate != None):
				args.copyTemplate(f)
			f.close()
		except Exception as e:
			print(e)


if __name__ == "__main__":
	main()
