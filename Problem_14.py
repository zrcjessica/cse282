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

def Neighbors(Pattern, d):
    if d == 0:
        return [Pattern]
    if len(Pattern) == 1:
        return ['A','C','G','T']
    neighborhood = []
    suffixNeighbors = Neighbors(Pattern[1:],d)
    for each in suffixNeighbors:
        if HammingDistance(Pattern[1:], each) < d:
            for base in ['A','C','G','T']:
                neighborhood.append(base+each)
        else:
            neighborhood.append(Pattern[0]+each)
    return neighborhood

def ApproxPatternCount(Pattern, Text, d):
    occurrences = 0
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            occurrences += 1
    return occurrences
    
def MotifEnumeration(Dna, k, d):
    Patterns = []
    dnaKmers = []
    for string in Dna:
        for i in range(len(string)-k+1):
            dnaKmers.append(string[i:i+k])
    dnaKmers = set(dnaKmers)
    for kmer in dnaKmers:
        for neighbor in Neighbors(kmer, d):
            substr_check = [ApproxPatternCount(neighbor,string,d)>0 for string in Dna]
            if sum(substr_check) == len(Dna):
                Patterns.append(neighbor)
    return list(set(Patterns))

def main():
	args = arg_parse()
	# run code
	dataset = []
	with open(args.input) as in_fh:
	    dataset = in_fh.read().splitlines()
	k,d = [int(x) for x in dataset[0].split()]
	dna = [dataset[i] for i in range(1,len(dataset))]

	with open(args.output,'w') as fh:
	    fh.write(' '.join(MotifEnumeration(dna,k,d)))
main()