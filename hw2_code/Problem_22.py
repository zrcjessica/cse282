import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

def NumToPattern(index,k):
    dna = ['A','C','G','T']
    if k == 1:
        return dna[index]
    prefixIndex = int(index/4)
    r = index%4
    symbol = dna[r]
    prefixPattern = NumToPattern(prefixIndex, k-1)
    return prefixPattern+symbol

def main():
	args = arg_parse()

	dataset = []
	with open(args.input) as in_fh:
	    dataset = [int(x) for x in in_fh.read().splitlines()]

	with open(args.output,'w') as fh:
	    fh.write(NumToPattern(dataset[0],dataset[1]))
main()