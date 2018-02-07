import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

def editDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    d = [[0]*(n+1) for row in range(m+1)]
    for i in range(1,m+1):
        d[i][0]=i
    for j in range(1,n+1):
        d[0][j] = j
    for j in range(1,n+1):
        for i in range(1,m+1):
            substitution = int(str1[i-1] != str2[j-1])
            d[i][j] = min([d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+substitution])
    return d[m][n]

def main():
    args = arg_parse()

    data = []
    with open(args.input) as infile:
        data = infile.read().splitlines()
    s = data[0]
    t = data[1]

    with open(args.output,'w') as outfile:
        outfile.write(str(editDistance(s,t)))

main()