
#list Comprehension:
# result=[]
# for i in range(11):
#     if i%2!=0:
#         result.append(i)
# print(result,end=' ')

# print([i for i in range(10)if i%2!=0])
'''if odd square else cube in list comrehension'''
print([i**2 if i%2!=0 else i**3 for i in range(11) ])
mat=[[1,2,3,4],[5,6,7,8]]
print([j**2 if j%2!=0 else j**3 for i in mat for j in i3 ])