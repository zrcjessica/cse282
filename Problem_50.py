def parsePermutation(p):
    stripped = p.replace('(','').replace(')','').replace('+','')
    return [int(x) for x in stripped.split()]

def kSortingReversal(p,k):
    p_abs = [abs(x) for x in p]
    end = p_abs.index(k+1)
    p[k:end+1] = [-1*x for x in p[k:end+1][::-1]]
    return p

def greedySorting(p):
    approxReversalDist = 0
    reversals = []
    for k in range(len(p)):
        if p[k] != k+1:
            p = kSortingReversal(p,k)
            reversals.append(p.copy())
            approxReversalDist += 1
            if p[k] == -(k+1):
                p[k] = -1*p[k]
                reversals.append(p.copy())
                approxReversalDist += 1
    return reversals

input_perm = '(+86 +110 +93 +61 -35 -119 +121 -68 -22 +113 +25 +141 -98 +48 +123 +118 -31 +12 -6 -97 -4 -126 +20 +132 +122 +62 +106 +41 -40 -69 +5 +34 -117 -28 +73 -139 +58 -133 -52 +142 -66 +42 +65 +109 +49 +72 +33 +37 +63 +94 -46 +87 +64 +103 -27 -80 +85 -70 +111 +19 -39 +51 +125 -7 -26 -71 +55 -145 -135 -2 -76 -24 +88 -104 -23 +21 -108 -11 +83 -43 -131 +124 +45 -53 +77 -81 -16 -18 +90 +13 +144 +15 +92 -95 -78 +30 +75 -17 -101 +102 +130 +140 +79 -57 +89 -82 +74 -54 +138 +8 -38 +14 -99 +137 -36 +96 -134 -136 -32 +56 -9 +29 +129 +91 +114 +59 -44 +127 -60 -128 -105 -116 +3 +115 -67 +50 +100 +112 -1 -10 -120 +84 -107 +143 +47)'
data = parsePermutation(input_perm)
output = greedySorting(data)
for line in output:
    reversal = '('
    for i in range(len(line)):
        if line[i]>0:
            reversal += '+' + str(line[i])
        else:
            reversal += str(line[i])
        if i != (len(line)-1):
            reversal += ' '
    reversal += ')'
    print(reversal)