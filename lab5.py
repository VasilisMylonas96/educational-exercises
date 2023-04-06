error=4000
x=int(input("give me one number"))
while x>=error:
 x=int(input("give me one number"))
Mapping=[[' ','I','II','III','IV','V','VI','VII','VIII','IX'],
[' ','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
[' ','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
[' ','M','MM','MMM'] ]
if x//1000>1:
    k=Mapping[3]
    k1=k[x//1000]
elif x//100>1:
    k=Mapping[x//100]
    k1=k[x//100]
elif x//10>1:
    k=Mapping[x//10]
    k1=k[x//10]
else :
    k=Mapping[x//1]
    k1=k[x//1]
if x//100-(x//1000)*10>1:
        l=Mapping[2]
        l1=l[x//100-(x//1000)*10]
elif x*10-(x//100)*10>1:
        l=Mapping[x*10-x//100*10]
        l1=l[x*10-x//100*10]
elif x-x//10*10>1 :
        l=Mapping[x-x//10*10]
        l1=l[x-x//10*10]
if x*10-x//100*10>1:
        m=Mapping[1]
        m1=m[x-(x//10)*10]
elif x-x//10*10>1 :
        m=Mapping[x-x//10*10]
        m1=m[x-x//10*10]
if x-x//10*10>1 :
    n=Mapping[0]
    n1=n[x-x//10*10]

if x>1000:
    print(k1,l1,m1,n1)
elif x>100:
    print(l1,m1,n1)
elif x>10:
    print(m1,n1)
else:
    print(n1)
