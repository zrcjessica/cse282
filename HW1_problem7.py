def HammingDistance(p,q):
    hdist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hdist += 1
    return hdist

HammingDistance('TCTTTGTATCATAAGGGTTAGGCCCGCCCGGCTAGGCCTATAACTCCAGGCAGCGTAACTAGGGCCACTCCTCCTTTGGGTCTAACACGGTTGAGACCCTGTTTGCAATAAAGATTGTTGGGGTCAAAACAACTTATGTATGTAGGGCCCTTCGCTACCGTGCTGGTGTTCCCGAGGCACTACGTACGCTGACTGGATGCAGTCTCAGTATTCGACCAAGGGTGTACGAAGGATACTATAACCGAGAAGATTAGTCTTAGTATAAGGTTCGACCCGGCGGAAAGTATCTCTGCCAGGGTTGGCTAGTACCCGCGAGCATACCACAAAGATGTACCAAAGCTGATCTGAAGTTCGTATTTGGGTGGCGTACTCTGGCGGGAAGGCGATGGTTTTACGTATCCCCGACTGTGTTGGATATTCAAAGTTAGTCACCCTTATTGTTCGGTAAAAAACATCAGTGTTGGCTACTTCGAAAACCAATGCTGGTATGCCGATTGCTGTGAAGGCTGCCAGTGTTTATCTAATCTTTGATTCAACATCTATGTTTTTTGTCTACCCTAATCTCCACTCATTTCGGTAGAGACGTGAAAGCCTCATGAGCGGGGTTGGGAAGGATCAAGCAGAAGGGGGGGCCCGTAGCAGCGGCATGGGATCATACTTTCAGAGAATCGTCTCGTACCAGAGCATCTCCCAAGGTCTAATCTTGCACTCAATAAGCTGTAGGCACACAGAACGGAGTGCAACCCAATTCGCGGACCGAGAGGGCCCCGCCGACCTCCGTTACAATTATTCTGCCTATGGCCACCGGCAATCAAAATGCTGATACCCGAGTAGACCGGAAGACCCCGAGAGAAGCTGGGCGAATACTGGTCACTTAAGAATGTGTCTATCAACCAGAAGCAGGGTGGATCGCCCCACCAGGGGGGGAATAAACCGTCGCTCAAACGCGAAACCGTCATAGCATTTTGGGCCTTGGGTCACTAGCCCATGTATCTAGCCAGCTCGTTTGCGTTCACGGAGCTGGCACGGCAAATCAAGGTA', 'TGGTGGCAACCTATTGCTCCGGATACATTCGCCGTCAGAGAACCTGAGTGTTCATTATCATGTAGCCGGTCCTGGAGAGTCCGCTCCCTGCAGAGGTCCATGCGGAGTAAATTAGTACACTCACTAATTGTGGAATCTTATTTCAACTTGCAAAGTAAGGTTATGGATCGCCCACCCCCTCGTGCGGTCTCCCGACCCCGGGACAAGCCCATGTGATGAGGTATGGGATGAAAGATTGCACGCAACCTGAGGCATTACCCGCTGTCGGATCGTTCCTAGAGATTAAAGGCCACACATAAACAATGTCGAAATCACCATTCAGTACAACGATGCCGGGCTATGAGACCCGACCCTATAATTGGGTCGGAACTGGATAGTCCAGGAGACGGCCACGTACGGAAGGTAAAGCTTCGTATGCGTCGATGAAGAGCTCGCCGATCGGACTGGGGTTTCTTGACCATCCCCGATAAAATCCAACAGCGGCGAGGGGGGCCATAAAGTGCGTGAGGGCTAGCCCCTCGTGCGAAGTCAGATCGCCCGGCTCGATGCTGGGTCTCTGCTGTTACTACTGTGTCTCAAAGGGTGATCGGCCGAAAACGACCATCTAAAATTATCAGTTAGTAGCGTAACGATGTACTAGGTATTTTGTCAAGTTTGGCATGTTCGTGGCAAGCGAGGCGGTCTAGTCCTTTGTTTTGCAATAGGCCCTCTAACCACTGGTGCAACGCACTCGTGTTTCCACAGACGGTCTGGATCAGACTCGCATAGAACCGTTGGCTCAGGTCCCGAGGGTCGAGCGCTTCCAGCTATCCGTCGCTGTTTAAATGTCCCGCTGAAACTAAGGCTGATAAAGCCCCCGTGCCAGCTCGTAAGTACTCGACGCCTTTTTGACTTCGTCCTTGTCCTAGCGGTCGTATATTTCACCGATTAGCAGACTCATGCTAATTTAACTTCAAGAGGGCCGAGATTTCCGGGTCGGCTGGTTACCTGATTACGGCTCGGGTAGTGTGATTTTCCGTTCGGCAGATCGACTCATTTTAA')