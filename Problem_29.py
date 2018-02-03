import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

def parseEulerian(fh):
    graph = {}
    lines = []
    with open(fh) as infile:
        lines = infile.read().splitlines()
    for row in lines:
        inNode, outNodes = row.split(' -> ')
        outNodes_list = outNodes.split(',')
        graph[inNode] = outNodes_list
    return(graph)

def EulerianPath(adj_list):
    epath = []
    curr_path = []
    start_v = ''
    allNodes = [node for sublist in adj_list.values() for node in sublist]
    for node in set(allNodes):
        inDegs = allNodes.count(node)
        outDegs = -1
        if node in list(adj_list.keys()):
            outDegs = len(adj_list.get(node))
        else:
            outDegs = 0
        if inDegs != outDegs and outDegs>0:
            start_v = node
    curr_path = [start_v]
    while len(curr_path):
        curr_v = curr_path[-1]
        if curr_v in adj_list.keys() and len(adj_list[curr_v]) != 0:
            next_v = adj_list[curr_v][0]
            curr_path.append(next_v)
            adj_list[curr_v].remove(next_v)
        else:
            epath.insert(0,curr_path.pop())
    return epath

def main():
    args = arg_parse()

    data = parseEulerian(args.input)

    with open(args.output,'w') as fh:
        fh.write('->'.join(EulerianPath(data)))
main()