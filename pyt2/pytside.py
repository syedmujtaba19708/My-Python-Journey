# 1. Write a python program to add two numbers.
# 2. Write a python program to find remainder when a number is divided by z.
# 3. Check the type of variable assigned using input () function.
# 4. Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. 
# 5. Write a python program to find an average of two numbers entered by the user.
# 6. Write a python program to calculate the square of a number entered by the user.

#Program to sum to numbers
a=int(input("Enter first number: ")) #This will take input from the user and store it in the variable a. The input will be stored as an integer.
b=int(input("Enter second number: ")) #This will take input from the user and store
sum=a+b #This will add the two numbers and store the result in the variable sum.
print("Sum =",sum) #This will print the sum of the two numbers entered by the user. The output will be: Sum = <sum>.

#Time to find the remainder when a number is divided by 2
number=int(input("Enter a number: ")) #This will take input from the user and store it in the variable number. The input will be stored as an integer.
remainder=number%2 #This will find the remainder when the number is divided by 2 and store it in the variable remainder.
print(" the remainder=", remainder) #This will print the remainder when the number is divided by 2. The output will be: The remainder = <remainder>.

#Program to check the type of variable assigned using input() function
user_input=input("Enter a number") #This will take input from the user and store it in the variable user_input. The input will be stored as a string.
print("The type of entered number:",user_input, "=", type(user_input)) #This will print the type of variable user_input which is <class 'str'>.

#To find two numbers are greater or not, user has already entered two numbers before so we will use them
print(" Is", a, "greater than ", b, "=", a>b) #This will print the comparison of a and b which is True or False.

#To find average we already have two entered numbers so we will use them as well. 
print("Average of", a, "and", b, "is: ", (a+b)/2) #This will print the average of a and b which is (a+b)/2.

#To calculate the square of a number entered by the user for which we already have a number entered by the user so we will use that as well.
print( "Square of", number, "is:", number**2) #This will print the square of the number entered by the user which is number**2.