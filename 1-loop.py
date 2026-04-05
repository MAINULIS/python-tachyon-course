# There is two loops in python. that are for loop and while loop
## range --> (1, 5, 2)    --> explanation: 1 is start, 5 is stop and 2 is step
for i in range(11): # output will be 11 numbers. started with 0.
    print(i)

for x in range(1, 101, 1): # printed 1 to 100 numbers
    print(x)

# print -10 to 20
for i in range(-10, 21, 1):
    print(i)

# ৫ এর নামতা
for i in range(5, 51, 5):
    print(i)

# take a number as an input and print the namta of that number
num = int(input("enter a number! \n")) # Input() always returns a string
# for i in range(num, num*10+1, num):
#     print(i)

for i in range(1, 11):
 # print(num, 'x', i, '=' , num*i)
 print(f"{num} x {i} = {num * i}")
