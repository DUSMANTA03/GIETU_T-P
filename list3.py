'''x=input()
if len(x)>2:
    z=x[0:2]+x[-2:]
    print(z)
elif len(x)==2:
    print(x*2)
else:
    print(-1)'''
def concat(str1):
    if len(str1)>2:
        z=str1[0:2]+str1[-2:]
        print(z)
    elif len(str1)==2:
        print(str1*2)
    else:
        print(-1)
concat("w3school")