'''n=int(input())
if n%3==0 and n%5!=0:
    print("multiple of 3",n)
elif n%5==0 and n%3!=0:
    print("multiple of 5",n)
elif n%15==0:
    printf("multiple of 3 and 5",n)
for i in range(1,101):
    print (i,end=' ')
for i in range(1,101,2):
    #(start,end,step)
    printf(i,end=' ')
for i in range(1,101,1):
    print(i,end=' ')
for i in range(100,1,-2):
    print(i,end=' ')
print()
for i in range(100,1,-1):
    print(i,end=' ')
print()

if i%2==0 and i%2!=0:
        print("even number",end=' ')
    else:
        print("odd number",end=' ')
for i in range(1,101):
    if i==50:
        break
    print(i,end=' ')
print()
print()
for i in range(1,101):
    if i==50:
        continue
    print(i,end=' ')
print()
print()
for i in range(1,101):
    if i==60:
        pass
    print(i,end=' ')
def func(nm1,nm2):
    print("number1=",nm1,"number2=",nm2)
    print()
    print()
func(10,20)
def func2(nm1,nm2):
    nm3=nm1+nm2
    return nm3
print(func2(100,200))
def func3(nm1,nm2):
    nm3=float(nm1)+nm2
    return nm3
print("return value is float type",func3('10',30.4))
def func3(nm1,nm2):
    nm3=nm1+str(nm2)
    return nm3
print("return value is string type",func3('10',30.4))
#catagories of functions
#1: positional arguments
def func3(nm1,nm2,nm3,nm4):
    print("nm1",nm1,"nm2",nm2,"nm3",nm3,"nm4",nm4)
func3(12,"23",34,45)'''
#keyword arguments
'''def func3(nm1,nm2,nm3,nm4):
    print("nm1",nm1,"nm2",nm2,"nm3",nm3,"nm4",nm4)
func3(nm4=10,nm3=20,nm1=30,nm2=50)
#3 default argument
def func4(name,rollno,branch="CSE",collegename="GIET"):
    print(name,rollno,branch,collegename)
func4("Hari",121)'''
#variable nu of argument
'''def func5(*var):
    sum=0
    for i in var:
        sum=sum+i
    return sum
print(func5(10,20))
print(func5(10,20,30,40,50,60))
print(func5(10,20,30,40,50,60))
'''

