# s=int(input())
# e=int(input())
# c=0
# l1=[]
# for i in range (s,e+1):
#     l1.append(i)
# for i in range(len(l1)+1):
#     for j in range(i):
#         print(l1[j:i])
#         if sum(l1[j:i])%2!=0:
#             c+=1
#             print(c)
n1=int(input())
n2=int(input())
l1=[]
for i in range(n1,n2+1):
    l1.append(i)
array=[i for i in range(n1,n2+1)]
print(array)
for i in range(len(array)):
    for j in range(i,len(array)):
        l1.append(array[i:j+1])
print(l1)