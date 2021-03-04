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
Name=input("\nEnter your name:")
str = str + Name
str+= ".Welcome to python."
print(str)

# Program to repeat a string using * operator 

str = "Hello!"
print(str *3)