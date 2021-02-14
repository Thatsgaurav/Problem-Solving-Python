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

# Write a program to print the following pattern
# 1
# 1 2
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(j, end=' ')

# Write a program to print the following pattern
# 1
# 22
# 333
# 444
# 55555

for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(i, end=' ')

# Write a program to print the following pattern
# 0
# 12
# 345
# 6789 

count = 0
for i in range(1,5):
    print()
    for j in range(1,i+1):
        print(count, end=' ')
    count = count+1

# Write a program to print the following pattern
#     1
#    12
#   123
#  1234
# 12345  

N = 5
for i in range(1,N+1):
    for k in range(N,i,-1):
        print(" ", end=' ')
    for j in range(1,i+1):
        print(j, end=' ')
    print()        