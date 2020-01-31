import argparse
import warnings
#warnings inserted

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(dest="file", help="input the file name here")
	parser.add_argument(dest ="kmer", help= "input K-mer here")
	args = parser.parse_args()


	file = open(args.file,"r")
	code = file.read()
	
	
	code = code.rstrip('\r\n').replace("\n",'') 
	code = code.capitalize()

	nucleotides = {}
	size = int(args.kmer)
	i = 0
	nuc = ""

	while i<= (len(code)-1 - size):
		nuc = code[i:(i+size)]
		if nuc in nucleotides:
			nucleotides[nuc] += 1
		else:
			nucleotides[nuc] = 1
		i = i+1
		
		
	outfile = open("results.txt","w")
	for key in nucleotides:
		outfile.write(key + "   " + str(nucleotides[key]))
		outfile.write("\n")
		
	
main()


