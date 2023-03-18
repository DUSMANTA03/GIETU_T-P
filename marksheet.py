#Percentage
count=0
#tup1=tuple(input().split())
l1=list(map(int,input().split(',')))
avg=sum(l1)/len(l1)
for i in l1:
    if i>=avg:
        count+=1
percentage=(count*100)/len(l1)
print(percentage)
#Sorted 
l1=sorted(l1)
print(l1)
#Frequency
freq=[]
for i in range(25):
    c=0
    for x in l1:
        if i==x:
            c+=1
    freq.append(c)
print(freq)

# l1=list(map(int,input().split(',')))
# avg=sum(l1)/len(l1)
# c=0
# freq=[]
# for i in l1:
#     if i>=avg:
#         c+=1
# print((c*100)/len(l1))
# print()
# for i in range(26):
#     flag=0
#     for c1 in l1:
#         if c1==i:
#             flag+=1
            
#     freq.append(flag)
# for k in range(len(freq)):
#     print(freq[k],end="")
#     if k<len(freq)-1:
#         print(',',end=' ')
# print()

# l2=sorted(l1)
# for l in range(len(l2)):
#     print(l2[l],end="")
#     if l<len(l2)-1:
#         print(",",end=" ")
