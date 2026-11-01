"""
RECORD CHECK  -  my version
===========================

Name  : Ndizeye Sangwa Herve
Lane  :  Cyber     (delete two)
Date  : 10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here
def status_of(percent):
    """Return the status based on the percentage"""
    if percent >=100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Return the difference and percentage."""
    difference= value - limit
    percent = (value / limit) * 100
    return difference, percent


# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())




# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.

# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

def print_report(label, value, limit, difference, percent, status):
    """Print the complete report for a record"""
    print()
    print("=" *34)
    print(f" RECORD CHECK - {label}")
    print("=" *34)
    print(f"Value      :{value:>10.2f}")
    print(f"Limit      :{limit:>10.2f}")
    print(f"Difference :{difference:>10.2f}")
    print(f"Percent    :{percent:>9.2f}%")
    print(f"Status     :{status:>10.2}")
    print("=" *34)

#INPUT, PROCESS AND OUTPUT
over_limit_count =0
while True:
    label = str(input("Enter a label : ")) # asking the user to enter a dataset 
    if label == "quit": #check if the user wants to quit the loop
        break
    value = float(str(input("Enter the new row loaded: "))) #asking user to enter the row loads 
    limit = float(str(input("Enter the row expected: "))) #asking user to enter the row expected

    difference, percent = check(value, limit) # calling the check function to calculate difference
    status = status_of(percent)
    if status == "OVER LIMIT": # increment the counter for records that are over the limit
        over_limit_count +=1

    print_report(label, value, limit, difference, percent, status)

print(f"Record over limit: {over_limit_count}")
# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
