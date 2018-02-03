def reconstructFromPath(patterns):
    text = patterns.pop(0)
    for kmer in patterns:
        text += kmer[-1]
    return text

patterns=[]
with open('rosalind_ba3b.txt') as in_file:
    patterns = in_file.read().splitlines()
reconstructFromPath(patterns)
