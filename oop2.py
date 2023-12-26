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

'''class A:
    def sum(self,a,b):
        print(a+b)

class B(A):
    def sum(self,a,b,c):
        super().sum(a,b)
        print(a+b+c)

obj = B()
obj.sum(2,3,4)
'''
'''class Shape:
    def area(self):
        return -1

class Ractangle(Shape):
    length = int(input("type length"))
    width = int(input("type width"))

    def area(self):
        print( self.length*self.width)

obj =Ractangle()
obj.area()'''


'''class Police_character:
    def walk(self):
        print(" the character is walking ")

    def talking(self):
        print(" the character is talking ")

    def jump(self):
        print(" the character is walking ")

    def walk_left(self):
        print("the character is walking left")

    def walk_right(self):
        print("the character is walking right")

obj = Police_character()
obj.walk()
obj.talking()'''

