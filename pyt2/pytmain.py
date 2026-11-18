#In this program we will learn about variables, and basic concepts regarding variables in Python.
a=1 #This is a basic example of a variable. Here we have stored 1 in the variable a. We can use this variable in our program to perform various operations.
b=2 #This is another variable where we have stored 2. We can use this variable in our program to perform various operations.
print(a+b) #This will print the sum of a and b which is 3.
c=a+b #Here we are storing the sum of a and b in the variable c. Now c will have the value 3.
print(c) #This will print the value of c which is 3.
#Now we can move to variable types.
name="Mujtaba" #This is a string variable where we have stored the name "Mujtaba". We can use this variable in our program to perform various operations.
age=22 #This is an integer variable where we have stored the age 22. We can use this variable in our program to perform various operations.
print("My name is",name,"and I am",age,"years old.") #This will print the name and age of the person. The output will be: My name is Mujtaba and I am 22 years old.
salary=50000.50 #This is a float variable where we have stored the salary 50000.50. We can use this variable in our program to perform various operations.
print("My salary is",salary,".") #This will print the salary of the person. The output will be: My salary is 50000.5 .
employed=True #This is a boolean variable where we have stored the value True. We can use this variable in our program to perform various operations.
print("Am I employed?",employed) #This will print the employment status of the person. The output will be: Am I employed? True
#Last is None type variable which is used to represent the absence of a value or a null value.
none_variable=None #This is a None type variable where we have stored the value None. We can use this variable in our program to perform various operations.
print("The value of none_variable is",none_variable) #This will print the value of none_variable which is None. The output will be: The value of none_variable is None
#In this program so far, we have learned about variables, and basic concepts regarding variables in Python. 
# We have learned about different data types of variables such as integer, float, string, boolean, and None type. 
#Now we will understand rules for naming variable in Python.
#Following are the rules for naming variables in Python:
#a. Variable names can only contain letters, numbers, and underscores. They cannot contain spaces or special characters.
#b. Variable names cannot start with a number. They must start with a letter or an underscore.
#c. Variable names are case-sensitive. This means that a variable named "myVariable" is different from a variable named "myvariable".
#d. Variable names cannot be a reserved keyword in Python. For example, we cannot use "if", "else", "while", "for", etc. as variable names.
#examples
my_variable = 10
_my_variable = 20
MyVariable = 30
#1myvariable = 40 #This will give an error because variable names cannot start with a number.
my_variable_1 = 50 #This is a valid variable name because it starts with a letter and contains only letters, numbers, and underscores.
# The number of total variables in Python is unlimited. We can create as many variables as we want in our program. 
# However, it is a good practice to use meaningful variable names that describe the purpose of the variable. This will make our code more readable and maintainable.
#Now we should focus a bit more on operators in Pythhon, we have already operators being used in Python. Now we will learn about all the operators in Python.
# As we did the sum before we can do others.
#First we have the arthimetic operators.
print(a-b) #This will print the difference of a and b which is -1.
print(a*b) #This will print the product of a and b which is 2.
print(a/b) #This will print the division of a and b which is 0.5.
print(a%b) #This will print the modulus of a and b which is 1.
print(a**b) #This will print the power of a and b which is 1.
print(a//b) #This will print the floor division of a and b which is 0.
print(a==b) #This will print the comparison of a and b which is False.
#Then we have the comparison operators.
print(a!=b) #This will print the comparison of a and b which is True.
print(a>b) #This will print the comparison of a and b which is False.
print(a<b) #This will print the comparison of a and b which is True.
print(a>=b) #This will print the comparison of a and b which is False.
print(a<=b) #This will print the comparison of a and b which is True.
#Then we have the logical operators.
print(a and b) #This will print the logical AND of a and b which is 2.
print(a or b) #This will print the logical OR of a and b which is 1.
print(not a) #This will print the logical NOT of a which is False.
print(not b) #This will print the logical NOT of b which is False.
#We should also look at the truth tables to understand the behavior of logical operators.
d = True
e = False
d and e #This will print the logical AND of d and e which is False.
d or e #This will print the logical OR of d and e which is True.
not d #This will print the logical NOT of d which is False.
not e #This will print the logical NOT of e which is True.
#Then we have the assignment operators.
a=b #This is an assignment operator which is used to assign the value of b to a. Now a will have the value 2.
print(a) #This will print the value of a which is 2.
a+=b #This is a shorthand operator which is equivalent to a=a+b. Now a will have the value 3.
print(a) #This will print the value of a which is 3.
b-=a #This is a shorthand operator which is equivalent to b=b-a. Now b will have the value -1.
print(b) #This will print the value of b which is -1.
a*=b #This is a shorthand operator which is equivalent to a=a*b. Now a will have the value -3.
print(a) #This will print the value of a which is -3.
b/=a #This is a shorthand operator which is equivalent to b=b/a. Now b will have the value 0.3333333333333333.
print(b) #This will print the value of b which is 0.3333333333333333.
#We can do multiple functions on float and on strings as well. We can use the built-in functions in Python to perform various operations on float and string variables.

#Type and Type Conversion
type(a) #This will print the type of variable a which is <class 'int'>.
type(b) #This will print the type of variable b which is <class 'float'>
type(name) #This will print the type of variable name which is <class 'str'>.
type(salary) #This will print the type of variable salary which is <class 'float'>.
type(employed) #This will print the type of variable employed which is <class 'bool'>.
t = type(c) #This will print the type of variable c which is <class 'int'>.
print(t) #This will print the type of variable c which is <class 'int'>
a_string="2" #This is a string variable where we have stored the string "2". We can use this variable in our program to perform various operations.
type(a_string) #This will print the type of variable a_string which is <class 'str'>.
#Now to convert this to an integer we can use the int() function.
a_int=int(a_string) #This will convert the string "2" to an integer
b_float=float(a_string) #This will convert the string "2" to a float
print(a_int) #This will print the value of a_int which is 2.
print(b_float) #This will print the value of b_float which is 2.0.
#We can also convert an integer to a string using the str() function. But we cannot convert a float to an integer using the int() function if we do some of it will be lost.
float_a=0.1
int_a=int(float_a) #This will convert the float 0.1 to an integer which is 0. 
# We can only convert a float to an integer using the int() function if the float is a whole number. Otherwise, it will give an error.
#e_float=float(name) #This will give an error because we cannot convert a string of words to a float.
#e_int=int(name) #This will give an error because we cannot convert a string of words to an integer.
#Now to get value from user we can use the input() function. The input() function takes input from the user and returns it as a string. 
# We can then convert it to the desired data type using the int(), float(), or str() functions.
value= input("Enter a value: ") #This will take input from the user and store it in the variable value. The input will be stored as a string.
print("The value you entered is",value) #This will print the value entered by the user. The output will be: The value you entered is <value>.
t=type(value) #This will print the type of variable value which is <class 'str'>.
print(t) #This will print the type of variable value which is <class 'str'>.
#If we do a sum
v=input("Enter a value: ") #This will take input from the user and store it in the variable v. The input will be stored as a string.
print(v+v) #This will print the value entered by the user twice. The output will be: <value><value>. 
#This is because the input is stored as a string and when we use the + operator on strings, it concatenates them.
#The type of the value entered by the user will be string. We can convert it to the desired data type using the int(), float(), or str() functions.
#Or we can use the eval() function to evaluate the input and return it as the appropriate data type. 
# The eval() function takes a string as input and evaluates it as a Python expression.
int_value=int(input("Enter a value: ")) #I have used the int() function to convert the input to an integer. The input will be stored as an integer.
print("The value you entered is",int_value) #This will print the value entered by the user. The output will be: The value you entered is <value>.