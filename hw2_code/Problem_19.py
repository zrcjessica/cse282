import argparse
import random

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

def HammingDistance(p,q):
    hdist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hdist += 1
    return hdist

def score(motifs):
    popular = consensus(motifs)
    cumsum = 0
    for seq in motifs:
        cumsum += HammingDistance(popular,seq)
    return cumsum

def ProbableKmer(Text, k, Profile):
    dna = {'A':0, 'C':1,'G':2,'T':3}
    probableKmers = {}
    for i in range(len(Text)-k+1):
        kmer = Text[i:i+k]
        cum_prod = 1
        for j in range(k):
            cum_prod = cum_prod*Profile[dna.get(kmer[j])][j]
        probableKmers[kmer] = cum_prod
    return max(probableKmers, key=probableKmers.get)

def getMotifs(profile,dna,k):
    out = []
    for seq in dna:
        out.append(ProbableKmer(seq,k,profile))
    return out

def laplace(motifs):
    d = {'A':0,'C':1,'G':2,'T':3}
    counts = [[0]*len(motifs[0]) for n in range(4)]
    for seq in motifs:
        for i in range(len(seq)):
            counts[d.get(seq[i])][i]+=1
    for i in range(4):
        for j in range(len(counts[0])):
            counts[i][j]+=1
    profile = [[0]*len(motifs[0]) for n in range(4)]
    for i in range(4):
        for j in range(len(motifs[0])):
            profile[i][j] = counts[i][j]/sum([counts[x][j] for x in range(4)])
    return profile

def consensus(motifs):
    consensus = ''
    profile = getProfile(motifs)
    d = {0:'A',1:'C',2:'G',3:'T'}
    for i in range(len(profile[0])):
        column = [seq[i] for seq in profile]
        mostFreq = column.index(max(column))
        consensus = consensus + d.get(mostFreq)
    return consensus

def getProfile(motifs):
    d = {'A':0,'C':1,'G':2,'T':3}
    counts = [[0]*len(motifs[0]) for n in range(4)]
    for seq in motifs:
        for i in range(len(seq)):
            counts[d.get(seq[i])][i]+=1
    profile = [[0]*len(counts[0]) for n in range(4)]
    for i in range(4):
        for j in range(len(profile[0])):
            profile[i][j] = counts[i][j]/len(motifs)
    return profile
        
def RandomizedMotifSearch(Dna,k,t):
    motifs = []
    for seq in Dna:
        start = random.randint(0,len(seq)-k-1)
        motifs.append(seq[start:start+k])
    bestMotifs = motifs
    while True:
        profile = laplace(motifs)
        motifs = getMotifs(profile,Dna,k)
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs
        else:
            return bestMotifs
        
def RepeatRandomizedMotifSearch(Dna,k,t):
    d={}
    for i in range(1000):
        bestMotifs = RandomizedMotifSearch(Dna,k,t)
        motifsScore = score(bestMotifs)
        d[motifsScore]=bestMotifs
    return d.get(min(list(d.keys())))

def main():
    args = arg_parse()

    dataset = []
    with open(args.input) as in_fh:
        dataset = in_fh.read().splitlines()
    k,t = [int(x) for x in dataset[0].split()]
    dna = [dataset[i] for i in range(1,len(dataset))]

    with open(args.output,'w') as fh:
        fh.write('\n'.join(RepeatRandomizedMotifSearch(dna,k,t)))
main()