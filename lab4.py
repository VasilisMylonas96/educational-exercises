S = input("Input text here: ")

L = S.split()

counters = {}
maxlen = 0
for word in L:
    maxlen = max(maxlen,len(word))
    if word in counters:
        counters[word]+=1
    else:
        counters[word]=1

# print(counters)

for w in counters:
    if (counters[w]==1):
        print("%-*s appears 1 time." % (maxlen,w))
    else:
        print("%-*s appears %d times." % (maxlen,w,counters[w]))
