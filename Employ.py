def add(emp_id,emp_name, emp_bonus=2500):
    print("add function")
    print(f"Employ id is {emp_id}\n Employ name is {emp_name}\n Employ bonus is {emp_bonus}\n\n")


add(12,"shyam")
add(24,"Tarun",3500)


def addnum(a,*verg):
    t = a
    for n in verg:
        t += n
    return t

total=addnum(2,3,4,7,9,20,45)
print(total)