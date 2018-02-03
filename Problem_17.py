import argparse

def arg_parse():
	parser = argparse.ArgumentParser(description='Process input and output files.')
	parser.add_argument('input', help='input filehandle')
	parser.add_argument('output', help='output filehandle')
	return parser.parse_args()

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

def consensus(motifs):
    consensus = ''
    profile = getProfile(motifs)
    d = {0:'A',1:'C',2:'G',3:'T'}
    for i in range(len(profile[0])):
        column = [seq[i] for seq in profile]
        mostFreq = column.index(max(column))
        consensus = consensus + d.get(mostFreq)
    return consensus

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
    
def GreedyMotifSearch(k,t,Dna):
    BestMotifs = [seq[0:k] for seq in Dna]
    for i in range(len(Dna[0])-k+1):
        motif0 = Dna[0][i:i+k]
        motifs = [motif0]
        for j in range(1,t):
            profile = getProfile(motifs)
            new_motif = ProbableKmer(Dna[j],k,profile)
            motifs.append(new_motif)
        if score(motifs) < score(BestMotifs):
            BestMotifs = motifs
    return BestMotifs

def main():
	args = arg_parse()

	dataset = []
	with open(args.input) as in_fh:
	    dataset = in_fh.read().splitlines()
	k,t = [int(x) for x in dataset[0].split()]
	dna = [dataset[i] for i in range(1,len(dataset))]

	with open(args.output,'w') as fh:
	    fh.write('\n'.join(GreedyMotifSearch(k,t,dna)))
main()