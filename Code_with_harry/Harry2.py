""" ### "Dictionary".
d1 = {}
print(type(d1))

d2 = {"Harry":"Roti", "Ramesh": "Rice", "Suresh":"Fish", "Subham":{"Lunch":"Meals","Dinner":"Fruits"}}
d2["Ankith"]="Meat" #Adding new items.
## Here "Subham" is dictionary itself inside a dictionary.
d2["Ravi"] = "Chicken"
del d2["Ravi"]  # Delete "Ravi" from dictionary.
print(d2)
print(d2["Harry"])
print(d2["Ramesh"])
print(d2["Subham"])
print(d2["Subham"] ["Lunch"])
print(d2["Subham"] ["Dinner"])
print(d2.get("Harry"))

d3 = d2.copy() ## to copy the dictionary.
print(d3)
d3.update({"Shashi":"Tea"}) #add new items to dctionary.
print(d3)
print(d3.keys())
print(d3.items())

### Assignment:1.0
## print value from dictionary using "input" function.

d2 = ({"Harry":"Roti", "Ramesh": "Rice", "Suresh":"Fish", "Subham":{"Lunch":"Meals","Dinner":"Fruits"}})
d3 = input("Enter Name : ")
print(d2[d3])


### Assignment:1.1
## Prepare dictionary of word meanings using "input" function.

d2 = ({"good": "ಒಳ್ಳೆಯ",
       "bad": "ಕೆಟ್ಟ",
       "work":"ಕೆಲಸ"})
d3 = input("Enter Name : ").lower()  #LOWER USED to convert upper input to match dictionary keys(lower).
print(d2[d3])


### "SET"
s = set()
print(type(s))
l = [1,2,3,4,5]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))

s.add(1)
s.add(1)
s.add(2)
print(s)  ##result print "1" only once because set will retains only unique values(No duplicate).

s1 = s.intersection({1,2,3})
print(s, s1)
s2 = s.union({1,2,3,4})
print(s,s2)
print(min(s2))
print(len(s2))
print(max(s1))
s2.remove(4)
print(s2)


### if,else & elif functions.
var1= 6
var2= 56

var3 = int(input("Enter input: "))
if var3>var2:
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("Lesser")

list = [5,7,3]

if 5 in list:
    print("Yes it is in the list")


###Assignment 2.0
Qualification_age=18
Upper_age_limit = 66
Age=int(input("Enter your age: "))

if Age>Qualification_age and Age<Upper_age_limit:
    print("you are qualified to drive")
elif Age==Qualification_age:
    print("Apply for license")
else:
    print("you are not qualified to drive")



### Assignment calculator.
operation1 = "*"
operation2 = "/"
operation3 = "+"
operation4 = "-"
#operation5 = "^2"
input3=input("Enter Operation to perform: " )
input1=int(input("Enter the first number: "))
input2=int(input("Enter the second number: "))


if input3==operation1:
    print(input1*input2)

elif input3==operation2:
    print(input1 / input2)

elif input3==operation3:
    print(input1+input2)

elif input3==operation4:
    print(input1-input2)

#elif input3==operation5 :
#    input5 = int("Enter the number: ")
#   print(pow(input5,2))

else:
    print("Enter correct number")



### for loop function.
## for loop print result until the number of items in dictionary or in list lasts.
list1 = [["Harry",19],["Girry",21],["Garry",15],["Marry",52]]

dict1 = dict(list1)

for item in list1:   #returns through list.
    print(item)

for item in dict1.items():  #returns through dictionary.
    print(item)

for item in dict1:  #returns only keys through dictionary.
    print(item)


### Assignment use list and print numbers grater than 6.
items = ["chetu",6,25,58,67,54,99,100,250]

for item in items:
    if str(item).isnumeric() and item>6:
        print(item)


### while loop function.
## while loop runs until the conditions is false.
i = 0
while (i<45):
    print(i)
    i = i + 1


### Break and Continue functions.
i = 0
while (True):
    if i+1<5:
        i = i + 1
        continue  # starts printing only after "i+1=5"

    print(i+1, end=" ")
    if (i==44):
        break      #loop will stop.
    i = i + 1


### Assignment use input function and write loop untill it reaches 100.

while(True):
    i = int(input("Enter the number: \n "))
    if (i>100):
        print("Congrats you entered number grater than 100")
        break
    else:
        print("Try again \n")
        continue



### Assignment  Guess the number.
i1=21
Number_of_guessess = 1
Total_number_of_Guessess = 6
print(f"Number of guessess is limited to only {Total_number_of_Guessess} times: ")
while (Number_of_guessess<= Total_number_of_Guessess):
    i=int(input("Enter the number: "))

    if i>i1:
        print("Enter lesser number than this \n try again!")
    elif i<i1:
        print("Enter grater number than this \n try again!")
    elif i == i1:
        print("Your guess is correct, Congrats you won")
        print(Number_of_guessess, "no of guessess took to finish")
        break
    print(Total_number_of_Guessess - Number_of_guessess, "no of guessess left")
    Number_of_guessess = Number_of_guessess + 1
if (Number_of_guessess> Total_number_of_Guessess):
    print("Game over")




### Operators in python
# Arithmetic operator. (+,-,*,/)
# Assignment operator.
# Comparison operator. (>,<,>=,<=)
# Logical operator.
# Identity operator. (is , is not)
# Membership operator.
# Bitwise operator.

# Assignment operator.
y = 5
print(y)
y +=7  # we can use "-=" also.
print(y)
y *= 5   # we can use "/=" also.
print(y)

# Logical operator.
a = True
b = False
print(a or b)

# Membership operator.
list1 = [1,25,45,68,57]
print(45 in list1)


### Functions and Docstrings.
def myfunc(a,b):
    print("Hello this is function", a+b)

myfunc(3,8)

def myfunc2(a,b):
    ''' This is a function which will calculate average of two numbers, it will not work for three numbers'''
    average = (a+b)/2
    return average

v= myfunc2(5,7)
print(v)
print(myfunc2.__doc__) #returns Docstrings.


### Try Except Exception Handling.
num1 = (input("Enter the 1st number: "))
num2 = (input("Enter the 2nd number: "))

try:
    print(int(num1)+int(num2))  #enter string here to get error .
except Exception as e:
    print(e)

print("This is very important")



### Python file IO basics.
''' "r" - open file for reading (default mode).
"w" - oepen a file for eriting.
"x" - create file if not exist.
"a" - Add more contents to a file.
"t" - text mode (default mode).
"b" - binary mode.
"+" - read and write
'''
f = open("Harry1.py","r")
#content = f.read()
#print(content)

#content = f.read(50)  ##read first 50 characters.
#print(content)

#for line in f:         # used to read line by line.
#   print(line, end="")

#print(f.readline())  # print 1st line.
#print(f.readline())  # print 2nd line.
#print(f.readline())  # print 3rd line.

f.close()


### Writing and Appending to a file.
f = open("Readharry.py", "w")
f.write("Harry is bad boy \n")
f.close()

f = open("Readharry.py", "r+")
print(f.read())
f.write("Thank you")


f = open("Readharry.py")
print(f.tell())
print(f.readline())
print(f.tell())  #where reader present
f.close()


with open("Readharry.py") as f:
    a= f.read(4)
    print(a)


### Recursions : Recursive v/s iterative approach.
## factorial using iterative method.

def factorial(n):
 '''
    :param n:  Integer
    :return:  n * n-1 * n-2 * n-3 .........1
    '''

    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

number = int(input("Enter the number: "))

print(factorial(number))


## Recursive using iterative method.
def factorial_recursive(n):
    '''
    :param n:  Integer
    :return:  n * n-1 * n-2 * n-3 .........1
    '''
    if n== 1:
        return  1
    else:
        return n * factorial_recursive(n-1)

    # 5 * factorial_recursive(4).
    # 5 * 4 * factorial_recursive(3).
    # 5 * 4 * 3 * factorial_recursive(2).
    # 5 * 4 * 3 * 2 * factorial_recursive(1).
    # 5 * 4 * 3 * 2 * 1 = 120

number = int(input("Enter your number: "))
print("Facorial using recursive method", factorial_recursive(number))


### Assignment Print * like pyramid.
print("How many row you want to print: ")
one = int(input())
print("Type 1 or 0")
two = int(input())
new = bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(i+i+1):
            print("*", end=" ")
        print()
elif new == False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()


## "Lambda" functions or "anonymous" functions.
minus = lambda x,y: x-y
print(minus(9,5))

##or  Boath are gives same result.
def minus(x,y):
    return x-y
print(minus(9,5))

## example of usage of lambda
def a_first(a):
    return a[1]

a = [[1,14],[5,6],[8,23]]
a.sort(key=a_first)
print(a)

## we can create same by using lambda without using function.
a = [[1,14],[5,6],[8,23]]
a.sort(key=lambda x:x[1])
print(a)


## Assignment Health Management System.
# Health Management System
# 3 clients - Harry, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


#bhai ye rha program
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("harry-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("harry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("hammad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")
print("health management system: ")
a=int(input("Press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    take(b)
else:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    retrieve(b)


## using python external and built in modules.
import random
random_number = random.randint(0,5)
print(random_number)     ## Returns random numbers between "0" and "5".

rand = random.random()*1000
print(rand)    ## Returns random numbers between "0" and "1000".

list = ["star plus","DD1","Zee","Colours"]
choice = random.choice(list)
print(choice)   ##Returns random string from the list.



## F - String and String Formating.
import math

me = "chetu"
a1 = 3
a = "This is {0} {1}"    ## here "0" is "Chetu" and "1" is "3".
b = a.format(me,a1)
print(b)

## F - string
a = f"this is {me} {a1} {math.cos(65)}"
print(a)



### "*args" and "**kwargs" functions.
def funcargs(normal,*args,**kwargs):  ##normal arguments should be passed before "*args".
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would like to introduce some of our employees")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")
har = ["chetu","harry","rohan","ravi","ramesh"]
normal = "I am a normal argument and the students are: "
kw = {"rohan":"Monitor","Harry":"Fitness trainer","Ravi":"coder", "Shivam":"cook"}
funcargs(normal,*har, **kw)



### "Time" module in python.
import time

initial = time.time()
print(initial)
k = 0
while (k<45):
    print("This is harry")
    ##time.sleep(2)  ## return result every 2 seconds
    k+=1
print("While loop ran in", time.time()-initial,"seconds")

initial2 = time.time()
for i in range(45):
    print("This is harry")
print("for loop ran in", time.time()-initial2,"seconds")

## Find local time.
localtime = time.asctime(time.localtime((time.time())))
print(localtime)


### How to import works in python.
import sys
print(sys.path)  ##returns path

## import "a" value from "Readharry" file.
import Readharry
print(Readharry.a)
Readharry.printvalue("This is me")



### Creating our first class in python.
class student:
    pass

harry = student()

harry.name = "Harry"
harry.std = "12th"
harry.section = "A"
harry.subjects = ["Kannada","Science","English","Maths"]

print(harry.section)
print(harry.std)
print(harry.subjects)
print(harry.subjects[1])


### Instances and class variables.
class employee:
    number_of_leaves = 8  ## this is class variable it can be accessed by harry and rohan instances also.
    pass

harry = employee()
rohan = employee()

harry.name = "Harry"
harry.salary = "10000"
harry.role = "Tester"

rohan.name = "Rohan"
rohan.salary = "12000"
rohan.role = "Lead"

print(rohan.name)
print(harry.number_of_leaves)  ## we can access class variable by any instances.
print(rohan.number_of_leaves)  ## we can access class variable by any instances.
print(rohan.__dict__)          ## returns dictionary of the rohan instances.
rohan.number_of_leaves = 9     ## here it will add to rohan instances and it will not change class variable.
print(rohan.number_of_leaves)
print(rohan.__dict__)
print(employee.number_of_leaves)   ## it will retuns "8" i.e. employee class variable.
employee.number_of_leaves = 10
print(employee.number_of_leaves)  ## here employee instances is changed to 10 from 8.


### self & __init__() (Constructors).

## "self" function.
class employee:
    number_of_leaves = 8

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

harry = employee()
rohan = employee()

harry.name = "Harry"
harry.salary = "10000"
harry.role = "Tester"

rohan.name = "Rohan"
rohan.salary = "12000"
rohan.role = "Lead"

print(rohan.printdetails())
print(harry.printdetails())


## Constructor function.
class employee:
    number_of_leaves = 8

    def __init__(self,aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

harry = employee("Harry", 10000," Testor")

print(harry.salary)
"""













