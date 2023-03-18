def ingadd(str1,str2="ing",str3="ly"):
    if str1[-3:] =="ing" and len(str1)>=3:
        print(str1+str3)
    elif str1[-3:]!="ing" and len(str1)>=3:
        print(str1+str2)
    else:
        print(str1)
ingadd(input())