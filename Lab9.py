def f(text):
    s1=[]
    x=text
    s=x.split()
    mysort(s)
    s1.append(s[0])
    for i in range (len(s)-1):
        if len(s[i])!=len(s[i+1]):
            s1.append(s[i+1])
    se=' '
    s3=se.join(s1)
    return s3

def mysort(L):
    for i in range (len(L)):
        for j in range(0,len(L)-i-1) :
            if len(L[j])>len(L[j+1]) :
                L[j+1],L[j]=L[j],L[j+1]
    return L

text=input('give me one text:')
text1=f(text)
print(text1)
