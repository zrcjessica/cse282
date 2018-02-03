def overlapGraph(patterns):
    adjacency = {}
    patterns = sorted(patterns,key=str.upper)
    for i in range(len(patterns)):
        kmer = patterns[i]
        suffix = kmer[1:]
        for j in range(len(patterns)):
            if i!=j:
                prefix = patterns[j][:-1]
                if prefix==suffix:
                    adjacency.setdefault(kmer,[]).append(patterns[j])
    return adjacency

in_patterns=[]
with open('rosalind_ba3c.txt') as in_file:
    in_patterns = in_file.read().splitlines()
output = overlapGraph(in_patterns)
for x in output.keys():
    print(x + ' -> ' + ','.join(output[x]))