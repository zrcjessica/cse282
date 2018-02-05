import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

def reconstructFromPath(patterns):
    text = patterns.pop(0)
    for kmer in patterns:
        text += kmer[-1]
    return text

def stringFromGappedPath(gappedPatterns,k,d):
    pairsA = []
    pairsB = []
    for pair in gappedPatterns:
        a,b = pair.split('|')
        pairsA.append(a)
        pairsB.append(b)
    prefix = reconstructFromPath(pairsA)
    suffix = reconstructFromPath(pairsB)
    string = prefix+suffix[-(k+d):]
    return string

def main():
    args = arg_parse()

    data = []
    with open(args.input) as infile:
        data = infile.read().splitlines()
    k,d = [int(x) for x in data.pop(0).split()]

    with open(args.output,'w') as outfile:
        outfile.write(stringFromGappedPath(data,k,d))

main()