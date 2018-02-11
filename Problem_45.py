def mlcs(str1,str2,str3):
    m,n,o = len(str1), len(str2), len(str3)
    s = [[[0]*(o+1) for j in range(n+1)] for k in range(m+1)]
    d = {}
    backtrack = {}
    out_str1, out_str2, out_str3 = '','',''
    for i in range(1,m+1):
        for j in range(1,n+1):
            for k in range(1,o+1):
                arr = [s[i-1][j][k],s[i][j-1][k],s[i][j][k-1], \
                       s[i-1][j-1][k-1]+int(str1[i-1]==str2[j-1]==str3[k-1]), \
                      s[i-1][j-1][k],s[i-1][j][k-1],s[i][j-1][k-1]]
                align = [(str1[i-1],'-','-'),('-',str2[j-1],'-'),('-','-',str3[k-1]), \
                        (str1[i-1],str2[j-1],str3[k-1]), (str1[i-1],str2[j-1],'-'), \
                        (str1[i-1],'-',str3[k-1]),('-',str2[j-1],str3[k-1])]
                coord = [(i-1,j,k),(i,j-1,k),(i,j,k-1),(i-1,j-1,k-1), \
                        (i-1,j-1,k), (i-1,j,k-1), (i,j-1,k-1)]
                s[i][j][k] = max(arr)
                d[i,j,k] = [coord[arr.index(s[i][j][k])], align[arr.index(s[i][j][k])]]
    curr = i,j,k
    print(curr)
    while curr[0]>0 and curr[1]>0 and curr[2]>0:
        edge = d[curr][1]
        out_str1 += edge[0]
        out_str2 += edge[1]
        out_str3 += edge[2]
        curr = d[curr][0]
    print('stop:' + ','.join([str(x) for x in curr]))
    stop = list(curr)
    if stop[0]!=0 or stop[1]!=0 or stop[2]!= 0:
        while stop[0]>0:
            out_str1 += [str1[stop[0]-1],'-'][int(stop[0]==0)]
            out_str2 += '-'
            out_str3 += '-'
            stop[0] += -1
        while stop[1]>0:
            out_str2 += [str2[stop[1]-1],'-'][int(stop[1]==0)]
            out_str1 += '-'
            out_str3 += '-'
            stop[1] += -1
        while stop[2]>0:
            out_str3 += [str3[stop[2]-1],'-'][int(stop[2]==0)]
            out_str1 += '-'
            out_str2 += '-'
            stop[2] += -1
    return s[m][n][o], out_str1[::-1], out_str2[::-1], out_str3[::-1]

x,y,z = '','',''
with open('rosalind_ba5m.txt') as infile:
    x,y,z = infile.read().splitlines()
print('\n'.join([str(x) for x in mlcs(x,y,z)]))