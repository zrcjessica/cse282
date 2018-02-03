import argparse

def arg_parse():
	parser = argparse.ArgumentParser(description='Process input and output files.')
	parser.add_argument('input', help='input filehandle')
	parser.add_argument('output', help='output filehandle')
	return parser.add_args()

def deBruijnKmer(patterns):
    graph = {}
    for kmer in patterns:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph.setdefault(prefix,[]).append(suffix)
    return graph

def main():
	args = arg_parse()
	# run code
dataset = []
with open('rosalind_ba2a.txt') as in_fh:
    dataset = in_fh.read().splitlines()
k,d = [int(x) for x in dataset[0].split()]
dna = [dataset[i] for i in range(1,len(dataset))]

with open('rosalind_ba2a.output','w') as fh:
    fh.write(' '.join(MotifEnumeration(dna,k,d)))