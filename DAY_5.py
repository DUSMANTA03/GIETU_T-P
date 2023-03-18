#OOPS BASED
'''Q1> WeCare insurance company wants to calculate premium of vehicles.

-->Vehicles are of two types - "Two Wheeler" and "Four Wheeler Each vehicle is identified by vehicle id, type, cost and premium amount.

-->Premium amount is 2% of the vehicle cost for two wheelers and6% of the vehicle cost for four wheelers.

Calculate the premium amount and display the vehicle details. Write a Python program to implement the class chosen with its attributes and methods.

Note:

Consider all instance variables to be private and methods to be public

Include getter and setter methods for all instance variables) Display appropriate error message, if the vehicle type is'''
'''class WeCare:
    def __init__(self):
        self.vid=None                  
        self.type=None
        self.cost=None
        self.p_amt=None
    def set_vid(self,__vid__):
        self.vid_=__vid__
    def set_type(self,type):
        self.type=type
    def set_cost(self,cost):
        self.cost=cost
    def get_pamt(self,p_amt):
        self.p_amt=p_amt
    def premiumamt(self):
        if self.type=="two wheeler":
            self.p_amt=int(self.cost*0.02)
            return self.p_amt
        elif self.type=="four wheeler":
            self.p_amt=int(self.cost*0.04)
            return self.p_amt
        else:
            print("Invalid Input")

obj1=WeCare()
obj1.set_vid(1)
obj1.set_type("two wheeler")
obj1.set_cost(int(input()))
print("The premium amount is= ", obj1.premiumamt())'''

'''Q2> A university wants to automate their admission process. Students are admitted based on marks scored in a qualifying exan

A student is identified by student id, age and marks in

qualifying exan

Data are valid, if:

Age is greater than 20

Marks is between 0 and 100 (both inclusive)

A student qualifies for admission, if Age and marks are valid and Marks is 65 or more '''
'''class University:
    def __init__(self):
        self.__s_id=None
        self.__marks=None
        self.__age=None
        self.__fees=None
    def set_s_id(self,s_id):
        self.__s_id=s_id
    def set_age(self,age):
        self.__age=age
    def set_marks(self,marks):
        self.__marks=marks
    def set_fees(self,fees):
        self.__fees=fees
    def validate_age(self):
        if self.__age>=20:
            return True
        else:
            return False
    def validate_mark(self):
        if self.__marks>0 and self.__marks<=100:
            return True
        else:
            return False
    def get_s_id(self):
        return self.__s_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    def get_fees(self):
        return self.__fees
    def elligible(self):
        if (self.__marks>=65 and self.__age>=20):
            print("Elligible for Admission")
        else:
            print("Not Elligible")
    def discount(self):
        if(self.__age>=20  and self.__marks >85):
               # self.__fees =self.__fees -(self.__fees*0.25)
             print("student id=",self.__s_id,"Course fee=",self.__fees-(self.__fees*0.25))
        else:
            print(self.__fees)
obj1=University()
obj1.set_s_id(10)
obj1.set_age(21)
obj1.set_marks(90)
obj1.set_fees(200000)
obj1.discount()
obj1.elligible()'''



'''Q4> PizzaForYou is a pizza store which sells different kinds of pizzas based on customer's order.40 min
Customer can either collect the order in person or opt for a door delivery.
Write a python program based on the class diagram given below.
Customer class:
validate_quantity(): A customer can order 1 to 5 pizzas
If quantity is valid, return true. Else return false
Pizzaservice class:
Initialize static variable counter to 100
Attribute, additional_topping is a boolean value which indicates whether additional topping is required or not.
True – additional topping is required, False – additional topping is not required
validate_pizza_type(): Customers can order "small" or "medium" type pizzas
If pizza type is valid, return true. Else return false
calculate_pizza_cost(): Calculate pizza cost
Validate pizza type and quantity
If valid,
Identify pizza cost based on details mentioned in the table
Set attribute, pizza_cost with the calculated pizza cost
Auto-generate service_id starting from 101 prefixed by first letter of pizza type. Example – S101, s102, m103, S104, M105 etc
If invalid, set pizza_cost to -1
PizzaType	Cost/Pizza(in Rs)	Additional topping cost/Pizza       (in Rs), if applicable
Small	150	35
Medium	200	50
Doordelivery class:
validate_distance_in_kms(): Minimum distance for door delivery is 1km and maximum is 10kms
Validate distance_in_kms
If valid, return true. Else, return false
calculate_pizza_cost: Calculate pizza cost
Validate distance in kms
If valid,
Calculate pizza cost (Hint: Invoke overridden method in parent class)
If pizza_cost is not -1, identify delivery charge based on details mentioned below and add it to attribute, pizza_cost
Distance in kms	Delivery Charge in km(in Rs)
For first 5 kms	5
For remaining 5 kms	7
Else, set pizza_cost to -1
Note: Perform case insensitive string comparison  
For testing:
Create objects of Pizzaservice and Doordelivery classes
Invoke calculate_pizza_cost() on Pizzaservice and Doordelivery objects
Display the detail'''
class customer:
    def validate_quantity(self,quantity):
        if quantity>=1 and quantity<=5:
            return True
        else:
            return False
class pizza_service:
    counter=100
    def __init__(self,p_type,additional_topping,quantity):
        self.additional_topping=additional_topping
        self.p_type=p_type
        self.p_cost=0
        self.quantity=quantity
        self.service_id=''
    def validate_pizza_type(self):
        if self.p_type=="small"or self.p_type=='medium':
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.p_type=="small":
            self.p_cost=150*self.quantity
            if self.additional_topping:
                self.p_cost+=35*self.quantity
            self.service_id='s'+str(pizza_service.counter+1)
        elif self.p_type=='medium':
            self.p_cost=200*self.quantity
            if self.additional_topping:
                self.p_cost+=50*self.quantity
            self.service_id='m'+str(pizza_service.counter+1)
        else:
            self.p_cost=-1
class delivery(pizza_service):
    #def __init__(self,p_type,additional_topping,quantity)
    def validate_distance_in_kms(self,distance_in_km):
        self.distance_in_km=distance_in_km
        if self.distance_in_km>=1 and self.distance_in_km<=10:
            if self.distance_in_km<=5:
                self.p_cost+=5
            elif self.distance_in_km>5 and self.distance_in_km<=10:
                self.p_cost+=7
        

            




