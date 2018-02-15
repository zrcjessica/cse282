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

def affineGap(v,w):
    aa, blosum = parseBlosum()
    SIGMA, EPSILON = -11, -1 #gap opening, extension penalties
    m,n = len(v), len(w)
    low = [[0]*(n+1) for row in range(m+1)]
    mid = [[0]*(n+1) for row in range(m+1)]
    up = [[0]*(n+1) for row in range(m+1)]
    v_out, w_out = '',''
    d = {} #key = (i,j), value = [(low prev, up prev, mid prev),(vals)]
    for i in range(1,m+1):
        low[i][0] = SIGMA+EPSILON*(i-1)
        mid[i][0] = SIGMA+EPSILON*(i-1)
    for j in range(1,n+1):
        up[0][j] = SIGMA+EPSILON*(j-1)
        mid[0][j] = SIGMA+EPSILON*(j-1)
    for i in range(1,m+1):
        for j in range(1,n+1):
            low[i][j] = max(low[i-1][j]+EPSILON,mid[i-1][j]+SIGMA)
            up[i][j] = max(up[i][j-1]+EPSILON,mid[i][j-1]+SIGMA)
            mid_arr = [low[i][j],mid[i-1][j-1]+blosum[aa.index(v[i-1])][aa.index(w[j-1])],up[i][j]]
            mid[i][j] = max(mid_arr)
            idx = mid_arr.index(mid[i][j])
            d[i,j] = [[(i-1,j),(i-1,j-1),(i,j-1)][idx], \
                      [(v[i-1],'-'),(v[i-1],w[j-1]),('-',w[j-1])][idx]]
    curr = m,n
    while curr[0]>0 and curr[1]>0:
        edge = d[curr][1]
        v_out += edge[0]
        w_out += edge[1]
        curr = d[curr][0]
    stop = list(curr)
    while stop[0]>0:
        v_out += [v[stop[0]-1],'-'][int(stop[0]==0)]
        w_out += '-'
        stop[0] += -1
    while stop[1]>0:
        w_out += [w[stop[1]-1],'-'][int(stop[1]==0)]
        v_out += '-'
        stop[1] += -1
    return mid[m][n], v_out[::-1], w_out[::-1]

v,w = open('rosalind_ba5j.txt').read().splitlines()
print('\n'.join([str(x) for x in affineGap(v,w)]))