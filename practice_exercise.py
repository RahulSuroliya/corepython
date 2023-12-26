# fint if the given input is palindrome or not

'''def palindrome():
    a = str(input("please give the input "))
    if (a != a[::-1]):
        print("it's not palindrome")
    else:
        print("it is palindrome")


palindrome()'''

'''class A:

    def avg_even_numbers_between(self,a,b):
        count = 0
        sum = 0
        print("Numbers :")
        for i in range(a,b):

            if i%2==0:

                print(i)
                count+=1
                sum +=i

        print("Average :",(sum)/count)

    def avg_odd_numbers_between(self,a,b):
        count = 0
        sum = 0
        print("Numbers :")
        for i in range(a,b):

            if i%2==1:

                print(i)
                count+=1
                sum +=i

        print("Average :",(sum)/count)

obj = A()
obj.avg_even_numbers_between(12,23)
obj.avg_odd_numbers_between(11,23)'''

'''a = int(input("please give starting no."))
b = int(input("please give ending no."))
print("Numbers :")
sum = 0
for i in range(a,b+1):
    if i%7==0:
        print(i)
        sum=sum+i
print("Sum :",sum)'''

# prog. to print all even indexed value in a list

'''lst = [1,2,3,4,5,6,7,8,9,10]

for i in range(0,len(lst)):
    if i%2==0:
        print("even indexed value :",lst[i])'''

#prog. to print all the even no in a list
'''lst = [2,3,8,19,14,11,34,46,55,79,88]
print("even no. in list :")
for i in lst:
    if i%2==0:
        print(i)'''

# prog. to print all odd indexed value in a list
'''lst = [1,2,3,4,5,6,7,8,9,10]

for i in range(0,len(lst)):
    if i%2==1:
        print("odd indexed value :",lst[i])'''

# prog. to extract odd indexed characters and add them to a list

'''a = []
b = str(input("please input a string"))
for i in range(0,len(b)):
    if i%2==1:
        a.append(b[i])
print(a)'''

# Write a prog to extract all vowels from a string and add to a list.
'''star = "Raj works in delhi"
lst = ['a','e','i','o','u']
lst2 =[]
for n in star:
    for m in lst:
        if n==m:
            lst2.append(n)

print(lst2)'''

# create a dictionary with lowercase alphabet as key and their ascii value as value.
'''star = "abcdefghijklmnopqrstuvwxyz"
d ={}
for i in star:
    d[i]=ord(i)

print(d)'''

# convert in uppercase in dictonary keys and values by using ascii key

'''star = "abcdefghijklmnopqrstuvwxyz"
d ={}
for i in star.upper():
    d[i]=ord(i)

print(d)'''

# print all the vowels along with the values in the dictonary

'''star = "abcdefghijklmnopqrstuvwxyz"
vowel = ['A','E','I','O','U']
d ={}
for i in star.upper():
    d[i]=ord(i)

print(d)
print('A :',d.get('A'))
print('E :',d.get('E'))
print('I :',d.get('I'))
print('O :',d.get('O'))
print('U :',d.get('U'))
'''

# print all the keys which have values ending with 1 or 4

'''star = "abcdefghijklmnopqrstuvwxyz"
d ={}
for i in star:
    d[i]=ord(i)
    if str(ord(i)).endswith('1') or str(ord(i)).endswith('4'):
        print(i,":",ord(i))
print(d)'''

# print all the keys and values which have values 5 or 7 in them

'''star = "abcdefghijklmnopqrstuvwxyz"
d ={}
for i in star:
    d[i]=ord(i)
    if '5' in str(ord(i)) or '7' in str(ord(i)):
        print(i,":",ord(i))
print(d)'''

# print all the keys and values which have values ending with even no.

'''star = "abcdefghijklmnopqrstuvwxyz"
d ={}
for i in star:
    d[i]=ord(i)
    if ord(i)%2==0:
        print(i,":",ord(i))
print(d)'''


# write a prog to check if a no is even or odd

'''a = int(input("give input here"))
if a%2==0:
    print("given no in even")
else:
    print("given no is odd")'''

# write a program
'''s = "rahul123@gmail.com"
for i in s:
    if i.isnumeric()==True:
        print(i)'''


# wap to count the digits in the above string

'''s = "rahul123@gmail.com"
count = 0
for i in s:
    if i.isnumeric() == True:
        print(i)
        count += 1
        print("Total no of digits :",count)'''

# wap to count the no of special characters in the string

'''s = "rahul123@gmail.com"
count = 0
for i in s:
    if i.isalnum() == False:
        print(i)
        count += 1
        print("Total no of special character :",count)'''

# wap to count all no of special characters,alphabet,and digits from above string

'''s = "rahul123@gmail.com"
count1 = 0
count2 = 0
for i in s:
    if i.isalnum() == False:
        print(i)
        count1 += 1

    elif i.isnumeric() == True:
        print(i)
        count2 += 1

    else:
        countalpha = len(s)-(count1+count2)


print("Total no of special character :",count1)
print("Total no of digits :", count2)
print("Total no of alphabets :", countalpha)
print("Total no of characters :",len(s))'''


# wap to iterate through a string 'hello world'
'''a="hello world"
for i in a:
    print(i)'''

# wap to extract all the no's from a string and print the sum of digits

'''s = "rahul123@gmail.com"
sum=0
for i in s:
    if i.isnumeric()==True:
        sum = sum + int(i)
        print(i)
print("sum of the digits :",sum)'''

# wap to iterate through a list

'''a = ['h','e','l','l','o','','w','o','r','l','d']
for i in a:
    print(i)'''

# wap to print all the list items with odd indexed values in reverse

'''a = ['h','e','l','l','o','','w','o','r','l','d']
i = 10
while i > 0:
    if i%2==1:
        print(a[i])
    i-=1'''

# wap to print no from 1-10
'''i=1
while i<11:
    print(i)
    i+=1'''


# wap to print no from 10-1
'''i=10
while i>0:
    print(i)
    i-=1'''

# print even no from 1-10
'''i=1
while i<=10:
    if i%2==0:
        print(i)
    i+=1'''

# print even no from 20-1
'''i=20
while i>0:
    if i%2==0:
        print(i)
    i-=1'''

# odd no from 1-10

'''i=1
while i<=10:
    if i%2==1:
        print(i)
    i+=1
'''
# odd no from 10-1
'''i=10
while i>0:
    if i%2==1:
        print(i)
    i-=1
'''

# no which are divisible by 5 and 7 in range 1-200
'''i=1
while i<=200:
    if i%5==0 and i%7==0:
        print(i)
    i+=1'''

# no ending with 6 in range 1-150
'''i=1
while i<=150:
    if str(i).endswith('6'):
        print(str(i))
    i+=1'''

# no which have 8 in them in range 1-200
'''i=1
while i<=200:
    if '8' in str(i):
        print(str(i))
    i+=1'''

# add no from 1-10 in a list
'''i=1
l=[]
while i<=10:
    l.append(i)
    i+=1
print(l)'''

# add no from 1-10 in a set
'''i=1
l=set()
while i<=10:
    l.add(i)
    i+=1
print(l)'''

'''for i in range(10):
     print((' '*(42-i))+('*'*i)+('*'*(i-1)))

i=30
while i>16:
    print((' ' *(42 - i)) + ('*' * i) + ('*' * (i - 1)))
    i-=2
i=17
j=1
while i>0 and j<18:
    print((' ' * (i+6)) + ('*' * i)+('  ' * j) + ('  ' * (j-1)) + ('*' * (i )))
    i-=2
    j+=2'''


