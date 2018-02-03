import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

def HammingDistance(p,q):
    hdist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hdist += 1
    return hdist

def DistanceBetweenPatternAndStrings(pattern,dna):
    k = len(pattern)
    distance = 0
    for seq in dna:
        hamDist = float('inf')
        for i in range(len(seq)-k+1):
            kmer = seq[i:i+k]
            if hamDist > HammingDistance(pattern,kmer):
                hamDist = HammingDistance(pattern,kmer)
        distance += hamDist
    return distance

def main():
	args = arg_parse()

	dataset = []
	with open(args.input) as in_fh:
	    dataset = in_fh.read().splitlines()
	pattern = dataset[0]
	dna = dataset[1].split()

	with open(args.output,'w') as fh:
	    fh.write(str(DistanceBetweenPatternAndStrings(pattern,dna)))
main()