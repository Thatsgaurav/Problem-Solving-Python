# Write a program to print the following pattern.
# Pass 1- 1 2 3 4
# Pass 2- 1 2 3 4
# Pass 3- 1 2 3 4
# Pass 4- 1 2 3 4
# Pass 5- 1 2 3 4

for i in range(1,6):
    print("PASS",i,"-  ",end=' ')
    for j in range(1,6):
        print(j, end=' ')
    print()    

# Write a program to print the following pattern
# **********
# **********
# **********
# **********
# **********

for i in range(5):
    print()
    for j in range(5): 
        print("*",end='')

# Write a program to print the following pattern
# *
# **
# ***
# ****
# *****

for i in range(1,6):
    print()
    for j in range(i):
        print("*", end=' ')