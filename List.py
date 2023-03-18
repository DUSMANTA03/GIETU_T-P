#list-->ordered ds
'''list1=[101,201,304]
print(list1.pop())
x=del.list1'''
'''def count(s):
    
    d=0

    c=0
    for i in s:
        if (i>=97 and i<=122) or (i>=65 and i<=90):
            c+=1
    for i in s:
        if (i>=49 and i<=57):
            d+=1
    return[c,d]

print(count(input()))'''
'''def func(str1):
    c=0
    s=0
    for i in str1:
        if i.isalpha():
            s+=1
        elif i.isdigit():
            c+=1
        else:
            continue
    return[c,s]
print(func("Infosys 123"))'''
def findpair(num,n):
    count=0
    for x in num:
        index=num.index(x)+1
    for y in range(index,len(num)):
        if x+num[y]==n:
            count+=1
    return count
num=[1,2,3,4,5,6,0]
n=7
print(findpair(num,n))