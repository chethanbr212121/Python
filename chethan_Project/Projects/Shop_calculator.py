## Write program for shop calculator to sum all the entered values untill quit.

#sum=0
#while (True):
   # num = (input("Enter the Price: \n"))
    #if num!= 'q':
        #sum = sum + int(num)
        #print(f"Total sum is:  {sum}")

    #elif num == 'q':
        #print(f"Your Total sum is: {sum} \n Thanks for shoping in \"Ramesh stores\" ")
       # break


### Write the program to print tables.
#input1=(input("Enter the number to print Tables: "))
#for i in range(1,11):
    #if input1.isdigit():
        #print(f"{int(input1)} x {i} = {i * int(input1)}")
    #else:
       # print("Enter correct number")

'''
### Simple calculator.
print("Choose correct option\n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division \n 5.Square \n "
      "6.Percentage \n 7.Interest calculation")

try:
    input3 = int(input("Choose option to perform: "))

    if input3 >= 7:
        print("Please choose the correct option")


    if input3==1:
        input1 = float(input("Enter the first number: "))
        input2 = float(input("Enter the second number: "))
        print(f"Sum of {input1} and {input2} is: {input1+input2}")

    elif input3==2:
        input1 = float(input("Enter the first number: "))
        input2 = float(input("Enter the second number: "))
        print(f"Substraction of {input1} and {input2} is: {input1-input2}")

    elif input3==3:
        input1 = float(input("Enter the first number: "))
        input2 = float(input("Enter the second number: "))
        print(f"Multiplication of {input1} and {input2} is: {input1*input2}")

    elif input3==4:
        input1 = float(input("Enter the first number: "))
        input2 = float(input("Enter the second number: "))
        print(f"Division of {input1} and {input2} is: {input1/input2}")

    elif input3==5:
        input1 = float(input("Enter the number: "))
        print(f"Square of {input1} is: {input1**2}")

    elif input3==6:
        input1 = float(input("Enter the first number: "))
        input2 = float(input("Enter the second number: "))
        print(f"Percentage of {input1} for {input2} is: {round(((input1/input2)*100),2)}%")

    elif input3==7:
        input1 = float(input("Enter the Interest rate: "))
        input2 = float(input("Enter the total amount: "))
        print(f"Percentage of {input1} for {input2} is: {round(((input1/100)*input2),2)}")



except Exception as e:
    print("Please enter only number inputs,",e)'''


'''
###calculator using function.
class Calculator:

    def addition(self,input1,input2):
        print(f"Addition of {input1} and {input2} is: {input1+input2}")

    def substraction(self,input1,input2):
        print(f"Substraction of {input1} and {input2} is: {input1-input2}")

    def multiplaction(self,input1,input2):
        print(f"Multiplication of {input1} and {input2} is: {input1*input2}")

    def division(self,input1,input2):
        print(f"Division of {input1} and {input2} is: {input1/input2}")

    def percentage(self,input1,input2):
        print(f"Percentage of {input1} for {input2} is: {round(((input1/input2)*100),2)}%")




input1 = float(input("Enter the first number: "))
input2 = float(input("Enter the second number: "))
a = Calculator()
#a.addition(input1,input2)
#a.substraction(input1,input2)
#a.multiplaction(input1,input2)
#a.division(input1,input2)
#a.percentage(input1,input2)'''





from datetime import datetime
now = datetime.now()
current_hour = now.strftime("%I")
print(current_hour)
current_minute = now.strftime("%M")
print(current_minute)
current_seconds = now.strftime("%S")
print(current_seconds)
current_period = now.strftime("%p")
print(current_period)






































































































































































