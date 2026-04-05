# if , elif and else condition
mark = int(input("Enter your Marks:"))

if mark >= 80:
    print("A+")
elif mark >= 70 and mark < 80:
    print("A")
elif mark >= 60 and mark < 70:
    print("b")
elif mark >= 50 and mark < 60:
    print("c")
elif mark >= 40 and mark < 50:
    print("d")
elif mark >= 33 and mark < 40:
    print("e")
elif mark <= 33:
    print("Fail")
else:
    print("Invalid Number")