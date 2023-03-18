def check_double(num):
    res=num*2
    z=str(num)
    x=str(res)
    a=sorted(z)
    b=sorted(x)
    if len(x) == len(z):
        if a==b:
            print("True")
        else:
            print("False")

check_double(int(input()))
        