import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

def overlapAlignment(v,w):
    v_out,w_out = '',''
    d = {}
    m,n = len(w),len(v)
    s = [[0]*(n+1) for row in range(m+1)]
    for j in range(1,n+1):
        for i in range(1,m+1):
            arr = [s[i-1][j]-2, s[i][j-1]-2, s[i-1][j-1]+[-2,1][v[j-1]==w[i-1]]]
            s[i][j] = max(arr)
            prev_coord = [(i-1,j),(i,j-1),(i-1,j-1)][arr.index(s[i][j])]
            d[i,j] = [prev_coord,[(w[i-1],'-'),('-',v[j-1]),(w[i-1],v[j-1])][arr.index(s[i][j])]]
    lastCol = [line[n] for line in s]
    colMax = max(lastCol)
    sink = [(m,s[m].index(max(s[m]))),(lastCol.index(colMax),n)][colMax>max(s[m])]
    curr = sink
    while curr[0]>0 and curr[1]>0:
        prev = d[curr][0]
        edges = d[curr][1]
        w_out += edges[0]
        v_out += edges[1]
        curr = prev
    return s[sink[0]][sink[1]], v_out[::-1], w_out[::-1]

def main():
    args = arg_parse()

    v,w = '',''
    with open(args.input) as infile:
        v,w = infile.read().splitlines()

    with open(args.output,'w') as outfile:
        outfile.write('\n'.join([str(x) for x in overlapAlignment(v,w)]))

main()