import random

def parseDAG(fh):
    data = []
    with open(fh) as infile:
        data = infile.read().splitlines()
    graph = {}
    for line in data:
        x,y = line.split('->')
        graph[int(x)] = [int(d) for d in y.split(',')]
    return graph

def noIncomingEdges(node,graph):
    values = [node for sublist in graph.values() for node in sublist]
    if node not in values:
        return True
    return False

def topologicalOrdering(graph):
    l = []
    keys = list(graph.keys())
    values = [node for sublist in graph.values() for node in sublist]
    candidates = list(set(keys)-set(values))
    while len(candidates):
        a = random.choice(candidates)
        l.append(a)
        candidates.remove(a)
        if a in graph.keys():
            for b in list(graph[a]):
                graph[a].remove(b)
                if noIncomingEdges(b,graph):
                    candidates.append(b)
            if a in graph.keys():
                outNodes = list(graph[a])
                for b in outNodes:
                    graph[a].remove(b)
                    if noIncomingEdges(b,graph):
                        candidates.append(b)
    outEdges = [len(graph[node]) for node in keys]
    if sum(outEdges):
        return False
    else:
        return l
        
graph = parseDAG('rosalind_ba5n.txt')
print(', '.join([str(x) for x in topologicalOrdering(graph)]))