def HammingDistance(p,q):
    hdist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hdist += 1
    return hdist

def Neighbors(Pattern, d):
    if d == 0:
        return [Pattern]
    if len(Pattern) == 1:
        return ['A','C','G','T']
    neighborhood = []
    suffixNeighbors = Neighbors(Pattern[1:],d)
    for each in suffixNeighbors:
        if HammingDistance(Pattern[1:], each) < d:
            for base in ['A','C','G','T']:
                neighborhood.append(base+each)
        else:
            neighborhood.append(Pattern[0]+each)
    return neighborhood
    
Neighbors('TGGATAGATTT',3)
