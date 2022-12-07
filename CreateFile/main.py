import argparse


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



def main():
	files : list[str] = main_parser.parse_args().File

	for file in files:
		try:
			f = open(file, 'x')
			f.close()
		except Exception as e:
			print(e)


if __name__ == "__main__":
	main()
