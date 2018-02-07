import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

def outputLCS(backtrack,v,i,j):
    string = ''
    while i>0 and j>0:
        if backtrack[i][j] == 's':
            i = i-1
        elif backtrack[i][j] =='e':
            j = j-1
        else:
            string += v[i-1]
            i = i-1
            j = j-1
    return string[::-1]

def lcsBacktrack(v,w):
    backtrack = [['']*(len(w)+1) for row in range(len(v)+1)]
    s = [[None]*(len(w)+1) for row in range(len(v)+1)]
    for i in range(len(v)+1):
        s[i][0] = 0
    for j in range(len(w)+1):
        s[0][j] = 0
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            arr =[s[i-1][j],s[i][j-1]]
            if v[i-1] == w[j-1]:
                arr.append(s[i-1][j-1]+1)
            s[i][j] = max(arr)
            backtrack[i][j] = ['s','e','se'][arr.index(s[i][j])]
    return backtrack

def main():
    args = arg_parse()

    data = []
    with open(args.input) as infile:
        data = infile.read().splitlines()
    v = data[0]
    w = data[1]

    backtrack = lcsBacktrack(v,w)
    with open(args.output,'w') as outfile:
        outfile.write(outputLCS(backtrack,v,len(v),len(w)))

main()