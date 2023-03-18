def translate(list1,dict1):
    list2=[]
    for i in list1:
        list2.append(dict1[i])
    return list2

dict1={"marry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
list1=['marry','christmas']
print(translate(dict1,list1))
