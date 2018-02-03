import random
import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

def deBruijnKmer(patterns):
    graph = {}
    for kmer in patterns:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph.setdefault(prefix,[]).append(suffix)
    return graph

def reconstructString(k,patterns):
    dbGraph = deBruijnKmer(patterns)
    epath = []
    curr_path = []
    start_v = ''
    preNodes = list(dbGraph.keys())
    outNodes = [x[0] for x in list(dbGraph.values())]
    start_v = list(set(preNodes)-set(outNodes))[0]
    curr_path = [start_v]
    while len(curr_path):
        curr_v = curr_path[-1]
        if curr_v in dbGraph.keys() and len(dbGraph[curr_v]) != 0:
            next_v = dbGraph[curr_v][0]
            curr_path.append(next_v)
            dbGraph[curr_v].remove(next_v)
        else:
            epath.insert(0,curr_path.pop())
    string = reconstructFromPath(epath)
    return string

def main():
    args = arg_parse()

    data = []
    with open(args.input) as infile:
        data = infile.read().splitlines()

    k = int(data.pop(0))

    with open(args.output,'w') as fh:
        fh.write(reconstructString(k,data))
main()