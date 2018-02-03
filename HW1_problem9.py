def PatternToNum(Pattern):
    dna = ['A','C','G','T']
    if len(Pattern) == 0:
        return 0
    symbol = Pattern[-1]
    prefix = Pattern[0:len(Pattern)-1]
    return 4*PatternToNum(prefix) + dna.index(symbol)

def NumToPattern(index,k):
    dna = ['A','C','G','T']
    if k == 1:
        return dna[index]
    prefixIndex = int(index/4)
    r = index%4
    symbol = dna[r]
    prefixPattern = NumToPattern(prefixIndex, k-1)
    return prefixPattern+symbol

def HammingDistance(p,q):
    hdist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hdist += 1
    return hdist

def ApproxPatternCount(Pattern, Text, d):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            count+=1
    return count

def FreqWordsMismatched(Text,k,d):
    freqPatterns = []
    freqCounts = [ApproxPatternCount(NumToPattern(i,k),Text,d) for i in range(4**k)]
    maxCount = max(freqCounts)
    for i in range(4**k):
        if freqCounts[i] == maxCount:
            pattern = NumToPattern(i,k)
            freqPatterns.append(pattern)
    return freqPatterns
       
FreqWordsMismatched('GGGACTCATTATTAATGCAAGATATTATTAATGGGACTCGTATCGTATTATTAATGGGACTCGGGACTCGGCTTCGAGTATCGTGTATCGTGCAAGATATTATTAATGGCTTCGAGGCTTCGAGGGACTCATTATTAATGCAAGATGGGACTCGGGACTCGGGACTCATTATTAATGCAAGATATTATTAATGCAAGATATTATTAATGGGACTCATTATTAATATTATTAATGTATCGTGTATCGTGTATCGTGGCTTCGAGCAAGATGGCTTCGAGCAAGATGCAAGATGCAAGATGCAAGATGCAAGATGGCTTCGAGTATCGTGGGACTCGGCTTCGAGCAAGATGCAAGATGGGACTCGGCTTCGAGGGACTCGGCTTCGAGGCTTCGAGCAAGATGGGACTCGTATCGTGGCTTCGAGGCTTCGAGGCTTCGAGTATCGTGCAAGATGTATCGTGTATCGTGGGACTCGCAAGATGGCTTCGAGTATCGTGGGACTCATTATTAATGGCTTCGAATTATTAATGGCTTCGAGGCTTCGAGGGACTCGGCTTCGAGGCTTCGAGCAAGATGGCTTCGAATTATTAATGTATCGTGCAAGATGTATCGTGGGACTCGCAAGATATTATTAATGCAAGATATTATTAATGTATCGTGGGACTCATTATTAATGGGACTCGGGACTCGTATCGTGGGACTCATTATTAATGCAAGATGTATCGTGCAAGATGTATCGTGGCTTCGAATTATTAATGCAAGATGGCTTCGAGGCTTCGAGTATCGTGCAAGATGTATCGTGGGACTCGGGACTCGCAAGATGGCTTCGAGTATCGTATTATTAATATTATTAATGCAAGATGGCTTCGAGCAAGATGCAAGAT',5,3)
