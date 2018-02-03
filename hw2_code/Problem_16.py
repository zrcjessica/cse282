import argparse

def arg_parse():
	parser = argparse.ArgumentParser(description='Process input and output files.')
	parser.add_argument('input', help='input filehandle')
	parser.add_argument('output', help='output filehandle')
	return parser.parse_args()

def ProbableKmer(Text, k, Profile):
    dna = {'A':0, 'C':1,'G':2,'T':3}
    probableKmers = {}
    for i in range(len(Text)-k+1):
        kmer = Text[i:i+k]
        cum_prod = 1
        for j in range(k):
            cum_prod = cum_prod*Profile[dna.get(kmer[j])][j]
        probableKmers[kmer] = cum_prod
    return max(probableKmers, key=probableKmers.get)

def main():
	args = arg_parse()

	dataset = []
	with open(args.input) as in_fh:
	    dataset = in_fh.read().splitlines()
	sequence = dataset[0]
	k = int(dataset[1])
	matrix = []
	for i in range(2,len(dataset)):
		matrix.append([float(x) for x in dataset[i].split()])

	with open(args.output,'w') as fh:
	    fh.write(ProbableKmer(sequence,k,matrix))
main()