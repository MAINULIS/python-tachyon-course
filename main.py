print("Hellow, world")

# Types of data in python
'''
# Numbers:
integer --> 3,29
Floating --> 32.7, 2.0
complex
# String
# Sequence data types:
list --> [3, 4, Jan, Feb]
tuple --> (3, 30, "python")
range --> (1, 5, 2)    --> explanation: 1 is start, 5 is stop and 2 is step
'''

'''
+= --> means add the value with the existing variable
-= --> means minus the value from the existing variable
*= -->means multiply the value with the existing variable
/= -->means divide the value with the existing variable
'''
# example
x = 20
x += 4
print(x)

x -= 3
print(x)

b= 7
b *= 10
print(b)

z = 60
z /= 10
print(z)

# Check If Value Is Int or Float in Python
a = 12
b = 34.4
c = "rana"
print(type(a))
print(type(b))
print(isinstance(b, float)) # true
print(type(c))