# #check nearest palindrome:
# import sys
# def checkpal(n):
#     for i in range(n+1,sys.maxsize):
#         if str(i)==str(i)[::-1]:
#             return i
# print(checkpal(int(input())))
'''l2=[]
c1,c2,c3=0,0,0
l1=list(input().split(','))
d={"P":"Pediatric","O":"Orthopedic","E":"ENT"}
for i in l1:
    if i.isalpha():
        l2.append(i)
for i in range(len(l2)):
    if l2[i]=='p':
        c1+=1
    elif l2[i]=='o':
        c2+=1
    elif l2[i]=='e':
        c3+=1
if c1>c2 and c1>c3:
    print(d["P"])
elif c2>c1 and c2>c3:
    print(d["O"])
else:
    print(d["E"])'''
'''x=input()
y=input()
ret=""
for i in x:
    for j in y:
        if i==j and i!=" ":
            ret=ret+j
            break
print(ret)
class Example:
    def __init__(self,num):
        self.num=num
    def setnum(self,num):
        self.num=num
    def getnum(self):
        return self.num
obj=Example(10)
print(obj.getnum())
obj.setnum(15)
print(obj.getnum())
class customer:
    def __init__(self,id):
        self.id=100
c1=customer(200)
print(c1.id)'''

#What is the output of the following code snippet?

'''class Book:

    def init_(self): 
        self.title=None

my_fav=Book()
my_fav.title="Head First Programming" 
your_fav=Book() 

your_fav.title="Learn Python the hard way"

my_fav.title="Learning Python"

print("My favorite is",my_fav.title)
print("Your's is",your_fav.title)'''

'''class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
    def __str__(self):
        return "Shoe with price: "+str(self.price)+" and material is: "+str(self.material) 
s1=shoe(200,"Rubber")
print(s1.price)
print(s1.material)
print(id(s1),":-ID of object s1") 
print(s1)

class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details")
    def purchase(self):
        self.display()
        print("Calculating Price")
Mobile().purchase()
m1=Mobile()
print(m1)
m2=Mobile()
print(m2)
m1=m2
print(m1)
print(m2)


class Mobile:
    def __init__(self,brand,price):
        self.brand= brand
        self.price= price 
        self.total_price = None

    def purchase(self):

        if self.brand =="Apple": 
            discount = 10
        else:
            discount= 5

        self.total_price= self.price -self.price*(discount/100)
        print("Total price of", self.brand, "mobile is", self.total_price)
mobl=Mobile("Apple", 20000)
mob2=Mobile("Samsung", 10000)
mobl.purchase()
mob2.purchase()'''


'''class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.wallet_balance=wallet_balance
    def update_balance(self,amount):
        if amount <100 and amount>0:
            self.wallet_balance+=amount
    def show(self):
        print("The balance is: ",self.wallet_balance)#or return self.wallet_balance
c1=Customer(108,"Gopal",24,1000)
c1.update_balance(500)
c1.show()'''

'''class Table:
    def _init_(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self,glass_top, wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self, glass_top, wooden_top):
        self.assign_data(glass_top,wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate(False,True)
print(rate)'''

class Table:
    def _init_(self):
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=Table()
back_table=Table() #
front_table=back_table
back_table=dining_table
print(dining_table, back_table, front_table)
