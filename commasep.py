
l1=[]
l2=[]
l3=[]
list1=list(map(int,input().split(",")))
for i in list1:
    if i!=5:
        l1.append(i)
    else:
        break
for j in range(len(list1)-1,-1):
    if j!=8:
        l2.append(j)
    else:
        break
l3=l1+l2
sum1=sum(l3)
print(sum1)
