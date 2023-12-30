### Special operators.
## "is" and "is not" function.
#a = 1000
#b = 1005
#print(a is b)  ## returns False because "a" is not equal to "b".
#c= 1000
#print(a is c)  ## returns True because "a" is equal to "c".
#print(b is not c)  ## returns True because "b" is not equal to "c".


## "in" and "not in" functions.
#a = ['h', 'b', 'c', 'd', 't' ,'s']
#print("h" in a )  ## return True because "h" is present in a.
#print("z" not in a)  ## return True because "z" is not present in a.

## math module functions.
import math
#print(math.pi)
r = 3
#print(2 * math.pi * r)  ## "2*pi*r.

#print(math.tau)  ## 2*pi or ratio of circle circuferance to it's radius.

#print(math.e)  ## euler's number.

#print(math.inf) ## Infinity.
#print(type(math.inf))
#print(-math.inf)
#print(math.inf>100000000000)    ###returns True because infinity is grater than any value.
#print(math.inf+100)   ## any thing with infinity is infinity only.

#print(math.nan)
#print(type(math.nan))

#print(math.factorial(5))

#print(math.ceil(21.25))

#print(math.floor(21.999))

#print(math.trunc(21.598545))

#print(math.perm(10,6))  ## Permutation.

#print(math.comb(10,6))  ## Combinations.

#print(math.gcd(10,20,25,45,75,60,90))  ### greatest common divisior.

#print(math.lcm(10,50))   ## LCM Least common multiple.

#print(math.pow(3,2))

#print(math.exp(2))  ## exponential function.

#print(math.log(2))
#print(math.log(2,3))

#print(math.log2(6))

#print(math.log10(8))

#print(math.sqrt(25))

#print(math.sin(3.14))

#print(math.asin(0.66))

#print(math.sinh(3.14))

#print(math.asinh(3.14))


### if , elif and else statements.
## Simple if statement.
age = 26
x = 'Adult' if age >18 else 'Child'
#print(x)

## "Pass" statement.
if age >18:
    pass  ## pass used where we want write block of code but it is not implemented yet, may be will write in future.


### "While" loop.
#a = [1,2,3,4,5]
#x = 1
#while a:
  #  print('This is iteration number: ', )
    #x +=1
   # print(a)
    #a.pop()  ## It will remove last element in evert iteration.


## Break and continue function.
#n = 0
#while n<5:
  #  print("value of n is: ",n)
  #  n+=1
  #  if n == 2:
  #      break
  #  print("hello")


#n = 0
#while n<5:
 #   print("value of n is: ",n)
 #   n+=1
 #   if n == 2:
  #      continue
  #  print("hello")   ## when n == 2 it will not print "hello".


## Project- 1 factorial of numbers.
#number = int(input("Enter the number: "))
#fact = 1

#if number == 0:
 #   result = 1
#
#else:
#     while number >= 1:
#        fact = fact * number
#        number = number - 1
#     result = fact

#print(f'factorial is {result}')


## Project- 2 fibbonachi numbers.
#count = int(input("How many fibbonachi number would you like to generate: "))
#i = 1

#if count == 0:
#    fib = [ ]
#elif count ==1:
#    fib = [1]
#elif count == 2:
#    fib = [1,1]
#elif count>2:
 #   fib = [1, 1]
 #   while i < (count-1):
 #       fib.append(fib[i] + fib[i-1])
 #       i +=1
#print(fib)


### For loop.
#a = [1,2,3,4,5,6]
#for x in a:
 #   print(x)

##or
#a = [1,2,3,4,5,6]
#for i in range(len(a)):
    #print(i)   ## It also give same result as above.

### For loop in dictionary's
#b = {'first':1,'second':2,"third":3,'fourth':4}
#for i in b:
 #   print(i)  ## It only print key's.

## to print values.
#b = {'first':1,'second':2,"third":3,'fourth':4}
#c = iter(b.values())
#for i in c:
 #   print(i)


### If statements in python.
## project:1.0
#orange_quality = "fresh"
#orange_price = 4.0

#if orange_quality == "fresh":
   # if orange_price <5:
        #print("I will buy 5 kg of orange")

    #lse:
        #print("I will buy 2 kg of orange")
#else:
    #print("I will not buy any orange")

## project:2.0
#inp_num = int(input("Please enter the number: "))

#if inp_num>=1 and inp_num<=20:
    #print("You entered valid number")

    #if inp_num %2 == 0:
       # print("Your number is even")
    #elif inp_num %2 == 1:
       # print("Your number is add")

#else:
    #print("Enter the valid number")


### File handling in python.
#of = open("file_hand.txt","r")  ## For text file open as read
#of1 = open("ph00124.png","rb")  ## For Binary file open as read

## Read([n]) is used for read file. if we dont specify anything reads full text. if we specity any number reads in terms of characters.
## Readline([n]) is used read each line one by one. if we specity any number reads in terms of characters.
## Readlines([n]) is used for read lines in  file.if we dont specify anything reads all lines.if we specity reads in terms of lines.

#my_file = open('reader_file.txt','w')

#my_file =open('reader_file.txt','a')
#my_file.write('Hi how are you \nPython \nSQL \nPandas \nOracle')
#my_file.close()

## "Read" function.
#my_file = open("reader_file.txt",'r')
#print(my_file.read())
#my_file.close()

#my_file = open("reader_file.txt",'r')
#print(my_file.read(10))   ## Here it reads only 10 characters.
#my_file.close()

## "Readline" function.
#my_file = open("reader_file.txt",'r')
#print(my_file.readline())   ## Here it reads only one/ first line once.
#print(my_file.readline())   ## Here it reads only one/ second line once.
#print(my_file.readline())   ## Here it reads only one/ third line once.
#my_file.close()

#my_file = open("reader_file.txt",'r')
#print(my_file.readline(5))   ## Here also reads 5 characters from first line.
#print(my_file.readline(5))   ## Here also reads 5 characters from second line.
#print(my_file.readline(5))   ## Here also reads 5 characters from third line.
#my_file.close()

## "Readlines" function.
#my_file = open("reader_file.txt",'r')
#print(my_file.readlines())   ## Here reads all lines.
#my_file.close()


## For loop in file handling
#my_file = open("reader_file.txt",'r')
#for line in my_file:
#    print(line)

## To read line from file using input function.
#line_number = int(input("Enter the line number to print: "))
#my_file = open("reader_file.txt",'r')
#current_line = 1

#for line in my_file:
    #if(current_line==line_number):
       # print(line)
        #break

    #current_line +=1



### Image file handling.(InComplete).
#import numpy as np
#from PIL import Image, ImageDraw, ImageFont
#from IPython.display import display
#import matplotlib.pyplot as plt

#location1 = r'Nature1.jpg'
#loaction2 = r'Nature2.jpg'

#im1 = Image.open(location1)
#im2 = Image.open(loaction2)

#print(im1.format, im1.size, im1.mode)
#print(im2.format, im2.size, im2.mode)


### Object oriented programming.







































