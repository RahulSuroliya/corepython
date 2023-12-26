'''import threading
from threading import *
def hello():
    for i in range(15):
        print("hello",i)

def hi():
    for i in range(15):
        print("hi",i)

# hello()
# hi()


t1 = threading.Thread(target=hello)
t2 = threading.Thread(target=hi)

#start threads
t1.start()
t2.start()'''
import threading

'''from threading import *
class Mythread(Thread):
    def run(self):
        for i in range(5):
            print("\n this is a child ")

t=Mythread()
t.start()'''

'''from time import sleep
from threading import Thread
class A(Thread):
    def run(self):
        for i in range(5):
            print("Rays")
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print("deepak")
            sleep(1)

t1 = A()
t2 = B()
t1.start()
t2.start()

t1.join()
t2.join()
print("Ncs")
'''

'''from threading import Thread


def run():
    for i in range(15):
        print("hi",i)

def hello():
    for i in range(15):
        print("hello",i)


t1=Thread(target=run(),daemon=True)
t2=Thread(target=hello(),daemon=False)
t1.start()
t2.start()'''

'''from threading import Thread
from time import sleep

class Account:
    balance=0

    def get_balance(self):
        sleep(1)
        return self.balance

    def set_balance(self,amount):
        sleep(1)
        self.balance = amount

    def deposit(self,amount):
        bal = self.get_balance()
        self.set_balance(bal+amount)

class Racing(Thread):
    account = Account()
    name = ""

    def __init__(self,account,name):
        super().__init__()
        self.account = account
        self.name = name

    def run(self):
        for i in range(5):
            self.account.deposit(100)
            print(self.name,self.account.get_balance())

t1 = Racing(Account(),"Ram",)
t2 = Racing(Account(),"shyam")

t1.start()
t2.start()

t1.join()
t2.join()'''

'''from threading import *
from time import sleep

class Account:
    balance=0
    def __init__(self):
        self.lock = threading.Lock()

    def get_balance(self):
        sleep(.5)
        return self.balance

    def set_balance(self,amount):
        sleep(.5)
        self.balance = amount

    def deposit(self,amount):
        self.lock.acquire()
        bal = self.get_balance()
        self.set_balance(bal+amount)
        self.lock.release()

class Racing(Thread):
    account = Account()
    name = ""

    def __init__(self,account,name):
        super().__init__()
        self.account = account
        self.name = name

    def run(self):
        for i in range(5):
            self.account.deposit(100)
            print(self.name,self.account.get_balance())

t1 = Racing(Account(),"Ram",)
t2 = Racing(Account(),"shyam")

t1.start()
t2.start()

t1.join()
t2.join()'''