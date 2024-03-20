'''
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number

# pb:2
s1 = "hello how are you"
s2 = "hello how is"

s1 = "hello how are you"
s2 = "hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)

# pb:3
0,1,2,3,4,5,6,7,8,9

n1 = 0
n2 = 1
ans=0+1=1

n1 = 1
n2 = 1
ans=1+1=2

n1 = 1
n2 = 2
ans= 1+2=3

n1 = 2
n2 = 3
ans=2+3=5

# find the 8th fibanochi number
num=8
n1=0
n2=1

for val in range(num):
    ans=n1+n2
    n1=n2
    n2=ans
print(ans)

# ! constructors
# ? eg:2
# unparametarised constructor
class profile:
    def __init__ (self):
        print("hello world")
obj =profile()
obj.__init__()

# ? eg :3
# parametarised constructor
class profile:
    def __init__ (self, id, name, age):
        print(id, name, age)

obj = profile(1, "malli", 23)

# ? eg:4
class c1:
    email = "malli@gamil.com"
    def m1(self):
        name = "malli"
        place = "cbe"
        print(name, place)
        print(self.email)

object = c1()
object.m1()

# eg;5
class c1:
    def m1(self):
        name = "malli"
        age = 23
        return name, age
    def display(self):
        # ! print(name, age)
        # ! print(self.name, self.age)
        print(self.m1())

object = c1()
object.display()

# eg:6
# to use the variables inside the constructor in another methods
class class1:
    def __init__(self):
        self.name = "malli"
        self.email = "malli@gmail.com"
        # return name, email # error --> cannot use return with constructor

    def display(self):
        print(self.name, self.email)

c1 = class1()
c1.display()

# ! -----> inheritance
# the process of utilising the methods and attributes of parent class
# throught the object of child class it is called as interference

# ? types of inheritence
single inheritance
multilevel inheritance
multiple inheritance
hybrid inheritance
heirarichal inheritance

# * single inheritence
# ? it has only one parent class and only one child class
# ! Eg:1
class parent:
    def m1(self):
        print("iam parent class")

class child(parent):
    def m2(self):
        print("iam child class")

obj = parent()
obj.m1()

# ! eg:2
class c1:
    def __init__(self):
        print("iam constructor from parent class")

class child(c1):
    pass

obj = child()

# ! eg:3
class parent:
    name = "malli"

class child(parent):
    name = "malli"

    def display(self):
        print(self.name)

d = child()
d.display()

# ! multilevel inheritance
# ? eg:1
class voice:
    def sound(self):
        print("all animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(dog):
    def cat_voice(self):
        print("meow")

class parrot(cat):
    def parrot_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()


# ! multiple inheritance
# ? it has multiple parent and i child

class while_petrol:
    def funtion_w(self):
        print("used to airplanes")

class organic_petrol:
    def function_o(self):
        print("used for bikes,cars")

class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")

class petrol(while_petrol,organic_petrol, premium_petrol):
    def defanition(self):
        print("petrols types")

p = petrol()
p.defanition()
p.function_o()

# ! eg:2
# mro ----> method resolution order
class addition:
    def add(self, a, b):
        print(a+b)
class subtract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition,subtract,multiply):
    def div(self, a, b):
        print(a/b)

calc = division()
#calc.add(3, 4)
calc.mul(4, 2)

# ! heirarical inheritance
class category:
    def cat_name(self, weight):
        print(weight)

class tomato(category):
    def tomato_spec(self):
        color="black"
        taste = "neutral taste"

class carrot(category):
    def carrot_specs(self):
        color="green"
        taste = "sweet"

c = carrot()
c.carrot_specs()
c.display()

# ! hybrid inheritance
# ? the combination of above 4 inheritance is called hybrid inheritance
class c1:
    def m1(self):
        print("class1")

class c2(c1):
    def m2(self):
        print("class2")

class c3(c2):
    def m3(self):
        print("class3")

class c4(c3):
    def m4(self):
        print("class4")

    def m3(self):
        print("iam m3 from c4")

class c5(c4):
    def m5(self):
        print("class4")

class c6(c5):
    def m6(self):
        print("class4")
obj = c6()
obj.m3()

# ! ---------> polymorphism
# * Ploymorphism in operators
#-----> +
# print(8+8)
# print("k"+'l')
# print([1,2,3]+[4,5,6])

# print(6*7)
# l1 = [1,2,3,4]
# print(*l1)
# def f1(*args)
# l1= [1,2,3,4]
# print(l1*10)

#) Tasks
#Write the code for the belwo tasks using function
#!)>d1 = {"shirt": 1000, "pant"; 1500, "Shoes"; "900", "handkey": 30}
#a.) Find the min ans max priced product
#b.) Find the product starts with 's' and 'S'
#2.) Find then 67, is strong number or not
#3.) 11 [1,2,3,4,5,6]
#n=2> [5, 6, 1,2,3,4]
#n=3--> [4,5,6, 1,2,3]

'''





















































































