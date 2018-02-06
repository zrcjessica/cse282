import random
import copy
import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

def noIncomingEdges(node,graph):
    values = [node[0] for sublist in graph.values() for node in sublist]
    if node not in values:
        return True
    return False

def parseDAG(fh):
    data = []
    with open(fh) as infile:
        data = infile.read().splitlines()
    source = int(data.pop(0))
    sink = int(data.pop(0))
    graph = {}
    for line in data:
        x,y = line.split('->')
        graph.setdefault(int(x),[]).append([int(d) for d in y.split(':')])
    return source,sink,graph

def topologicalOrdering(graph):
    l = []
    keys = list(graph.keys())
    values = [node[0] for sublist in graph.values() for node in sublist]
    candidates = list(set(keys)-set(values))
    while len(candidates):
        a = random.choice(candidates)
        l.append(a)
        candidates.remove(a)
        if a in graph.keys():
            for b in list(graph[a]):
                graph[a].remove(b)
                if noIncomingEdges(b[0],graph):
                    candidates.append(b[0])
            if a in graph.keys():
                outNodes = list(graph[a])
                for b in outNodes:
                    graph[a].remove(b)
                    if noIncomingEdges(b[0],graph):
                        candidates.append(b[0])
    outEdges = [len(graph[node]) for node in keys]
    if sum(outEdges):
        return False
    else:
        return l

def getPredecessors(graph, node):
    p = []
    for key,value in graph.items():
        for sublist in value:
            if sublist[0] == node:
                p.append(key)
    return p
    
def longestPath(graph,source,sink):
    prevDict = {}
    path = []
    keys = list(graph.keys())
    values = [node[0] for sublist in graph.values() for node in sublist]
    allNodes = set(keys+values)
    noPredecessors = set(keys)-set(values)
    s = [-float('inf')]*(sink+1)
    s[source]=0
    graphCopy = copy.deepcopy(graph)
    topo = topologicalOrdering(graphCopy)
    if topo:
        for b in topo[topo.index(source):len(topo)]:
            if topo.index(b)>topo.index(source) and b not in noPredecessors:
                arr = []
                predecessors = getPredecessors(graph,b)
                for a in predecessors:
                    a_outnodes = [sublist[0] for sublist in graph[a]]
                    a_weights = [sublist[1] for sublist in graph[a]]
                    abWeight = a_weights[a_outnodes.index(b)]
                    arr.append(s[a]+abWeight)
                s[b] = max(arr)
                prevDict[b] = predecessors[arr.index(s[b])]
    curr = sink
    path.append(sink)
    while not noIncomingEdges(curr,graph):
        prev = prevDict[curr]
        path.insert(0,prev)
        curr=prev
    return s[sink],path

def main():
    args = arg_parse()

    source,sink,graph = parseDAG(args.input)
    output = longestPath(graph,source,sink)

    with open(args.output,'w') as outfile:
        outfile.write(str(output[0])+'\n')
        outfile.write('->'.join(str(x) for x in output[1])+'\n')

main()