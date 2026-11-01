# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

limit = 20
value = int(input("Value: "))

if value > limit:
    print("OVER")
else:
    print("OK")
#the code was missing a data type for the input value, which caused a type error when comparing it to the integer limit.