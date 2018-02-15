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

AA, BLOSUM = parseBlosum()
SIGMA = -5 #indel penalty

def fromSource(v,w):
    m,n = len(w),len(v)
    left = [[0]*(int(m/2)+1) for row in range(n+1)]
    for i in range(1,n+1):
        left[i][0] = i*SIGMA
    for j in range(1,int(m/2)+1):
        left[0][j] = j*SIGMA
    for i in range(1,n+1):
        for j in range(1,int(m/2)+1):
            left[i][j] = max(left[i-1][j]+SIGMA,left[i][j-1]+SIGMA, \
                             left[i-1][j-1]+BLOSUM[AA.index(v[i-1])][AA.index(w[j-1])])
    midCol = [left[x][int(m/2)] for x in range(n+1)]
    return midCol
             
def middleNode(v,w):
    midFromLeft = fromSource(v,w)
    midFromRight = fromSource(v[::-1],w[::-1])
    length = [x+y for x,y in zip(midFromLeft,midFromRight[::-1])]
    return length.index(max(length)), int(len(w)/2) #i,j of middle node

def middleEdge(v,w):
    midCol = fromSource(v,w)
    start = middleNode(v,w)
    nextCol = [SIGMA*int(len(w)/2+1)]
    for i in range(1,len(v)+1):
        nextCol.append(max(nextCol[i-1]+SIGMA,midCol[i]+SIGMA, \
                           midCol[i-1]+BLOSUM[AA.index(v[i-1])][AA.index(w[int(len(w)/2)])]))
    return start, (nextCol.index(max(nextCol)),int(len(w)/2)+1)

v,w = open('rosalind_ba5k.txt').read().splitlines()
print(' '.join([str(x) for x in middleEdge(v,w)]))