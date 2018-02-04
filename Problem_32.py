import random
import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

def deBruijnPair(pairs):
    graph = {}
    for each in pairs:
        prefix = each[0][:-1],each[1][:-1]
        suffix = each[0][1:],each[1][1:]
        graph.setdefault(prefix,[]).append(suffix)
    return graph

def parsePairs(pairs):
    d = []
    for line in pairs:
        d.append(line.split('|'))
    return d

def reconstructFromPath(patterns):
    text = patterns.pop(0)
    for kmer in patterns:
        text += kmer[-1]
    return text

def stringFromPairedPath(k,d,path):
    prefix = reconstructFromPath([x[0] for x in path])
    suffix = reconstructFromPath([x[1] for x in path])
    if prefix[k+d:] != suffix[:-(k+d)]:
        return None
    string = prefix+suffix[-(k+d):]
    return string

def reconstructFromPairs(k,d,pairedReads):
    string=None
    while string is None:
        dbGraph = deBruijnPair(parsePairs(pairedReads))
        epath = [] 
        curr_path = [] 
        start_v = ()
        preNodes = list(dbGraph.keys())
        outNodes = [x[0] for x in list(dbGraph.values())] 
        start_v = list(set(preNodes)-set(outNodes))[0] 
        curr_path = [start_v] 
        while len(curr_path):
            curr_v = curr_path[-1]
            if curr_v in dbGraph.keys() and len(dbGraph[curr_v]) != 0:
                next_v = random.choice(dbGraph[curr_v])
                curr_path.append(next_v)
                dbGraph[curr_v].remove(next_v)
            else:
                epath.insert(0,curr_path.pop())
        string = stringFromPairedPath(k,d,epath)
    return string

def main():
    args = arg_parse()

    data = []
    with open(args.input) as infile:
        data = infile.read().splitlines()
    k,d = [int(x) for x in data.pop(0).split()]
    
    with open(args.output,'w') as outfile:
        outfile.write(reconstructFromPairs(k,d,data))

main()