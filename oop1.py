'''class Person:
    name =""
    dob =""
    address =""

    def setname(self,name):
        self.name = name

    def getname(self):
        return self.name

    def setdob(self,dob):
        self.dob = dob

    def getdob(self):
        return self.dob

    def setaddress(self,address):
        self.address = address

    def getaddress(self):
        return self.address

    def getdetails(self):
        return self.name,self.dob,self.address

obj = Person()
obj.setname("rahul")
obj.setdob("17-02-2001")
obj.setaddress("sikar")
obj.getname()
obj.getdob()
obj.getaddress()
print(obj.getname())
print(obj.getdob())
print(obj.getaddress())
print(obj.getdetails())'''



'''class Account:
    name =""
    accountType ="Saving"
    balance =1000

    def setname(self,name):
     self.name =name

    def getname(self):
      return self.name

    def setaccountType(self,accountType):
      self.accountType =accountType

    def getaccounttype(self):
        return self.accountType

    def setbalance(self,balance):
      self.balance =balance

    def getbalance(self):
        return self.balance

    def setdetails(self,name):
        self.name = name



    def getdetails(self):
        return self.name,self.accountType,self.balance


obj =Account()
obj.setname("Rajat")
obj.setaccountType("Saving")
obj.setbalance(15000)
obj.getdetails()
obj.getname()
obj.getaccounttype()
print(obj.getname())
print(obj.getaccounttype())
print(obj.getbalance())
obj.setdetails("Raj")
obj.getbalance()
print(obj.getdetails())
'''

# first
'''class A:
    age = 10
    print(age)
obj = A()'''

# second

'''class A:
    "docstring calling"
    age = 10
    print(age)
obj = A()
print(obj.age)
print(A.age)
print(obj.__doc__)
print(A.__doc__)'''

# third

'''class A:
    age = 10
    def fun(self):
        "hi i am"
        name = "learn coding"
        print(name)
obj = A()
obj.fun()
print(obj.age)
print(A.age)
print(obj.fun.__doc__)'''

# forth

'''class A:
    name = "Raj"
    age = 23
    address = "Kanpur"
    def __init__(self):
        print(A.name,A.age,A.address)

    def fun(self,name,age,address):
        print(name,age,address)

obj = A()
obj.fun("Rahul",22,"sikar")'''

'''class Calculator:
    a = 1
    b = 1

    def add(self,a,b):
        #c = a+b
        print("add = "
              "" ,a+b)

    def sub(self,a,b):
        c = a-b
        print(c)

    def mul(self,a,b):
        c = a*b
        print(c)

    def div(self,a,b):
        if b==0:
            print("cannot divide by 0")
        else:
            c = a/b
            print(c)

a = Calculator()
a.add(2,4)
a.sub(5,3)
a.mul(2,5)
a.div(5,0)
a.div(5,2)
'''

'''class A:
    a = 10
    _b = 20
    __c = 30
   # print(a,_b,__c)

obj = A()
print(obj.a)
print(obj._b)
print(obj.__c)'''

'''class A:
    a = 10
    _b = 20
    __c = None

    def add(self):
        self.__c = self.a + self._b
        print("add",self.__c)

obj =A()
obj.add()
print(obj.a)
print(obj._b)
print(obj.__c)'''

'''class A:
    a = 10
    _b = 20
    __c = None
'''
'''class B(A):
    def show(self):
        print(self.a)
        print(self._b)
        print(self.__c)

objb = B()
objb.show()'''


'''class A:
    a = 10
    _b = 20
    __c = None
    print(a,_b,__c)'''

'''class B:
    def show(self):
        print(A.a)
        print(A._b)
        print(A.__c)

objb =B()
objb.show()'''

'''class Math:
    def max(a,b):
        if(a>b):
            print(a)
        else:
            print(b)

Math.max(5,7)'''

'''class A:
    def showdisplayA(self):
        print("This is class A")

    def showdataA(self):
        print("A is the parent class of B")

class B(A):
    def showdisplayB(self):
        print("This is class B")

    def showdataB(self):
        print("B is the child class of A")

objb =B()
objb.showdisplayA()
objb.showdisplayB()
objb.showdataA()
objb.showdataB()'''

'''class A:
    def displayA(self):
        print("This is class A")

class B(A):
    def displayB(self):
        print("This is class B")

class C(B):
    def displayC(self):
        print("This is class C")

obj = C()
obj.displayA()
obj.displayB()
obj.displayC()
'''
'''class A:
    def displayA(self):
        print("This is class A")

class B:
    def displayB(self):
        print("This is class B")

class C(A,B):
    def displayC(self):
        print("This is class C")

obj = C()
obj.displayA()
obj.displayB()
obj.displayC()'''

'''class A:
    def is_even(self,n):
        for i in range (1,n):
            if i%2==0:
                print(i)

obj = A()
obj.is_even(20)'''

'''class A:
    def is_even(self,m,n):
        for i in range (m,n):
            if i%2==0:
                print(i)

obj = A()
obj.is_even(20,79)
'''

'''def is_armstrong():
    number = int(input("please give input "))
    str_number = str(number)
    len_number = len(str_number)
    sum = 0
    for digit in str_number:
        sum = int(digit)**len_number
        sum = sum + sum1

    if(sum == number):
            print("This no. is armstrong")
    else:
            print("This no. is not armstrong")

is_armstrong()'''

'''class A:
    def __init__(self):
        print(" This is constructor")

    def show(self):
        print("Show method")

    def __del__(self):
        A = self.__class__.__name__
        print("Destroying",A)

obj = A()
'''

'''class A:
    def add(self, a, b):
        # c = a+b
        print("add = "
              "", a + b)

    def sub(self, a, b):
        c = a - b
        print(c)

    def mul(self, a, b):
        c = a * b
        print(c)

    def div(self, a, b):
        if b == 0:
            print("cannot divide by 0")
        else:
            c = a / b
            print(c)

class B(A):
    def __init__(self):
        print("This is child class")

obj = B()
obj.add(2,4)
'''



'''for i in range(1,21):
    if i%2 == 0:
        print(i)'''

'''class Shape:
    def __init__(self,color):
        self.color = color

    def display_color(self):
        print(f"The shape is {self.color}")

class Rectangle(Shape):
    def __init__(self,color,width,height):
        super().__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def display_color_and_area(self):
        super().display_color()
        area = self.calculate_area()
        print(f"The area of rectangle is {area}")

rectangle = Rectangle("blue",9,10)
rectangle.display_color_and_area()'''

'''class Formulas:
    def add(self, a, b):
        # c = a+b
        print("add = "
              "", a + b)

    def sub(self, a, b):
        c = a - b
        print(c)

    def mul(self, a, b):
        c = a * b
        print(c)

    def div(self, a, b):
        if b == 0:
            print("cannot divide by 0")
        else:
            c = a / b
            print(c)

    def reminder(self,a,b):
        c = a%b
        print(c)

    def quescent(self,a,b):
        c = a//b
        print(c)

    def square_root(number):
        # Initial guess for the square root
        guess = number / 2.0

        # Iterate until desired accuracy is achieved
        while abs(guess * guess - number) > 0.0001:
            guess = (guess + number / guess) / 2.0

        print(guess)

    '''


'''class Addition:

    def add(self,a=0,b=0,c=0):
        print("Addition is ",a+b+c)

s = Addition()
s.add(12,12)
s.add(12,12,12)
s.add(12)
s.add()'''

# method overloading

'''class Calci:
    def add(self,num1=None,num2=None,num3=None):
        if num1!=None and num2!=None and num3!=None:
            print("Addition is",num1+num2+num3)
        elif num1!=None and num2!=None:
            print("Addition is ",num1+num2)
        else:
            print("incorrect value provided")

a = Calci()
a.add(12,12)
a.add(12,12,12)
a.add()
'''

'''class Area:
    def area(self,radius=0,length=0,breadth=0,base =0,height=0,circle=0,square=0,ractangle=0,triangle=0):
        if square!=0:
            print("area os square is ",length*length)
        elif ractangle!=0:
            print("area of ractangle is ",length*breadth)
        elif triangle !=0:
            print("area of triangle is ",0.5*base*height)
        elif circle!=0:
            print("area of circle is",3.14*radius*radius)
        else:
            print("Formula is not specified")

obj = Area()
obj.area(base=12,height=24,triangle=1)
obj.area(length=12,square=1)
obj.area(radius=3.5,circle=1)
'''
'''def count_notes(a):
    # a = input("please input a no. in multiples of 10")
         b = a%500
         c = b%200
         d = c % 100
         e = d % 50
         f = e % 20
         g = f%10
         h =g%5
         i =h%2
         print("notes of 500 =", a//500)
         print("notes of 200 =", b//200)
         print("notes of 100 =", c//100)
         print("notes of 50 =", d//50)
         print("notes of 20 =", e//20)
         print("notes of 10 =", f//10)
         print("notes of 5 =", g // 5)
         print("notes of 2 =", h // 2)
         print("notes of 1 =", i // 1)

count_notes(888)'''

