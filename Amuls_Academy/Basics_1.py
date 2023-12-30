"""
### format function.
input1 = 8/7
print(format(input1,'0.3f'))  ## returns only 3 digits.

input2 = 'hello'
print(format(input2,'<40'))  ## returns string at left.
print(format(input2,'>40'))  ## returns string 40 characters to right.
print(format(input2,'^20'))  ## returns string centre with in 20 characters..


## identifier: Variable names are called as "identifier". ex: input2 = 20, here input2 is identifier.
## Keywords: and, or , in , for , while etc.
print(help('keywords'))  ##returns list of all keywords in python.

##Control characters: ex:\n,\ etc.


### arithmatic operations.
## Truncate division or Floor division.
print(8//2.1) ## by using "//" it will truncate the output to previous value(floor) not next value .
print(8/2.1)

## power function(**).
print(5**2) ##return 25.
print(3**2) ##return 9.


### membership operator: ex: in and not in.
list5 = [1,5,8,7,9,6,4]
print( 2 in list5)  ##False because 2 not in list5.
print( 8 in list5)  ##True because 8 in list5.
print( 2 not in list5)  ##True because 2 not in list5.


### precedence.
''' arithmetic operation priority as following
1. ()
2.**
3.unary operator
4.*,/,//,%
5. +,-
6. << >>
7. &
8. ^
9. |
10. Relational and membership operators.
11. not.
12. and
13. or
'''
print(2+5*4)  ## returns 22 here multiplication priority first and then addition.
print((2+5)*4) ## returns 28 here bracket priority first and then multiplication.
print(2+5-4)   ## returns 3 here left to right evaluation occurs because of same priority for addition and substraction.
print(3**2**2) ##here print(2**2) evaluate first and returns 4. then result 4 evaluate with 3 print(3**4) and returns 81


### For loop.
## example:1.0
for letter in "python":
    print("character is",letter)

## example:2.0
for letter in [10,20,30,40]:
    print(letter)

## example:3.0
for letter in [10,20,30,40]:
    if letter >= 25:
     print(letter," grater than 25 ")
    else:
        print(letter," Lesser than 25")


## While loop.
count = 1
while count <= 5:
    print(count)
    count = count + 1
print("thank you")

## break function.
# example:1.0
count = 0
while count <=5:
    if count ==3:
        break
    else:
        print(count)
    count = count +1
print("Thank you")

#example:2.0
for  letter in "chethan":
    if letter == 'a':
        break
    else:
        print(letter)
print("Thank you")


### continue function.
# example:1.0
for  letter in "chethan":
    if letter == 'a':   ## here it skips "a" and continue loop.
        continue
    else:
        print(letter)
print("Thank you")

#example:2.0
var = 10
while var>0:
    var = var - 1
    if var == 3:
        continue
    print(var)
print("Thank you")


## list function.
list2 = [[10,20,40],[24,45,90],[15,87,98]]
print(list2[0][1]) ##returns 20
print(list2[1])  ## returns [24,45,90].
print(list2[1][2]) ##returns 90


#example:1.0
list_1 = [10,25,45,78,98,99,64,56]
for num in list_1:
    print(num)

## list operations(replace, insert, sort, delete, append, reverse).
#list_2 = [92,25,45,78,100,99,64,84]
## replace.
#list_2[2]=3.9  ## 45 replaced by 3.9
#list_2[2:4]=(12,13,54)  ## 25,45,78 are replaced by 12,13,54.
#print(list_2)  ## returns [92, 25, 3.9, 78, 100, 99, 64, 84].

#list_new = [1,2,'orange','apple','mango']
#list_new[1] = ['Banana','Coconut']  ## Here single value "2" is replaced by list having two values.
#print(list_new)
#print(list_new[1])  ## returns ['Banana', 'Coconut']
#list_new[2:4]= ['onion']
#print(list_new)   ## here 'orange' and 'apple' are replaced by single value "onion".


## insert.
#list_2.insert(5,'chethan')  ## after 100 inserted by "chetu".
#print(list_2)   ## returns [92, 25, 3.9, 78, 100, 'chethan', 99, 64, 84]

## sort.
## if a list having either full "string" or full "number" then only we can perform sort operation.
list_4 = ['dog','cat','monkey','lion','tiger']
list_4.sort()
print(list_4)
print(list_4)

##delete.
#del list_2[6]  ## delete 99 from list_2.
#print(list_2)  ## return [92, 25, 3.9, 78, 100, 'chethan', 64, 84]
#list_5 = [10,52,68]
#del list_5     ## delete full list
#print(list_5)   ## return error because list is deleted already.

## append.
list_4.append('ramesh')  ## append is used to insert at the end only.
print(list_4)

## reverse.
list_4.reverse()  ## reverse position of elements in list.
print(list_4)

## extend.
list_1.extend([21,31,51,71]) ##in extend it takes only one arguments once so to define multiple elements use list inside
print(list_1)  ## returns [10, 25, 45, 78, 98, 99, 64, 56, 21, 31, 51, 71] at end values are added or list is extendede

list_1.extend(list_4)  ## List_4 is added to list_1
print(list_1) 

## pop
list_1.pop()  ## if we dont mention any index delete last index by default.
print(list_1)
list_1.pop(4)   ## here it delete 4th index.
print(list_1)



### tuples.
numbers1 = (10,25,85,45,78)
numbers2 = ((12,25.45),(19,25,36,78),(77,84,98,100))
print(numbers1)
print(numbers1[2])
print(numbers2[1][2])
## tuples immutable so there is no operations like sort,insert,append,delete etc

## Packing ang unpacking of tuples.
t = (1,2,3,4)
(a,b,c,d) = t  ## here we equating boat tuples
print(a)   ## retrns 1
print(b)   ## retrns 2
print(c)    ## retrns 3
print(d)    ## retrns 4


### string functions.
list_1 = [10,25,45,78,98,99,64,56]
list_2 = [52,74,89,98,65]
list_name = 'chethan'

print(list_name.count('h')) ## h present 2 times.
print(list_1.index(99))  ## 99 is present in 5th index.
print(list_1 + list_2)
## we can add one number list with another number list. we can not add number list with string list and vice versa.
## we can not add list and tuple, we can only add list with list and tuple with tuple only.


### list assignment and copying.
list1 = [10,25,74,85]
list2 = list1
print(list2)

list1[1] = 35  ## 35 will replace in both list1 and also list2.
print(list1)
print(list2)

## to overcome use list() copy.
list3 = list(list1)  ## it will give copy of list and there is no dependency on coping list1, list3 is independent.
print(list3)
list1[0] = 20
print(list1)
print(list3) ##here list2 will not be replaced.

result = [x**2 for x in [1,2,3,4]]
print(result)


## range function.
for i in range(1,11):
    print(i)


## function.
## example:1.0
def avrg(a,b,c):
    return (a+b+c)/3
print("Well Come")
result1 = avrg(10,20,30)
result2 = avrg(1,2,3)

print(result1)
print(result2)


## example:2.0
def average(n1,n2,n3):
    return (n1+n2+n3)/3.0
print("well come")
num1 = int(input())
num2 = int(input())
num3 = int(input())

result = average(num1,num2,num3)
print(result)


## example:3.0
def average(n1,n2,n3):
    return (n1+n2+n3)/3.0
print("well come")

result_1 = average(n2=5,n1=10,n3=15)
print(result_1)


## example:4.0
def average(n1,n2,n3=5):
    return (n1+n2+n3)/3.0
print("well come")

result_1 = average(n2=5,n1=10,n3=15)  ### here n3 taken 15 not 5 which is defined above.
print(result_1)


## example:5.0
def average(n1,n2,n3=5):
    return (n1+n2+n3)/3.0
print("well come")

result_1 = average(n2=5,n1=10) ## now it taken 5 because we did not define n3 here.
print(result_1)


## lambda function.
sum = lambda var1,var2 : var1+var2
print("sum is",sum(10,20))


### variable length arguments.
def func1(*mylist):
    for num in mylist:
        print(num)
func1(10,20,30)
func1(10)
func1(1,2,3,4,5,6)


### Math functions.
import math

print(math.exp(4))
print(math.e**4)
print(math.sqrt(9))
print(max(10,75,89,45))
print(min(10,75,89,45))
print(math.log(10))
print(math.modf(11.855))
print(math.pow(4,2))
print(math.pi)
print(math.degrees(math.pi))
print(math.radians(180))
print(math.factorial(4))


### modules.
import sys
print(sys.path)



### Dictionary.
my_dict1 = {1:"one",2:'two',3:"three"}
print(my_dict1)

##or
my_dict2 = {}
my_dict2['Fruit1'] = 'Apple'
my_dict2['Fruit2'] = 'Banana'
my_dict2['Fruit3'] = 'Orange'
print(my_dict2)

##or
my_dict3 = dict[(1,"one"),(2,'two'),(3,"three")]
print(my_dict1)

##or
a = [1,2,3,4]
b = ["Apple","Orange","Banana","Mango"]
my_dict4 = {}
for i in range(len(a)):
    my_dict4[a[i]] = [b[i]]
print(my_dict4)
print(my_dict4.keys())
print(my_dict2.keys())
print(my_dict4.values())
print(my_dict2.values())
print(my_dict4[2])   ## it will return 'orange'.
### or
print(my_dict4.get(2))  ## it will return 'orange'.


## create dictionary from different way.
list1 = [1,2,3,4]
print(dict.fromkeys(list1))

##or
print({}.fromkeys(range(1,7),10))


### setdefault in dictionary.
## setdefault(key,values) ## here value is optional.
## here if key is not present it will add key and values to dictionary, if key present it will add value to dictionary.
students = {'ramesh':20, 'riya':25, 'john':30}
print(students.setdefault('ramesh'))
print(students.setdefault('anabel'))
print(students)  ## here "anabel" is added to dictionary.
print(students.setdefault('ravi',24))
print(students)  ## here "ravi" as key and value 24 is added to dictionary.


### update dictionary.
list1 = [1,2,3,4]
list2 = ['a','b','c','d']
print(list1+list2)   ## we can cancatinate or update very easily.

dict1 = {1:"apple",2:"ball",3:"cat"}
dict2 = {"o":"orange"}
#print(dict1+dict2)  ## it will not return any result.

## we can update by using "update" command.
print(dict1.update(dict2))
print(dict1)  ## here we can see dict1 is updated by key"o" and value "orange".

##we can update dictionary and list boat at a time.
dict_1 = {1:"a",2:"b"}
list_1 = [3,"c"]           ## here "3" is key and "c" is value.
print(dict_1.update([list_1]))
print(dict_1)   ## here dict_1 is updated as "3" as key and "c" as value.

## we can also update by expression.
print(dict_1.update(y=3,z=4))
print(dict_1)  ## both "y" and "z" are updated.

## for same key we can replace by new value
print(dict_1)
dict_2 = {1:"apple"}
print(dict_1.update(dict_2))
print(dict_1)   ## here we can see key value "1" is updated by "apple".
dict_3 = {}
print(dict_3.update(dict_1))
print(dict_3)   ##here dict_3 is updated same as dict_1



### delete elements from dictionary.
my_dict = {1:"a", 2:"b",3:"c",4:"d"}
del my_dict[2]
print(my_dict)
print(my_dict.pop(1))
print(my_dict)
print(my_dict.clear())   ## to remove or delete whole dictionary.
print(my_dict)



### difference between list and dictionary.

## temperatre display program using dictionaries.
daily_temps = [68.8 , 71 , 67, 71.8 , 73.4, 75.5,75]

day = input("enter 'sun','mon', 'tue','wed','thur','fri',or 'sat': ").lower()

if day == 'sun':
    dayname = "sunday"
    temp = daily_temps[0]

elif day == 'mon':
    dayname = "monday"
    temp = daily_temps[1]

elif day == 'tue':
    dayname = "tuesday"
    temp = daily_temps[2]

elif day == 'wed':
    dayname = "wednesday"
    temp = daily_temps[3]

elif day == 'thur':
    dayname = "thursday"
    temp = daily_temps[4]

elif day == 'fri':
    dayname = "friday"
    temp = daily_temps[5]

elif day == 'sat':
    dayname = "saturday"
    temp = daily_temps[5]
else:
    print("please enter the correct input")
print(f"the temperatue for: {dayname} was, {temp} degrees")


## temperatre display program using list.
daily_temps = {"sun":68.8,"mon":78.2,"tue":72.1,"wed":56.5,"thur":65.6,"fri":59.5,"sat":65.9}

dayname = {"sun":"sunday","mon":"monday","tue":"tuesday","wed":"wednesday","thru":"thrusday","fri":"friday","sat":"saturday"}

day = input("enter 'sun','mon', 'tue','wed','thur','fri',or 'sat': ").lower()

print(f"the temperatue for: {day} was {daily_temps[day]} degrees")



### loop with index.
## with out using index.
color = ['red', 'blue', 'yellow']
for i in color:
    print(i)

## with using index.
for i in range(len(color)):
    print(i,color[i])

## using enumerate function.
for i,j in enumerate(color,1):  ## here "1" is index start number. if dont mention any number it will start fron zero.
    print(i,j)



### set datatype in python.
## set is an mutable data type with non duplicated, unordered values
## {} are used in sets..
fruits = {'apple', 'banana'}
print(fruits)

print(fruits.add('grapes'))
print(fruits)

## creating immutable set.
animal = frozenset({'lion','tiger','cheeta'})
print(animal)
#print(animal.add('cat'))   ## here we cannot add any elements to frozenset.

## check for duplicate values in set.
num1 = {1,2,3,1,4,3,5,2,5,6}
print(num1)  ## it will returns only distinct/unique values.

## create empty set.
emptyset = {}
print(type(emptyset))   ## it will show type as "dictionary".

emptyset1 = set()
print(type(emptyset1))  ## now it will return type as "set".

## copy set.
num = {1,2,3,4,5,6}
num1 = set(num)
print(num1)  ## copyed num value to num1.



### set operations.
##"membership" operation.
set1 = {1,2,3,4,5,'hello'}
print(6 in set1)   ##False
print(4 in set1)   ##True

## add element to set.
set1.add(6)
print(set1)  ## "6" is addede to set1.

## remove from set.
set1.remove(2)
print(set1)   ## "2" is removed from set1.

## union operation.
## union will remove duplicate elements.
set2 = {1,4,5,11,12,"apple"}
print(set1.union(set2))  ## union using union key
##or
print(set1|set2)  ## union using "|" symbol.

##Intersection operation.
## it returns only common values from two or more sets.
print(set1.intersection(set2))  ## Intersection using Intersection key.
##or
print(set1 & set2)    ## Intersection using & symbol.


## difference(like minus in sql) operation.
## it will return values present in first set which are not present on second set.
print(set1.difference(set2))  ##return values present in "set1" and not present in "set2"
print(set2.difference(set1))  ##return values present in "set2" and not present in "set1"
## or
print(set2-set1)  ## difference using "-" symbol

## symetric difference operation.
## it will returns values which are not common in two different sets.
print(set1.symmetric_difference(set2))
##or
print(set1^set2)

##length of set.
print(len(set1))
print(len(set2))

## copy sets.
set3 = set1.copy()
print(set3)

## clear operation.
set4 = {1,5,8,7,9,4,5}
print(set4)
print(set4.clear())
print(set4)



### file handling in python
text_file = open("text.txt","w")  ## it will creates file.

text_file.write("Hello \nThank you")  ## To write text to file.
text_file.close()   ## if we dont close file text will not save into file.

text_file = open("text.txt","a") ## To add more line to file open the file in "a" (append) mode and write text.
text_file.write("\nWell come to Python")  ## use "\n" to write next line.
text_file.close()

text_file = open("text.txt","r")  ## To read use "r"(read).
print(text_file.read())
text_file.close()


## Rename and Delete files.
import os
#os.rename("text.txt","text1.txt")  ## it will work to rename file in current directory only.

#text_file = open("text1.txt","r") ## reda renamed file.
#print(text_file.read())
#text_file.close()

## to get current directory.
#print(os.getcwd())  ##E:\ETL\Python Videos\Python Practice\chethan Project\Amuls Academy

## rename file using file path.
## *** here use "\\" because "\" work as escape character.
os.rename("E:\\ETL\\Python Videos\\Python Practice\\chethan Project\\Amuls Academy\\text3.txt","E:\\ETL\\Python Videos\\Python Practice\\chethan Project\\Amuls Academy\\text4.txt")

text_file = open("text4.txt","r") ## reda renamed file.
print(text_file.read())
text_file.close()


### remove file.
import os
os.remove("E:\\ETL\\Python Videos\\Python Practice\\chethan Project\\Amuls Academy\\file5.txt")

text_file = open("file5.txt","r") ## reda renamed file.
print(text_file.read())
text_file.close()



### managing directories.
import os
#os.mkdir("E:\\ETL\\Python Videos\\Python Practice\\chethan Project\\new_directory")

print(os.getcwd())  ## E:\ETL\Python Videos\Python Practice\chethan Project\Amuls Academy

## to change our current working directory to new working derectory.
os.chdir("E:\\ETL\\Python Videos\\Python Practice\\chethan Project\\new_directory")
print(os.getcwd())
## changing back to old directory.
os.chdir("E:\\ETL\\Python Videos\\Python Practice\\chethan Project\\Amuls Academy")
print(os.getcwd())

## create new directory in existin directory.
#os.mkdir("amul new")

## view sub-directories.
print(os.listdir()) ## it will give sub-directories in current working directory.

###print(os.listdir("C:\\")) ## It will give all folders in "c" drive.
###print(os.listdir("E:\\")) ## It will give all folders in "E" drive.


## remove directory.
os.rmdir("amul new")




### Exception handling.
import math
num = int(input("Enter the number to calculate factorial: "))
try:
    result= math.factorial(num)
    print(result)
except Exception as e:
    print("Plese enter positive number,", e)


## Raise ValueError with try and exception.
try:
    num = int(input("Enter a number: "))
    if num<=0:
        raise ValueError("Enter positive number")
except ValueError as e:
    print(e)


## Execute finally with try and exception.
import math
num = int(input("input: "))
try:
    result = math.factorial(num)
    print(result)

finally:
    print("Thank you")
'''Here error message will return as "Traceback". Exception is handled correctly by python thats why 
finally is printed , if it does not handled python will not execute finally'''




### class method.
class person:
    pass  ### empty class

p = person()
print(p)


## defining method in calss.
class person:
    def display(self):   ##this is method part
        print("hello")

person1 = person()    ## main function part
person1.display()

##or
class person:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("hello",self.name)

person2 = person("chetu")
person2.display()


### class and instance variables.
class student:
    clg = 'xyz'   ## Class variable.

    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name

    def display(self):
        print("student name: ",self.name)
        print("student rollnumber: ",self.rollno)
        print("college is: ", student.clg)

student1 = student('xyz001',"Ravi")
student1.display()

student2 = student('xxyz056',"Ramesh")
student2.display()


### Fundamental features of object oriented programming.
## inheritance class.
## in inheritance there are two types Base class and Derived class.
## derived class can inherit methods and variables from bace class.

## eample:1.0
class animal:   ## Base class
    def eating(self):
        print("eating")

class dog(animal):   ## This is Derived class.
    def bark(self):   ##"animal" is inherited from Base class now method eating belongs to both class.
        print("bark")

d = dog()  ## if we are not use inheritance "animal" both class will become different and we can not call d.eating here.
d.eating()
d.bark()

## eample:2.0
class animal:
    def __init__(self,name):
        self.name = name

class dog(animal):
    def display(self):
        print(self.name)

d = dog("babydog")
d.display()


## Multilevel inheritance.
class person:          ## Base class
    def display(self):
        print("Hello this is person")

class employee(person):  ## Derived class -1
    def printing(self):
        print("Hello this is derived class employee")

class programmer(employee): ## Derived class -2
    def show(self):
        print("Hello this is another derived class programmer")

p1 = programmer()
p1.display()
p1.printing()
p1.show()


## Multiple inheritance.
class land_animal:
    def printing(self):
        print("This animal lives on land")

class water_animal:
    def display(self):
        print("This animal lives in water")

class frog(land_animal,water_animal):
    pass

f1 = frog()
f1.display()
f1.printing()


## Method overriding.
class A:
    def display(self):
        print("method belong to class A")

class B(A):
    def display(self):
        print("method belongs to class B")

b1 = B()
b1.display()


### Encapsulation.
## it is used to prevent data being modified.
# Example:1.0
class car:
    def __init__(self):
        self.__updatesoftware()
    def drive(self):
        print("driving")
    def __updatesoftware(self):
        print("updating software")

blackcar = car()
blackcar.drive()


# Example:2.0
class car:
    __maxspeed = 0
    __name = ""
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "supercar"
    def drive(self):
        print("driving")
        print(self.__maxspeed)
    def setspeed(self,speed):
        self.__maxspeed = speed
        print(self.__maxspeed)

redcar = car()
redcar.drive()
redcar.setspeed(100)


## polymorphism.
class dog:
    def sound(self):
        print("bowbow")
class cat:
    def sound(self):
        print("meow")
def makesound(animaltype):
    animaltype.sound()

catobj = cat()
dogobj = dog()
makesound(catobj)
makesound(dogobj)



### Time modules.
import time
print(time.time())  ## it gives seconds from 1970
print(time.localtime((time.time()))) ## it gives current year,month,day,hour,min,sec,weekda,yearday and daylight saving.
print(time.asctime())  ## it gives current day,month,date, time in IST, year.

tuple1 = (1993,6,8,9,20,3,0,0,0)
print(time.localtime(time.mktime(tuple1))) ## it gives current year,month,day,hour,min,sec,weekda,yearday.

tuple2 = (1993,12,8,9,20,3,0,0,0)
print(time.localtime(time.mktime(tuple2)))


### Calendar module.
import calendar
print(calendar.month(2000,4))  ## Gives calender.
print(calendar.calendar(2000))
print(calendar.weekday(2000,3,9))  ## return week day.
print(calendar.isleap(2001))  ## return leap year or not by True and False.
print(calendar.leapdays(2000,2017)) ## Leap years(2000,2004,2008,2012,2016) between 2000 and 2017.
print(help(calendar))


### dir function.
import math
print(dir(math))   ## gives full key words details of modules

import  time
print(dir(time))


### Printing * in right angle triangle.
## Example:1.0
num = int(input("Enter the number of rows: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()


## Example:2.0
num = int(input("Enter the number of rows: "))
k = 1
for i in range(1,num+1):
    for j in range(1,k+1):
        print("*", end=" ")
    k = k+2
    print()


## Example:3.0
num = int(input("Enter the number of rows: "))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*", end=" ")
    print()



## Example:4.0
num = int(input("Enter the number of rows: "))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,2*i+1):
        print("*", end=" ")
    print()


## Using function.
#Example:5.0
def pyramid(rows):
    for i in range(rows):
        print(' '*(rows-i-1)+'*'*(i+1))
pyramid(5)


#Example:6.0
def pyramid(rows):
    for i in range(rows):
        print(' '*(rows-i-1)+'*'*(2*i+1))
pyramid(4)


#Example:7.0
'''here num and 0 are represent range(ex:if num=4 then range 4 to 0) and -1 represent 
decreasing downwords every step by -1 (ex: 4,3,2,1 downwords)'''

num = int(input("Enter the number of rows: "))
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()


#Example:8.0  print diamond shape.
def pyramid(rows):
    for i in range(rows):
        print(" "*(rows-i-1)+"* "*(i+1))   ## here space after "* ".
    for j in range(rows-1,0,-1):
        print(" "*(rows-j)+'* '*(j))      ## here space after "* ".

pyramid(10)


## #Example:9.0  print inverted right angle traingle shape.
num = int(input("Enter the number of rows: "))
for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()
"""

print("Hello")

































































































































