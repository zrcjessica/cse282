import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

def parsePAM():
    aa = 'A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y'.split()
    m = ''' 2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3
        -2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0
         0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4
         0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4
        -3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7
         1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5
        -1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0
        -1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1
        -1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4
        -2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1
        -1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2
         0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2
         1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5
         0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4
        -2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4
         1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3
         1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3
         0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2
        -6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0
        -3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10'''.split()
    pam = []
    while len(m):
        pam.append([int(x) for x in m[:20]])
        del m[:20]
    return aa,pam

def localAlignment(str1,str2):
    aa, pam = parsePAM()
    SIGMA = -5 
    out_str1, out_str2 = '',''
    d = {}
    m,n = len(str1),len(str2)
    s = [[0]*(n+1) for row in range(m+1)]
    max_val = -float('inf')
    max_coord = -1,-1
    for i in range(1,m+1):
        s[i][0] = SIGMA*i
    for j in range(1,n+1):
        s[0][j] = SIGMA*j
    for j in range(1,n+1):
        for i in range(1,m+1):
            mismatch = pam[aa.index(str1[i-1])][aa.index(str2[j-1])]
            arr = [0,s[i-1][j]+SIGMA, s[i][j-1]+SIGMA, s[i-1][j-1]+mismatch]
            s[i][j] = max(arr)
            prev_coord = [(0,0),(i-1,j),(i,j-1),(i-1,j-1)][arr.index(s[i][j])]
            d[i,j] = [prev_coord,[['',''],[str1[i-1],'-'],['-',str2[j-1]],[str1[i-1],str2[j-1]]][arr.index(s[i][j])]]
            if s[i][j] > max_val:
                max_val = s[i][j]
                max_coord = i,j
            if j==n and i==m and max_coord != (i,j):
                s[i][j] = max_val
                prev_coord = max_coord
                d[i,j] = [prev_coord, ('','')]
    curr = m,n
    while curr[0]>0 and curr[1]>0:
        prev = d[curr][0]
        edges = d[curr][1]
        out_str1 += edges[0]
        out_str2 += edges[1]
        curr = prev
    return s[m][n], out_str1[::-1], out_str2[::-1]

def main():
    args = arg_parse()

    s,t = '',''
    with open(args.input) as infile:
        s,t = infile.read().splitlines()

    with open(args.output,'w') as outfile:
        outfile.write('\n'.join([str(x) for x in localAlignment(s,t)]))

main()