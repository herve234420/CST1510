"""
RECORD CHECK  -  my version
===========================

Name  : Ndizeye Sangwa Herve
Lane  :  Cyber    (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

OVERLIMITCOUNT = 0

while True:
    label = str(input("Enter a Source IP(or quit): "))
    if label == "quit":
        break
    value = float(input("Enter failed logins: ")) 
    limit = float(input("Enter total attempts: "))    


    difference = limit - value
    percent = (difference / limit) * 100 if limit != 0 else 0

    status = ""   # replace with your if / else (or if / elif / else)
    if percent >= 100:
        status = "OVER LIMIT"
        OVERLIMITCOUNT += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"




    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)


    print("=" * 34)

    print(f"value       : {value:>10.2f}")
    print(f"limit       : {limit:>10.2f}")
    print(f"difference  : {difference:>+10.2f}")
    print(f"percent     : {percent:>10.2f}%")
    print(f"status      : {status:>10}")

print()
print(f"OVER LIMIT COUNT: {OVERLIMITCOUNT}")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
