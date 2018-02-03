def PatternToNum(Pattern):
    dna = ['A','C','G','T']
    if len(Pattern) == 0:
        return 0
    symbol = Pattern[-1]
    prefix = Pattern[0:len(Pattern)-1]
    return 4*PatternToNum(prefix) + dna.index(symbol)

PatternToNum('CTCGACGCCGGCCTCAGATGGTAAAGAGTG')
