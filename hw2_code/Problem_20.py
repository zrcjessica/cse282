import argparse
import random

def arg_parse():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('input', help='input filehandle')
    parser.add_argument('output', help='output filehandle')
    return parser.parse_args()

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
        

def ProfileRanGenKmer(text,k,profile):
    idx = {'A':0,'C':1,'G':2,'T':3}
    kmers = []
    probs = []
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        cumprod = 1
        for j in range(k):
            cumprod = cumprod*profile[idx.get(kmer[j])][j]
        probs.append(cumprod)
        kmers.append(kmer)
    c = sum(probs)
    distribution = [x/c for x in probs]
    out = random.choices(kmers, weights=distribution)
    return out[0]

def GibbsSampler(Dna,k,t,N):
    motifs = []
    for seq in Dna:
        start = random.randint(0,len(seq)-k-1)
        motifs.append(seq[start:start+k])
    bestMotifs = motifs
    for iteration in range(N):
        i = random.randint(0,t-1)
        motifi = motifs.pop(i)
        profile = laplace(motifs)
        motifs.insert(i,ProfileRanGenKmer(Dna[i],k,profile))
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs
    return bestMotifs

def RepeatGibbs(Dna,k,t,N):
    d={}
    for i in range(20):
        bestMotifs = GibbsSampler(Dna,k,t,N)
        motifsScore = score(bestMotifs)
        d[motifsScore]=bestMotifs  
    return d.get(min(list(d.keys())))

def main():
    args = arg_parse()

    dataset = []
    with open(args.input) as in_fh:
        dataset = in_fh.read().splitlines()
    k,t,N = [int(x) for x in dataset[0].split()]
    dna = [dataset[i] for i in range(1,len(dataset))]

    with open(args.output,'w') as fh:
        fh.write('\n'.join(RepeatGibbs(dna,k,t,N)))
main()