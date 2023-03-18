five= int(input("Enter number of 5 note"))
x=five*5
one = int(input("Enter the number of 1 coin"))
y=one*1
required=int(input("enter required value"))
if required <= (x+y):
    x1=required%5
    print("number of 1 coin needs:",x1)
    y1=required//5
    print("number of 5 note needs:",y1)
else:
    print(-1)
    