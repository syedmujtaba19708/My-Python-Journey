import requests #To use and showcase an external module we will use the requests module which is used to make HTTP requests in python.
import os #This will be of help to print the contents of a directory using the os module.

# In this after learning about modules and python introduction we will solve the following exercise:
#1. Write a program to print Twinkle twinkle little star poem in python.
#2. Use REPL and print the table of 5 using it.
#3. Install an external module and use it to perform an operation of your interest.
#4. Write a python program to print the contents of a directory using the os module.
#Search online for the function which does that.
#5. Label the program written in problem 4 with comments. 


#Program to print Twinkle twinkle little star poem
print("Twinkle twinkle little star,")
print("How I wonder what you are!")
print("Up above the world so high,")
print("Like a diamond in the sky.")
print("Twinkle twinkle little star,")
print("How I wonder what you are!")

#program to print the table of 5 in REPL. We will write it here and copy paste it in REPL to see the output.
for i in range(1,11): 
    print(f"5 x {i} = {5*i}")
    #The for range for loop is 1 and 11 because we want to print the table of 5 from 1 to 10. 
    #The loop does not multiply 11 because the range function does not include the last number in the range.

#install an external module and use it, so we will install the module called "requests" which is used to make HTTP requests in python.
#We will use it to get the content of a webpage and print it.


response = requests.get("https://www.example.com") #any webpage can be pasted here to check the content of that webpage.
#requests was installed using pip install requests command in the terminal.
print(response.text)

#Program to print the contents of a directory using the os module.
#The os module is used to interact with the operating system and perform various operations like creating, deleting, and modifying files and directories.
#The function used to print the contents of a directory is os.listdir() which returns a list of the names of the entries in the directory given by path.
#If path is not specified, the current working directory is used.
print(os.listdir(r"C:\Users\Aro\Desktop\pyt>")) #this was my path for the directory I wanted to read, change it accordingly.and
#r is used to indicate that the string is a raw string and should not be treated as an escape sequence.

#We have already labeled the program with comments explaining each step and the purpose of the code. Hence the work here ends. Arigato!