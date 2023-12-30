'''
### "print" Function.
print("He is learning python", end=",")
print("He is also learning SQL")

print("He is learning python","He is also learning SQL")

### "escape sequence's"
print("c:\n harry") #"\n" returns next line.

print("c:\" harry") # \" returns double quote.

print("c:\' harry") # \' returns single quote.

print("harry is \n good boy") #"\n" returns next line.

print("harry is \t good boy")  # \t "returns new tab.

print('http:\\\\screener.in') # \\ returns \ so if we want two \\ we need to use \\\\

# For more search in google "escape sequence".

print(15 * "Chethan")  #returns string 15 times Horizontally.

print(15 * "Chethan \n")  #returns string 15 times Vertically.


### Id,Type and Value.
#a=50
#b = 'Hello'
#print(id(a))
#print(id(b))
#print(type(a))
#print(type(b))



### "Input" function
s1 = input("Enter first number: ")
s2 = input("Enter second number: ")
print(int(s1)+int(s2))


### String slicing.
mystring = "He is very good boy"
print(len(mystring))
print(mystring[0:19:2])  # Skips one character and returned every 2nd letter.
print(mystring[:15])   # Returns from "0".
print(mystring[0:])    # Returns full string.
print(mystring[0:-4])  # (same as [0:15]  (15 is 19-4=15 here 19 is length of string) it removes last 4 characters.
print(mystring[::-1])  # It reverses the string.
print(mystring[::-2])  # It reverses the string skips one character and returned every 2nd letter.


### String functions.
string1 = "heisgoodboy"
string2 = "He is good boy"
string3 = 100.25

print(string1.isalnum())  # True (String is alphanumeric  because there is no space).
print(string2.isalnum())  # False (String is not alphanumeric  because there is a space).
print(string2.isalpha())  # False  (string is not alphabetic because space.
print(string1.isalpha())  # True  (string is alphabetic because only alpha characters present.
print(string2.isupper())  #Returns True if all characters in the string are upper case.
print(string2.istitle())  #Returns True if the string follows the rules of a title.
print(string2.isnumeric()) #Returns True if all characters in the string are numeric.
print(string2.isdigit())  #Returns True if all characters in the string are digits.
print(string2.endswith("boy"))  # True (string ends with "boy" characters).
print(string2.count("o"))  # Here "o" is present 3 times.
print(string1.capitalize()) # returns 1st letter capital.
print(string2.find("good"))  #returns position of "good" is 6th.
print(string2.upper())  # returns all upper.
print(string1.lower())  # returns all lower.
print(string2.replace("good","bad")) # replaces "good" by "bad".
print(string2.casefold())  # returns all lower.
print(string2.endswith('boy'))  # returns True because String ends with "boy".
print(string2.startswith("He")) #Returns true if the string starts with the specified value.
print(string2.isascii())  #Returns True if all characters in the string are ascii characters.
print(string2.zfill(20))  #Fills the string with a specified number of 0 values at the beginning.
print(string2.title())  #Converts the first character of each word to upper case.
print(string2.swapcase())  #Swaps cases, lower case becomes upper case and vice versa
print(string2.splitlines())  #Splits the string at the specified separator, and returns a list.
print(string2.rsplit())  #Splits the string at the specified separator, and returns a list
print(string2.split('o'))  #Splits the string at 'o' gives space insted of "o", and returns a list
print(string2.partition("He is")) #Returns a tuple where the string is parted into three parts.

string_1 = 'aaaahelloaaaa'
print(string_1.strip('a'))  ### remove "a" from left and right side of string.
str_2 = '!!!!chetu'
print(str_2.lstrip('!'))  ### remove left side characters.
str_3 = 'chetu@@@'
print(str_3.rstrip('@'))  ### remove right side characters.
str_4 = "  hello  "
print(str_4.strip())   ### It removes space from boath sides.


### "List"
l1 = []
print(type(l1)) # Returns type "list"

grocery = ["tamota","onion","butter","gee"]
print(grocery)
print(grocery[0])
print(grocery[1])
print(grocery[3])

nmbers = [2, 5,7,9,8,1]
print(nmbers)
print(nmbers[4])
print(nmbers[2])

nmbers = [2, 5,7,9,8,1]
nmbers.sort()
print(nmbers)  #returns sorted/ordered form.
print(min(nmbers))
print(max(nmbers))

nmbers = [2, 5,7,9,8,1]
nmbers.append(77)
print(nmbers)  # add "77" to end.

nmbers = [2, 5,7,9,8,1]
nmbers.insert(2,25)  #addind "25" at 2nd place.
nmbers.insert(4,28)  #addind "28" at 4th place.
nmbers.remove(8)     #removes 8.
nmbers.pop()         #removes last element.
nmbers[1] = 21       # Added 21 to 1st place.
print(nmbers)
print(len(nmbers))
print(sum(nmbers))
print(max(nmbers))
print(min(nmbers))

nmbers = [2, 5,7,9,8,1]
nmbers.reverse()
print(nmbers)

## List slicing.
list1 = ['chetu','Ramesh',5555,8547,'Ravi']
print(list1[1:1])   ## Return blank.
print(list1[1:2])   ## return 1st index 'ramesh' it will not return 2nd index.
print(list1[1])     ## return 1st index 'ramesh'.
print(list1[:])     ## Returns full list.
print(list1[1:3])   ## Returns 1st and 2nd index only, will not return 3rd index.

## Mutable - can change. ex: List.
## Immutable - Cannot change. ex: Tuple.


### "Tuple"
T1 = ()
print(type(T1)) # Returns type "Tuple"

tpp = (1,) # single character in bracket will not give "tuple" so add "," to change to tuple.
print(tpp)

tp = (1,2,5,7)
print(tp)

### "swapping"
a= 5
b= 6
a,b = b,a
print(a) #returns 6.
print(b) #returns 5.


### import function from file in same directory.
import Readharry
Readharry.module1()  ## It returns "My name is:  Chethan"
'''

#### Escape sequences.
#print('it\'s my birthday')   ## single quote is used by using " \' ".
#print("my name is: \n 'Chethan'") ## after \n prints in next line
#print("Ramesh is a \t Doctor")  ## It return space after "\t" .





























