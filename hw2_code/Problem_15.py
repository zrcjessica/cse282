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

def NumToPattern(index,k):
    dna = ['A','C','G','T']
    if k == 1:
        return dna[index]
    prefixIndex = int(index/4)
    r = index%4
    symbol = dna[r]
    prefixPattern = NumToPattern(prefixIndex, k-1)
    return prefixPattern+symbol

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0
    for string in Dna:
        HammingDist = float('inf')
        for i in range(len(string)-k+1):
            kmer = string[i:i+k]
            if HammingDist > HammingDistance(Pattern, kmer):
                HammingDist = HammingDistance(Pattern, kmer)
        distance = distance + HammingDist
    return distance

''' REMEMBER TO RETURN JUST ONE INSTEAD OF LIST OF MEDIAN STRINGS'''
def MedianString(Dna,k):
    distance = float('inf')
    median = ''
    for i in range(4**k):
        pattern = NumToPattern(i,k)
        if distance>DistanceBetweenPatternAndStrings(pattern, Dna):
            distance = DistanceBetweenPatternAndStrings(pattern, Dna)
            median = pattern
    return median

def main():
	args = arg_parse()

	dataset = []
	with open(args.input) as in_fh:
	    dataset = in_fh.read().splitlines()
	k = int(dataset[0][0])
	dna = [dataset[i] for i in range(1,len(dataset))]

	with open(args.output,'w') as fh:
	    fh.write(MedianString(dna,k))
main()