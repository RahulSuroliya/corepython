'''file = open("Rahul.txt",'r')
content = file.read()
file.close()
print(file.mode)
print(file.closed)
print(content)
'''

'''file = open("Rahul.txt")
for line in file:
    print(line)
file.close()'''

'''file = open("Test.txt",'w')
file.write("Hi\n")
file.write("This is a python file")
file.close()
'''

'''with open("Test.txt","w") as file:
    file.write("Hi\n")
    file.write("This is a python file")

with open("Test.txt","r")as file:
    content=file.read()
    print(content)

with open("Test.txt","r")as file:
    content=file.read(10)
    print(content)
    print(file.tell())
    print(file.seek(0,2))
    '''

'''import os
os.renames("rays.txt","ray.txt")
os.remove("ray.txt")
'''


