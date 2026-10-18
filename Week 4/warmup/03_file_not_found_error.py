# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("missing.txt not found")
