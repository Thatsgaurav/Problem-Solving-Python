# Program to traverse a string using indexing 

msg = "Hello!"
index = 0;
for i in msg:
    print("msg[",index,"]=",i)
    index += 1;

# Program to concatenate two string + operator

str1 = "Hello"
str2 = " World!"
str3 = str1 + str2
print("Concatenated string is :",str3)

# Program to append a string using + operator 

str="Hello!"
Name=input("\nEnter your name :")
str = str + Name
str+= ".Welcome to python."
print(str)

# Program to repeat a string using * operator 

str = "Hello!"
print(str *3)

# Program to use format sequences 

name = "Gaurav"
age = 9 
print("Name = %s and age = %d"%(name,age))
print("Name = %s age = %d"%("Gaur",8))

# ---------------------------------------------- >>>>
print ("Hello, I am {} years old !".format(18))

# Program to demonstrate slicing operation

str = "PYTHON"
print("str[1.5] = str[1:5]")