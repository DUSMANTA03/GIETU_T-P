# a1=int(input())
# a2=int(input())
# a3=int(input())
a1,a2,a3=map(int,input().split())
if a1==7:
    print(a2*a3)
elif a2==7:
    print(a3)
elif a3==7:
    print(-1)
else:
    print(a1*a2*a3)