import argparse
import Compilercpp

main_parser = argparse.ArgumentParser(description = "Short compiler command")

main_parser.add_argument('Inputfile', metavar = 'inputfile', type = str, nargs = '+', help = 'File to compile')

def main():
	arg = main_parser.parse_args()
	# print(arg)
	compiler = Compilercpp.Compiler(arg.Inputfile)
	compiler.run()
		

if __name__ == '__main__':
	main()
