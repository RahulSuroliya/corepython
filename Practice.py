'''class A:
    a =10
    _b = 20
    __c = 30
    print(a,_b,__c)

obj = A()
print(obj.a)
print(obj._b)
print(obj.__c)'''


'''class A:
    a = 10
    _b = 20
    __c = 30

class B(A):
    def show(self):
        print(self.a)
        print(self._b)
        print(self.__c)

d = A()

print(d._A__c)'''


'''class A:
    a = 10
    _b = 20
    __c = None

class B:
    def show(self):
        print(A.a)
        print(A._b)
        print(A.__c)

obj = A()
objb = B()
objb.show()
'''


'''class Math:
    def max(a,b):
        if (a>b):
            print(a)
        else:
            print(b)
Math.max(5,7)
'''

'''def fact(n):
        if n==0:
          return 1
        else:
            return n*fact(n-1)

a = fact(6)
print(a)'''














