import argparse
import os
import sys

if getattr(sys, 'frozen', False):
	path = os.path.dirname(sys.executable)
else:
	path = os.path.dirname(__file__)

main_parser = argparse.ArgumentParser(
	description = "Count time running of a program."
)

main_parser.add_argument(
	"File",
	metavar = "file",
	type = str,
	help = "Program you want to count time running."
)

def main():
	args = main_parser.parse_args()

	file : str = args.File
	# print(path)
	os.system(fr"{path}\C++Source\timecpp.exe {file}")

if __name__ == "__main__":
	main()