import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

def parseBlosum():
    aa = 'A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y'.split()
    m = ''' 4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
         0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
        -2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
        -1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
        -2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
         0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
        -2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
        -1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
        -1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
        -1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
        -1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
        -2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
        -1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
        -1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
        -1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
         1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
         0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
         0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
        -3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
        -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7'''.split()
    blosum = []
    while len(m):
        blosum.append([int(x) for x in m[:20]])
        del m[:20]
    return aa,blosum

def globalAlignment(str1,str2):
    aa, blosum = parseBlosum()
    SIGMA = -5 
    out_str1 = ''
    out_str2 = ''
    d = {}
    m = len(str1)
    n = len(str2)
    s = [[0]*(n+1) for row in range(m+1)]
    for i in range(1,m+1):
        s[i][0] = SIGMA*i
    for j in range(1,n+1):
        s[0][j] = SIGMA*j
    for j in range(1,n+1):
        for i in range(1,m+1):
            mismatch = blosum[aa.index(str1[i-1])][aa.index(str2[j-1])]
            arr = [s[i-1][j]+SIGMA, s[i][j-1]+SIGMA, s[i-1][j-1]+mismatch]
            s[i][j] = max(arr)
            prev_coord = [(i-1,j),(i,j-1),(i-1,j-1)][arr.index(s[i][j])]
            d[i,j] = [prev_coord,[[str1[i-1],'-'],['-',str2[j-1]],[str1[i-1],str2[j-1]]][arr.index(s[i][j])]]
    curr = m,n
    while curr[0]>0 and curr[1]>0:
        prev = d[curr][0]
        edge = d[curr][1]
        out_str1 += edge[0]
        out_str2 += edge[1]
        curr = prev
    stop = list(curr)
    while stop[0]>0:
        out_str1 += [str1[stop[0]-1],'-'][int(stop[0]==0)]
        out_str2 += '-'
        stop[0] += -1
    while stop[1]>0:
        out_str2 += [str2[stop[1]-1],'-'][int(stop[1]==0)]
        out_str1 += '-'
        stop[1] += -1
    return s[m][n],out_str1[::-1],out_str2[::-1]

def main():
    args = arg_parse()

    s,t = '',''
    with open(args.input) as infile:
        s,t = infile.read().splitlines()

    with open(args.output,'w') as outfile:
        outfile.write('\n'.join([str(x) for x in globalAlignment(s,t)]))

main()