import argparse
import sys

main_parser = argparse.ArgumentParser(
	description = "Compare two files."
)

main_parser.add_argument("File1", type=str, metavar="file1")
main_parser.add_argument("File2", type = str, metavar = "file2")

def main():
	args = main_parser.parse_args()
	try : 
		file1 = open(args.File1, "r").readlines()
	except Exception as e :
		print(e)
		sys.exit(0)
	try : 
		file2 = open(args.File2, "r").readlines()
	except Exception as e :
		print(e)
		sys.exit(0)
	line = 0
	checkSize = (len(file1) == len(file2))
	for x, y in zip(file1, file2):
		line += 1
		x = x.rstrip("\n")
		y = y.rstrip("\n")
		if(x != y):
			if(not checkSize):
				print("Two files have different sizes.\nAnother difference :")
			else:
				print("Two files are difference :")
			print(f"{args.File1}:")
			print(f"   {line}| {x}")
			print(f"{args.File2}:")
			print(f"   {line}| {y}")
			sys.exit(0)
	if(checkSize):
		print("Two files are same")
	else: 
		print("Two files have difference.")


if __name__ == "__main__":
	main()
