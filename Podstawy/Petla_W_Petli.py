from time import sleep

# *
# **
# ***
# ****


for i in range(0, 4):
    for j in range(0, i+1):
        print("*", end="")
    print("\r")

print("\r")

#     *
#    **
#   ***
#  ****
# *****

n = 5
for i in range(n):
    for j in range(n-(i+1)):
        print(end=" ")
    for j in range(i+1):
        print("*", end="")
    print("\r")

print('\r')

#     **
#    ****
#   ******
#  ********
# **********


for i in range(n):
    for j in range(n-(i+1)):
        print(end=" ")
    for j in range(i+1):
        print("*****", end="")
    print('\r')