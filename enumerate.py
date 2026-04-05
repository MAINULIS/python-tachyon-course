# enumerate --> গণনা করা, calculate
## The enumerate() function in Python is a built-in tool that adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate object

## using enumerate() function we can get index and value at the same time
students = ["Rana", "Shakib", "Shamim"]
for index, student in enumerate(students):
    print(f"{index+1}. Welcome,{student}!")