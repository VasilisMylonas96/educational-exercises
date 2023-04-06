def permutation(lst):
    k2=[]
    for i in range (len(lst)):
        for j in range (len(lst)):
            k=lst[:]
            k1=k[j]
            k[j]=k[i]
            k[i]=k1
            if not(k in k2):
                k2.append(k)
    return k2
l=int(input('GIVE ME ONE NUMBER:'))
L=[]
for i in range (1,l+1):
    L.append(i)
L1=permutation(L)
print(L1)
den exei oloklirothei
