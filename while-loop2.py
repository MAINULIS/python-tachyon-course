#  determine sum of numbers 1-100
i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i += 1
print(sum)

## Factorial
num = int(input("Enter a Number.. \n"))
result = 1
while num > 1:
    result = result * num
    num -= 1
print(result)


## Fibonacci series --> 0 1 1 2 3 5 8 13 15 ...
n = int(input("Enter a number: "))
a = 0
b = 1

while(b <= n):
 print(b, end = " ")
 a, b = b, a + b

# ## Prime number
num = int(input("Enter a number: "))

if num > 1:
    i = 2
    is_prime = True
    while i < num:
        if num % i == 0:
            is_prime = False
            print(i)
        i = i + 1
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
else:
    print(" Enter a valid number!")