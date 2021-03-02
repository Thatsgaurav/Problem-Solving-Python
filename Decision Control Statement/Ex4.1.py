# Program to increment a number if it is positive 

x = 10
if(x>0):
    x = x+1
print(x)      

# Write a program to determine whether a person is eligible to vote 

age = int(input("Enter the age :"))
if(age>=18):
    print("You are eligivle to vote")
else:
    print("You are not eligible to vote")    

# Write a program to determine the character entered by the user.

char = input("Press any key : ")
if(char.isalpha()):
    print("The user has entered a character")
if(char.isdigit()):
    print("The user has entered a digit")
if(char.isspace()):
    print("The user entered a white space character")       

#  Write a program to determine whether a person is eligible to vote or not. if he is not eligible, display how many years are left to be eligible.

age = int(input("Enter the age : "))
if(age>=18):
    print("You are eligible to vote")
else:
    yrs = 18 - age
    print("You have to wait for another" + str(yrs) +" years to cast your vote")

# Write a program to find larger of two numbers.

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
if(a>b):
    large = a
else:
    large = b
print("Large = ", large)  

# Write a program to find whether the given number is even or odd.

num = int(input("Enter any number : "))
if(num%2==0):
    print(num,"is even")
else:
    print(num,"is odd")    

#--->>> Write a program to enter any character. if the entered character is in lowercase then 
# convert it into uppercase and if it is an uppercase character, then convert it into lowercase <<<---

ch = input("Enter any character : ")
if(ch >= 'A' and ch <='Z'):
    ch = ch.lower()
    print("The entered character was in uppercase. In lowercase it is : " + ch)
else:
    ch = ch.upper()
    print("The entered character was in lowercase. In uppercase it is : " + ch)    


# --->>> A company decides to give bonus to all its employes on Diwali. A5% bonus on salary 
# is given to the male workers. Write a Program to enter the salary of the employee and sex 
# of the employee. if the salary of the employee is less than ₹ 10,000 then the employee 
# gets an extra 2% bonus on salary. Calculate the bonus that has to be given to the employee 
# and dispay the salary that the employee will get. <<<--- 

ch = input("Enter the sex of the employee (m or f) : ")
sal = int(input("Enter the salary of the employee : "))
bonus = 0
if (ch=='m'):
    bonus += ((5/100)*sal)
    if (sal<10000):
        bonus += ((2/100)*sal)
else:
    if (sal<10000):
        bonus += ((2/100)*sal)
print('\n','*'*20)
print('Bonus: ',bonus)
print('Total Amount is',sal+bonus)
print('*'*20)

# Write a program to find whether a given year is a leap year or not.

year = int(input("Enter any year : "))
if((year%4==0 and year %100!=0) or (year%400 == 0)):
    print("Leap Year")
else:
    print("Not a Leap Year")    
