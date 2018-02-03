def PatternMatching(Pattern, Genome):
    startPos = []
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            startPos.append(i)
    return startPos

PatternMatching('CTTCTCACT', 'CTCCTTCTCAGACGTGCACTTCTCACAGGTCTTCTCAGCTTCTCACTTCTCAGCTTCTCACTTCTCAATCTTCTCACCCCGCTTCTCACTTCTCACTCTTCTCACATCCCTTCTCAACTTCTCAGCTTCTCACTTCTCACTTCTCACATACTTCTCACAGTCTTCTCAGGCTTCTCATTTATATCTTCTCACTTCTCACTTCTCAAATACGTCTTCTCATCTTCTCACCTTCTCAGTCTTCTCATGGGAGCTTCTCATGGTCCTTCTCACTTCTCAGTACTTCTCAAAACCTTCTCAACGCTCTTCTCACTCTTCTCAGATCTTCTCATCTTCTCAATGACACTTCTCACTTCTCACACTTCTCAACAACTTCTCACTTCTCACACTCTTCTCAGGGCGGATGCTTCTCACTTCTCATCAACGTCTTCTCACTTCTCACTTCTCACCTTCTCACTTCTCACTTCTCACTTCTCAGCCTTCTCAAATCTTCTCACTTCTCATCCGTCTTCTCACCCTTCTCACTTCTCATCTTCTCACTTCTCATCTTCTCATCCTTCTCATGTACTTCTCATACTTCTCAGCTTCTCACACTTCTCAACCTTCTCAGCTTCTCACTTCTCAAGGCTTTTTATCGAACGGCTTCTCACTTCTCAGACTTTAATTTCTTTCTTCTCACGCTCTTCTCACTTCTCATTTGACTTCTCATGGCTTCTCAAGTTTTTCTTAACCTTCTCACTTCTCAATCTTCTCACTTCTCAGCTTCTCACCTTCTCAGCTCAAAACCTTCTCAATCTTCTCACTTCTCACCTTCTCACCACCTTCTCACAGACTCTTCTCATCACTTCTCACCTTCTCATGCCCTTCTTCTCAGACTTCTCAAATCTTCTCACTTCTCACAGCCTTCTCACCGTTGGTCTTCTCACGCTTCTCACTTCTCACTTCTCATACCTTCTCACTTCTCACTGCTTCTCACTTCTCACTTCTCACTTCTCATGGTCTTCTCAAGACTTCTCATCTTCTCAGGCCTTCTCACCCCTTCTCATGCCTTCTCACTTCTCACTTCTCAGAGGCGCTTCTCACCTTCTCAGTGTCTTCTCACTTCTCACTTCTCAGACCAGCTTCTTCTCAGGACAGCTTCTCATACGACTTCTCATGTTCTTCTCACTTCTCACTTCTCACCCTTCTCATCTTCTCACCTTCTCACTTCTCACTTCTCATACCCACTTCTCACTTCTCACCTTCTCACCGTACTTCTCACTTCTCACTTCTCACTTCTCAAATTACTTCTCAGTGTCTCCCTTCTCATCTTCTCACTTCTCAAAACTTCTCATCTTCTCATGAACTTCTCACTTCTCATCTTCTCAATACATCTTGCTTCTCACACTTCTCATCCTTCTCATGGGAGCTTCTCACTTCTCACAGTGTCTTCTCAGGCTTCTCACTTCTCAACTTCTCAACTTCTCACTTCTCAGTACCCTTCTCACTTCTCAGCTTCTCAGGTCTTCTCATGCTTCTCATTTACACCTTCTCATTTCTTCTCAGGGCTTCTCAGTGACTTCTCAGTTCCTTCTCATCTTCTCAACTTCTCATCTTCTCACTTCTCAGCTTCTCAACCTATAGGCTTCTCACCTGGGTCTTCTCAAGACTTCTCATAGCTTCTCAAAGAGGTCTTCTCACCTTCTCAGTAACTATACTTCTCAGATCGTATGGCTTCTCATTCTTCTCAACGCTTCTCATCCTTCTCACTTCTCAAGCCTTCTCACCTTCTCAAGGCTTCTCATTCTTCTCACTTCTCACTTCTCAGCCTTCTCACTTCTCACACTTCTCAGCTTCTCACTTCTCACCTTCTCAACTTCTCAGTTCTGCAACCTTCTCATCTTCTCACTTCTCACGTCTTCTCAGGGCTCAGTCTTCTCAGCCTTCTCAAGCCTTCTCATCTTCTCAACTTCTCAGACCTTCTCACAACTTCTCATCTTCTCATGCTTCTCATCTTCTCATAAGCCTTCTCAGTTAAGCTTCTCACTACTTCTCACCTCTTCTCACTTCTCACTTCTCAACTCTTCTCACCTTATCTTCTCATCTTCTCAATTGTCTTCTCAAGTGCCTTCTCAGTCCTTCTCACTTCTCACTTCTCATAGTTGCCTGCTTCTCAGGAATCACCCTTCTCACCCTCTTCTCAACACTCTTCCTTCTCACCTTCTCATACTTCTCACTTCTCACGCTTCTCATTCTTCTCAAAACAATTCTTCTCACTTCTCAAACAGCCTTCTCAACGCTTCTCAATGCTTCTCACTTCTCAACTTCTCAACTTCTCAGCCCCTTCTCAAAGTCTTCTCATCTTCTCACTTCGGTGGTGGCACTACTTCTCACTTCTCAAGAGGGTCTTCTCACTTCTCAATCTTCTCATAGCCCGTATCCTCTTCTCAGGCCTTCTCAATCCACTTCTCAGACGCTTAGCGATTTCTTCTTCTCACCTTCTCAGTGGATTACTTCTCAAGGAGACTTCTCAACTTCTCAACTTCTCAGGCTTCTCATTACGTCTTCTCACTTCTCACTTCTCAAATCCTTCTCAATTAGCTTCTCATTCACTTCTCACTTCTCACCATTTCTTCTCACAAGGAACTTCTCACTTCTCATCAACTTCTCAGCCTTCTCAGCTTCTCACTTCTCACCTTCTCACCCTTCTCAGCTTCTCACTTCTCACTTCTCACTCTTCTCAGATAGCTTCTCAACCCGAACTAAACTTCTCATACTTCTCATTCTTCTCACTTCTCACTTCTCACCTTCTCAAAGCCTTCTCACTTCTCAATCTTCTCATCTTCTCAGCTCGGCGGCTTCTCACACAGAGTCTCTTCTCATCTTCTCACCCTTCTCAGCTCTTCTCAGCTTCTCATGTCTTCTCATACTACACTTCTCACACTTCTCACTTCTCATCGTCCGTCTTCTCACTTCTCAACTTCTCAGGGCCTTCTCACCTTCTCACTTCTCAGACCTTCTCAGCCTTCTCACCGTAATCTTCTCACTTCTCACTTCTCACCTTCTCACTTCTCACTTGTCTTCTCAACTTCTCAATCACCTGTAACCCACTTCTCACGCTGCTTCTCAGCCTTCTCACCATTATTTCTTCTCACCCTTCTCACTTCTCAGTATCAACCTTCTCAAACTTCTCATGGTACCTTCTCACTTCTCACGACTTCTCACACTTCTCACCTTCTCAGTCTTCTCAACTTCTCAGGGTGCTTCTCAGCTTCTCACTTCTCACTTCTCAGCTGGAGCACTTCTCAAAGCGTGTCTTCTCACCATCATTCTTCTCACACGATACTTCTCATCGCTTCTCACTTCTCATGGCTCTTCTCAATGCTTCTCATGATCGGCATCTTCTCATATGCCTTCTCACTTCTCATGGCACAGCTTCTCATAACCTTCTCAGCTTCTCAACGCCTTCTCAGAGGGCTTCTCAAAGAGCGACCTTCTCACTTCTCAGCTTCTCAAGTCGACTTCTCACTTCTCATTCTTCTCAAGTAACTTCTCACTTCTCACTTCTCAAGCCCCGACTTCTCAGGCACTCCACTGCTTCTCATCAGCTTCTCAAAGCCTTCTCAACTTCTCACCTTCTCATCTTCTCAACTTCTCAAGACCTTCTCACTTCTCAACTTCTCAACTTCTCACTTCTCACGGAACTTCTCAGTGCTTCTCAGACCTTGTCTCTTCTCATCGCTTCTCAAGTCCGAGCTTCTCAAACGTCTTCTCAGCCTTGCTTCTCAGTAGCCTTCTCAACTTCTCACTAACTAGCTTCTCACGCTTCTCAGTTTTGCCTCTCTTCTCACTTCTCACTTCTCACTTCTCATACTCCTTCTCACTCCACTTCTCACTCGCTTCTCACTTCTCAGCTTCTCAGCTTCTCAGGCTTCTCACTTCTCATGCTTCTCAGAAACCTTCTCATCTTCTCACTTCTCATTGAGCCTTCTCACTTCTCATTCTTCTCACTTCTCACTTCTCACCTTCTCAAGTCCCGCCTCAACTTCTCATCCTTCTCACTTCTCAACCTTCTCATAACTTCTCATATCTTCTCAGCGGCTTCTCAGAGGGCTTCTCACGTCTTCTCACTTCTCATTGATAGTTTTCCACTTCTCACCTTCTCACCTTCTCACTTCTCAATCTTCTCACTTCTCACTTCTCAGTGCTTCTCAGCGAACGCTTCTCAGCCCCTTCTCATCTTCTCATGCTTCTCACTTCTCATAGTCTCGGCTTCTCAACTTCTCAACACTTCTCACTTCTCAAACCTTCTCACTTCTCAAACTTCTCAGCTTCTCAGCTTCTCACTTCTCACTAGTGCTTCTCACTTCTCATCTCACTTCTCAGGGCCTTCTCACTTCTCACTCCTTCTCACTTCTCACCTTCTCACTTCTCACGCTTCTCACTTCTCACTTCTCAAGATGCCTTCTCACCTTCTCATGAAAATCTTCTCATCTTCTCATCTTCTCAAGATCTACAGCTTCTCAGTCTTCTCATGGGTCTTCTCACTTCTCACTTCTCACGCTTCTCACTCCTTCTCAGGGAGCTTCTCAGATGTAATCTTCTCACTTCTCACGCCCTTCTCACTTCTCATGGCCGTGCTTCTCAACCTCGCTTCTCACAAACTCCTTCTCATGCCTTCTCACTGAGCTTCTCACAACTTCTCACTTCTCACCCTTCTCATCCTTCTCACATCTTCTCACTTCTCACTTCTCATCCCGCTTCTCATCTTCTCACTTCTCACTTCTCATAGTGGCTTCTCACTTCTCACTTCTCACTTCTCACTTCTCACTGCCTTCTCATCTTCTCACCTTCTCAAACTTCTCACTTCTCACCTTCTCACCTTCTCATACAATGGCTCTTCTCATCCTCCTTCTCACTTCTCATCCTTCTCATGACTTCTCACCTTCTCAACCTTCTCACTTCTCAGGCTTCTCACTTCTCAGTCGGTCTTCTCATCTTATCTTCTCACCACTTCTCATCTTCTCACACCTTCTCAAGCTTCTCACTTCTCAGCTTCTCACCTTCTCATTTCTTCTCACCAAGTCTTCTCACTTCTCAAGCTTCTCACTTCTCAACGATATCCCCTTCTCACCCGACTTCTCATCTTCTCACTTCTCATCTTCTCAACTTCTCAGCAAGTGGCACTTCTCAATCTTCTCATAACTACTTCTCACACATGTACTTCTCAACTTCTCACTTCTCATCGGATCAAGGGAGCATAACTTCTCAATCACTTCTCACTTCTCACTTCTCATACTTCTCACTTCTCAGACTCTTCTCACTTCTCACCCTTCTCACCGACCTTCTCACTTCTCATACCCACACCTTCTCACAAACCCTGGGGTAGGACTTCTTCTCACCCTTCTCAGCTTCTCACTTCTCAACTTCTCAGCCGCACTAACTTCTCACTTCTCACGTTTCTTCTCATCTTCTCACTTCTCAGACTTCTCAGGAGAGGTCGCTTCTCAACTAATCCTTCTCACTTCTCACTAGGCTTCTCAATAGACGTCCCGATAGCTTCTCAGCTTCTCAGACCTTCTCACTATTCCTTCTCAGATCCTTCTCACTCTTCTCACCTTCTCACCTTCTCACACTTCTCATCTTCTCATTCAGCGCTTCTCAAGGTCTCTTCTCACTTCTCACTTCTCAGATTACCTTCTCACATACTCAGTGTCCCTTCTCAATACTTCTCAGCTTCTCACTTCTCAGCTTCTCACTTCTCAGGTCTTCTCAATCTTCTCACTTCTCACTTCTCACTTCTCAAACACTTCTCACCTTCTCACGGTACTTCTCAGCGGCACCTTCTCACTTCTCAGTGGACGCTTCTCACTTCTCATTCTTCTCAACGGCCCTTCTCACTTCTCACTTCTCACTTCTCAACTTCTCATACTTCTCAAATCGACTTCTCATACCTTCTCAACTTCTCAAAGCCCTTCTCACTTCTCACCTTCTCAGGAACTTCTCACATCTTCTCAGCCAACGATGGATCACGCTTCTCACTTCTCACCCTTCTCACCTCTTCTCACACTTCTCACCTTCTCAACTTCTCAACTTCTCACGGCTTCTCAATCCTTCTCACTTCTCACTTCTCACTTCTCACGCTTCTCAGAACTTCTCAGACCTTCTCATACTTCTCACCTTCTCATGACTCTTCTCAACAACTTCTCAGGTCCCCCTTCTCAAAGCTTCTCAACTTCTCACATTCCATTAACTTCTCACTTCTCACTTCTCACACTTCTCAGGTGCAAGCTTCTCAGACCTTCTCACTTCTCAATACTCACTTCTCACACCCACTTCTCAAGTGTAACCTTCTCACCTACTTCTCACTTCTCACTTCTCAACTTCTCACTTCTCAACTTCTCAGTCTTCTCATACCCTTCTCAGGCCTTCTCACTTCTCATCGCTTCTCAGACTTCTCACTTCTCAACGCGGACTTCTCACGACTTCTCAACTTCTCACTTCTCACTTCTCAATTCTTCTCATTCAATTCTTCTCAAGCTTCTCAGACTATGCTTCTCAATTTCCGATCTTCTCAGGTCGAACCTTCTCAGAACTTCTCACTTCTCAAACGAGGCTTTTCTTTCTTCTCATAGCTTGACTTCTCATGCTCTTCTCAGACTTCTCAGCTTCTCACGCTCCCGTCTTCTCATGACCTTCTCACTTCTCAAGTCTTCTCAGCTTCTCAGGGACAATTGTCGAACTACACTTCTCACTCTTCTCATTCTTCTCAGAGTCCGATTGTGGCTCTTCTCAAACTTCTCACTAGGGTGCCCTTCTCAGCTTCTCACTTCTCACTTCTCACTTCTCAACTTCTCATCTTCTCATAATGAATCTTCTCACACTTCTCAGCTTCTCACTTCTCAGACTTCTCACCTTCTCAGTCCGAGGTCTTCTCATGTTGGGCTTCTCACTTCTCAACTTCTCACTTCTCAACTTCTCATCTTCTCATGTAGGACGCTTCTCATCTTCTCACGCTTCTCACTTCTCACTTCTCACTTCTCAACCTTCTCACCACAGGCTTCTCACTTCTCACCTTCTCACTTCTCAGAACTTCTCAAGTTTTACTTCTCACCACTTCTCACTTCTCATACTTCTCAACTTCTCACCTGTCGGCCTTCTCAGATCCTTGCTTCTCACTTCTCAACTTCTCAGGGCTTTCTCTTCTCAGCTTCTCATGTTCTTCTCAGGCTTCTCATCGCACTTCTCAAACTTCTCATATCGACTTCTCACCTCCGCTACGCTTCTCAACCTTCTCAGACCCCCTTCTCAAACAGACCTTCTCACTTCTCAAGGGCTTCTCACCTTCTCAGCTTCTCAGCTTCTCAGCACTTCTCATGCAACCTTCTCATTCTTCTCAGCGTAGGAGCTTTGGCCGCCTTCTCAATCTTCTCACTTCTCACACCTTCTCAACCTTCTCACTTCTCAATCCTTCTCAGCTTCTCATCTTCTCACTTCTCATTCCTCCTTCTCAGGGCTTCTCAGACTTCTCACCTTCTCACGCTTCTCACCTTCTCAGCTTCTCATACTTCTCAAGACTTCTCACTTCTCAGGGGCTTCTCACCGTTCCTTCTCATCTTCTCACTCTTCTCACCCAGAACGCCGCTTCTCAGTCTTCTCAAACTTCTCAGCAGCTTCTCAAGCTGCGCCCTTCTCACTTCTCAGTTTCTTCTCATCTATGCGCTTCTCAGAAACTTCTCATGGCCTTCTCACTTCTCACACTTCTCAACTTCTCACCCTTCTCACTTCTCAGCTTCTCAGCCTTCTCAACTTCTCAAAAGCTTCTCATGCCGGAGCTTCTCATAAGTACTTCTCAGCTTCTCATGCTTCTCATACCTTCTCAACTTCTCACTTCTCAACTTCTCACCAACTTCTCAGTTCGTCTTCTCAGCTTCTCAGAGTATCTTCTCACTTCTCATAGCCTTCTCACTTCTCACGGATCCTTGGCTTCTCAAGGCTTCTCAGTGTAGTTCCCTTCTCAACCTTCTCACTTCTCACTTCTCATCTTCTCACCTTCTCACTTCTCAGTAGCTTCTCAGGACTTCTCATTGCTTCTCAAACATGCTTCTCAACTCTTCTCACCTTCTCAGAGTTCTTCTCAGGGCTTCTCACTTCTCAGCCACTTCTCACGCTTCTCACTTCTCAACACTTCTCAGGCCAAACTTCTCACTGCTTCTCATCTTCTCAGTCTTCTCACTTCTCAATTCTTCTCACTTCCTTCTCATCCTTCTCAACCCTTCTCACCTTCTCACCGTCTTTCGGAGTACTTCTCAGCCTTCTCAGGCCTTCTCAGTGCCTTCTCACTTCTCAATGTCAGAACTTCTCATATCTTCTCATCTTCTCAGACCTTCTCACTGGCTTCTCAACTTCTCACTTCTCAGAGCCCTTCTCAGTTCGCCTTCTCAGGGCCTTCTCATACTCCTTCTCATACTTCTCACTTCTCACAACTTCTCAGCCTTCTCAAAACG')