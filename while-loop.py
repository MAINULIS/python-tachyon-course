i = 1
while i < 11:
    print(i)
    i = i+2

num = int(input("Enter a Number.. \n"))

i = 1
print(f"Multiplication Table for {num}:")
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# find out Quotient and modulus
i = 1
while i <= 100:
    print(f"{i} / 2 = { i / 2}")
    print(f"{i} % 2 = {i % 2}")
    i += 1
