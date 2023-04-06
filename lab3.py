'''
Input the elements of L1, separated by commas: 23,43,1,2,5,98
Input the elements of L2, separated by commas: 3,9,14,10,2,5,9,19,12
L1= [23, 43, 1, 2, 5, 98]
L2= [3, 9, 14, 10, 2, 5, 9, 19, 12]
n1= 98
n2= 19
prod= 1862
L1= [23, 43, 1, 1862, 2, 5, 98]
L2= [3, 9, 14, 10, 1862, 2, 5, 9, 19, 12]
L3= [1, 2, 2, 3, 5, 5, 9, 9, 10, 12, 14, 19, 23, 43, 98, 1862, 1862]
'''

S1 = input("Input the elements of L1, separated by commas: ")
S2 = input("Input the elements of L2, separated by commas: ")

s1 = S1.split(',')
s2 = S2.split(',')

L1 = [int(x) for x in s1]
L2 = [int(x) for x in s2]

print("L1=",L1)
print("L2=",L2)

n1 = max(L1)
n2 = max(L2)

print("n1=",n1)
print("n2=",n2)

prod = n1*n2
print("prod=",prod)

L1.insert(len(L1)//2,prod)
L2.insert(len(L2)//2,prod)

print("L1=",L1)
print("L2=",L2)

L3 = L1+L2

L3.sort()
print("L3=",L3)
