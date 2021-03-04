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
str =  "PYTHON"
print("str[-1]=",str[-1])
print("str[-6]=",str[-6])
print("str[-2]=",str[-2:])
print("str[:-2]=",str[:-2])
print("str[-5:-2]=",str[-5:-2])

#Check if the string starts with "The" and ends with "Spain":

import re
txt = input("Enter Your text :")
x = re.search("^The.*Spain$", txt)
if (x):
  print("YES! We have a match!")
else:
  print("No match")



# ------------------------------------------------------------->>>>>

# write a function that takes a list of words and 	returns the length of longest one

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])