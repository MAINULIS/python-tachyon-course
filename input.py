# We used input() function to take a value or input from the user
# Input() always returns a string

# Check If Value Is Int or Float in Python
a = 12
c = "rana"
b = 34.4
print(type(a))
print(isinstance(a, int)) # true
print(type(b))
print(type(c))

# take input form user
x = input("enter a number! \n")
print(x)
print(type(x)) # Input() always returns a string
name = input("inter Your Name: \n")
print("Have a nice day",name)
print(f'Have a nice day {name}')


