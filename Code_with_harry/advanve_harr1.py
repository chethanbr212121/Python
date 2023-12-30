
## Exception usage in program.
## example: 1.0
#while(True):
    #print("Press q to quit")
   # a = input("Enter a number: ")
    #if a == 'q':
       # break
    #try:
        #a = int(a)
       # if a>6:
            #print("You entered grater than 6")
        #elif a==6:
            #print("You entered number equal to 6")
        #else:
            #print("You entered number less than 6")

    #except Exception as e:
       # print(f"Please enter the numbers only {e}")   ## If we print "e" it shows what type of error.
                                                      ## If we don't want to see what type of error, dont print "e".
#print("Thanks for playing this game")



## example:2.0 different way of handling exception.
#try :
    #a = int(input("Enter a number : "))
    #c = 1/a
    #print(c)
#except ValueError as e:
    #print("Please enter a valid value") ## here we are not printing error message.


#except ZeroDivisionError as e:
    #print("Make sure you are not dividing by 0")

#print(" Thanks for using this code")




## Raising exception.
## We can define error and print them when error occurs
#def increment(num):
    #try:
        #return int(num) + 1
   # except:
        #raise ValueError("Please enter correct number")
#a = increment(10)
#print(a)


### Use "else" in exception.
#try:
     #a = int(input("Enter a number: "))
     #c = 1/a
    # print(c)
#except Exception as e:
     #print(e)
#else:
    # print("We are successful")


### try except by using "finally".
## It will print this message irrespective of even progarm execute or exit or Program rise exception also.
#try:
     #a = int(input("Enter a number: "))
     #c = 1/a
    # print(c)
#except Exception as e:
    # print(e)
     #exit()
#finally:
    # print("We are done")



## if__name__ == "__main__" usage
## "__main__" shows function is running in a same file (because in some cases we may use function in different file also).
#def greet (name):
   # print(f"Good morning, {name}")
#print(__name__)
#if __name__ == "__main__":
    #name = input("Enter a name:\n")
 #   greet(name)


### Global and Local variables.
## without using global key word.
#a= 54  ## Global variable.
#def func():
    #a = 8  ## Local variable.
    #print(a)  ## Returns Local variable.
#func()
#print(a)  ## Returns Global variable.


## with using global key word.
#a= 54  ## Global variable.
#def func():
   #global a
    #print(f"print statement 1: {a}")  ## Returns Global variable.
    #a = 8  ## Local variable.
    #print(f"print statement 2: {a}")  ## Returns Local variable.
#func()
#print(f"print statement 3: {a}")  ## Returns "8" because local variable will become global variable by defining "global".



### "enumerate" function.
## Without enumerate.
#list1 = [3, 53, 2, False, 6.2, "Harry"]
#index = 0
#for item in list1:
   # print(item, index)
    #index += 1


## With enumerate.
#list1 = [3, 53, 2, False, 6.2, "Harry"]
#for index, item in enumerate(list1):
   # print(item, index)


##list comprehensions.
## Used to create new list from existing list based on condition.
#example:1
#a = [3,6,7,8,9,2,4,23,75,23,123,67]
#b = []
#for item in a:
    #if item%2==0:
       # b.append(item)
#print(b)

#short cut for list comprehensions in another way.
#a = [3,6,7,8,9,2,4,23,75,23,123,67]
#b = []
#b = [i for i in a if i%2 == 0]
#print(b)  ## returns all the values of even numbers in list "b" from list "a".

#example:2
#list1 = [1,8,95,4,56,25,45,21,14]
#list2 = []
#list2 = [i for i in list1 if i>8]
#print(list2)   ##return all the values grater than 8 in list2 from list1.


## Assignment:1
''' Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not present, a message 
without exit the program must be printed prompting the same'''
#def readfile(filename):
    #try:
        #with open(filename,"r") as f:
           # print(f.read())
    #except FileNotFoundError:
        #print(f"File {filename} is not found")
#readfile("1.txt")
#readfile("2.txt")
#readfile("3.txt")
#readfile("4.txt")  ## 4.txt file is not created so it returns file is not found.



## Assignment:2
''' Write a program to print third, fifth, and seventh element from a list using enumerate function.'''
#list1 = [1,2,3,4,5,6,7,8,9]
#for index, item in enumerate(list1):
    #if index ==2 or index ==4 or index==6:
     #print(f"The {index + 1}th element is {item}")

##or
#alist = [1,2,3,4,5,6,7,8,9]

#for index, i in enumerate(alist[2:len(alist)-2:2]):
    #print(index,i)




## Assignment:3
'''Write a list comprehension to print a list which contains the multiplication table of a user entered number '''
#num = int(input("Enter your number: "))
#table = [num*i for i in range(1,11) ]
#print(table)




## Assignment:4
'''Write a program to display a/b where "a" and "b" are integers. If b=0, then dispaly infinity by handling 
the ZerodivisionError'''
#a = int(input("Enter the first number: "))
#b = int(input("Enter the second number: "))
#try:
    #c = a / b
    #print(c)
#except:
    #print("Infinite")



## Assignment:5
'''Store the multiplication tables generated from a program in a file name Table.txt'''
#num = int(input("Enter the table number: "))
#table = [num*i for i in range(1,11) ]
#print(str(table))
#with open("tables.txt","a") as f:
    #f.write(str(table))
    #f.write('\n')



###lambda function.
##It is used in the place of function(def func():).

#func = lambda a: a+5
#square = lambda x:x*x
#sum = lambda a,b,c:a+b+c

#x = 3
#print(func(x))
#print(square(x))
#print(sum(x,1,2))



### Join function.
## Join is used to join strings from "List" or "Tuple" etc.
#line = [ "camers","laptop","phone","hear phone","Hard disk"]
#sentence = " and ".join(line)  ## It returns "and" after every string insted of "," in list.
#sentence1 = " \n ".join(line)   ## It returns strings one below one vertically.
#print(sentence)
#print(sentence1)


### Formating function.
## It is used before introduction of ' f"chetu {} " ' function to python for formating.
#name = "Chethan"
#channel = "Code by yourself"
#type = "coding"
#a= "This is {} and his channel is {}".format(name,channel)
#a1= "This is {0} and his {2} channel is {1}".format(name,channel,type)  ## using index inside curly-brace
#print(a)
#print(a1)


### map function.
#def square(num):
    #return num*num
#line1 = [1,2,4]

#method:1
#line2 = []
#for item in line1:
   # line2.append(square(item))
   # print(line2)

#method:2 using "map"
#print(list(map(square,line1)))  ## Returns square root for list(line1).



### filter function.
#def grater_than_5(num):
    #if num > 5:
       # return True
    #else:
        #return False

#g10 = lambda num: num>10  ## we can replace function by lambda.

#l1 = [1,25,4,25,48,52,5,85,9,68,454,12,54]
#print(list(filter(grater_than_5,l1)))
#print(list(filter(g10,l1)))



### Reduce function.
#from functools import reduce

#sum = lambda a, b: a+b

#l2 = [1,2,3,4]
#val = reduce(sum,l2)
#print(val)



### Assignment.
'''Write program by taking input like name, marks and phone number and write sentence like "My name is chethan,
My marks is 423 and my phone number is 9156234587'''

#input1 = str(input("Enter the name: "))
#input2 = int(input("Enter you marks: "))
#input3 = int(input("Enter your phone number: "))

#print(f"My name is {input1}, My marks is {input2} and My phone number is {input3}")


### Assignment.
## Return 7th multiplication table in verticle.
#l2 = [str(i*7) for i in range(1,11)  ]  ## if we are not convert to string it will through error.

#print(l2)

#verticaltable = "\n".join(l2)
#print(verticaltable)


### Write the numbers divisible by 5.

#l3 = [5,25,45,40,87,56,89,90,100,565,210]

#a = filter(lambda a: a%5 == 0, l3)
#print(list(a))


### Write a program to find maximum of the number in list using reduce function.
#from functools import reduce
#l4 = [1,5,8,6,2,5,4,9,8,54,52,155,55]

#a = reduce(max,l4)
#print(a)


























