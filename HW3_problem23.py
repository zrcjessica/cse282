def CompositionK(k, text):
    kmers = []
    for i in range(len(text)-k+1):
        kmers.append(text[i:i+k])
    return sorted(kmers,key=str.upper)

CompositionK(50,'CAAGTCGCTCGAATCGAGGTGGACAAGTACTCATGGATGCGTTCACAGTAATCGCATTGTTGCAAGGGGAGCTCTTGAAACCGAAACTTCACCGAGCCGCGTACGACGACTGACCGAGCCGCCACGCGATACCACGTCTCCGGCGCGAGGCATACCTAAGCGAGAGATGAGTATGAACAGCTCGGACCCAACCTGTGCAGCCGTCTCCGTTACTGACTGATCGGGAAGGCTATGTGATCCTAGCGTATGCGATTGCGTGAGCTCGGACTTGGTGTGGAGAGAATAATTCGTATGTTGGAATGATCTCCCTCTCGGGGAAGCTCGCTCTCGTCAGCTGGACGAGGTGAGAAACAGTAACTTACCACCGGGTGTCCCGATCTCAATAGTTCCTTTAGAAACTGTTCTATTCCATCAGCACGGTATCTGGCGACATTCGCGAGTGCCGACTGCGTGTCTCGGCGACTCGTCCAACGTGATATTAAGGTAAGGTGGGACTGTGCGCCTGCGGGAAAATCAAGATCTAATGCCTCCCTGAAGGAACTACAAAGGGGTTTTCGTCACTACTTGGACTACGGCCAACCTGTAAAACCGGAAGATAGCTCCATAGCCTGGCCCTGAATGCGCCTTATGCGATTTAATACCCATTGCTCGCTGCAATAGCAGCTGATCACCACTGGGATTTACTATAACATCCGTGTCGTCGTCACGGTGTTGAGTCCCAGATCAAGCGCCGAATATTATGCGATAATTGGTCGGGAAGCCCCTGCTTGGTCTCAAAACATACTTAGTAGGAAATCTTGTTAACTCCTGGGGAGCGGGGTGATTATAATTCGCAACGCACGGTATTACTGCTGGTTGCATGTAATTCCTGGCCTTCCCGACGCAGGGCCTTAAAGATAGGCCGCATATAGGGGCTCCCGCTAGGTTTAGGTGTAGTTCTACCTAGCTGGAGACGCCACATTCGATTAGTCAGCATACCTGAGATACTGTACACGTCTAT')
