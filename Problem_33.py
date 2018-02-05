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

def nonBranching(graph,v):
    keys = list(graph.keys())
    values = [node for sublist in graph.values() for node in sublist]
    in_v = values.count(v)
    out_v = 0
    if v in keys:
        out_v = len(graph[v])
    if in_v == 1 and out_v == 1:
        return True
    return False

def isolatedCycles(graph):
    isolatedCycles = []
    foundCycles = set()
    keys = list(graph.keys())
    values = [node for sublist in graph.values() for node in sublist]
    allNodes = set(keys+values)
    for v in allNodes:
        currCycle = []
        if nonBranching(graph,v) and v not in foundCycles:  
            currCycle.append(v)
            w = graph[v][0]
            while nonBranching(graph,w) and w != currCycle[0]:
                foundCycles.add(w)
                currCycle.append(w)
                w = graph[w][0]
            if nonBranching(graph,w) and w == currCycle[0]:
                isolatedCycles.append(currCycle)
                foundCycles = set(currCycle)
                currCycle = []
    return isolatedCycles

def reconstructFromPath(patterns):
    text = patterns.pop(0)
    for kmer in patterns:
        text += kmer[-1]
    return text

def maxNonBranchingPaths(graph):
    paths = []
    keys = list(graph.keys())
    values = [node for sublist in graph.values() for node in sublist]
    allNodes = set(keys+values)
    for v in allNodes:
        keys = list(graph.keys())
        values = [node for sublist in graph.values() for node in sublist]
        in_v = values.count(v)
        out_v = 0
        if v in keys:
            out_v = len(graph[v])
        if out_v>0 and not nonBranching(graph,v):
            for w in graph[v]:
                nonBranchPath = [v,w]
                while nonBranching(graph,w):
                    u = graph[w][0]
                    nonBranchPath.append(u)
                    w = u
                paths.append(nonBranchPath)
    if len(isolatedCycles(graph))>0:
        paths.append(isolatedCycles(graph))
    return paths
       
def genContigs(patterns):
    dbGraph = deBruijnKmer(patterns)
    paths = maxNonBranchingPaths(dbGraph)
    contigs = []
    for each in paths:
        contigs.append(reconstructFromPath(each))
    return contigs

def main():
    args = arg_parse()

    data = []
    with open(args.input) as infile:
        data = infile.read().splitlines()
    
    with open(args.output,'w') as outfile:
        outfile.write(' '.join(genContigs(data)))

main()