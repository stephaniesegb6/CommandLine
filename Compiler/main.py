import sys
import argparse
import Compilercpp

main_parser = argparse.ArgumentParser(description = "Short compiler command")

main_parser.add_argument('Inputfile', metavar = 'inputfile', type = str, nargs = '+', help = 'File to compile')

main_parser.add_argument(
	'--norun',
	dest = 'isrun',
	action = 'store_false',
	help = 'Compile without running.'
)

def main():
	arg = main_parser.parse_args()
	# print(arg)
	files = arg.Inputfile
	try:
		language = Compilercpp.checkLanguages(files)
	except Exception as e:
		print(e)
		sys.exit(0)
	if(language == 'cpp'):
		compiler = Compilercpp.CompilerCpp(files)
	compiler.compile()
	if(arg.isrun):
		compiler.run()
	

if __name__ == '__main__':
	main()
