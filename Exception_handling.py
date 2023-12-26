'''a = 4
b = 0
try:
    c = a/b
    print('C:',c)
except ZeroDivisionError:
    print("check your divident is zero")'''

'''a = 4
b = 0
try:
    c = a/b
    print('C:',c)
except ZeroDivisionError as e:
    print("Exception:",e)'''


'''a = 4
b = 2
try:
    c = a/b
    print('C:',c)
except ZeroDivisionError:
    print("check your division is zero")
else:# it will be executed when no exception raised
    print("your division was greater than zero")
    
a = 4
b = 0
try:
    c = a/b
    print('C:',c)
except ZeroDivisionError:
    print("check your division is zero")
else:# it will be executed when no exception raised
    print("your division was greater than zero")'''

'''a = 4
b = 0
try:
    c = a/b
    print('C:',c)
except ZeroDivisionError:
    print("check your division is zero")
finally:
    print("always executed")
'''
'''a = 4
b = 2
try:
    c = a/b
    print('C:',c)
except ZeroDivisionError:
    print("check your division is zero")
finally:
    print("always executed")'''


'''try:
    number = int(input("Enter your number :"))
    if number > 10:
        raise Exception('invalid number')
except Exception as e:
    print(e)'''