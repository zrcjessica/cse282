import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

def parseInput(fh):
    graph = {}
    lines = []
    with open(fh) as infile:
        lines = infile.read().splitlines()
    for row in lines:
        inNode, outNodes = row.split(' -> ')
        outNodes_list = outNodes.split(',')
        graph[inNode] = outNodes_list
    return(graph)

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
                currCycle.append(w)
                isolatedCycles.append(currCycle)
                foundCycles = set(currCycle)
                currCycle = []
    return isolatedCycles

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
    for each in isolatedCycles(graph):
            paths.append(each)
    return paths

def main():
    args = arg_parse()

    data = parseInput(args.input)

    with open(args.output,'w') as outfile:
        for each in maxNonBranchingPaths(data):
            outfile.write(' -> '.join(each)+'\n')

main()