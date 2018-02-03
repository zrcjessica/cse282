import random
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
        
def EulerianCycle(adj_list):
    ecycle = []
    start_v = random.choice(list(adj_list.keys()))
    curr_path = [start_v]
    while len(curr_path):
        curr_v = curr_path[-1]
        if len(adj_list[curr_v]) != 0:
            next_v = adj_list[curr_v][0]
            curr_path.append(next_v)
            adj_list[curr_v].remove(next_v)
        else:
            curr_path.pop()
            ecycle.insert(0,curr_v)
    return ecycle

def main():
    args = arg_parse()

    data = parseEulerian(args.input)

    with open(args.output,'w') as fh:
        fh.write('->'.join(EulerianCycle(data)))
main()