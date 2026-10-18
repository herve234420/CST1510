"""
RECORD CHECK  -  my version
===========================

Name  : Ndizeye Sangwa Herve
Lane  :  Cyber      (delete two)
Date  :  17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here

def check_record(value, limit):
    """Calculate the difference, percentage and status for a record."""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report for one record."""
    print("=" * 35)
    print(f"RECORD CHECK - {label}")
    print("-" * 35)
    print(f"{'Value:':<15}{value:>10.2f}")
    print(f"{'Limit:':<15}{limit:>10.2f}")
    print(f"{'Difference:':<15}{difference:>10.2f}")
    print(f"{'Percent:':<15}{percent:>9.2f}%")
    print(f"{'Status:':<15}{status:>10}")
    print("=" * 35)


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.
def load_records(path):
    """Load records from a file and return them as dictionaries."""
    records = []

    try:
        with open(path, "r") as f:
            for line in f:
                line = line.strip()

                if line:
                    label, value, limit = line.split(",")
                    records.append({
                        "label": label,
                        "value": float(value),
                        "limit": float(limit)
                    })

    except FileNotFoundError:
        print(f"File not found: {path}")

    return records


records = load_records("records_sample.txt")




# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
over_limit_count = 0

with open("results.txt", "w") as f:
    for record in records:
        difference, percent, status = check_record(
            record["value"], record["limit"]
        )

        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status
        )

        f.write(f'{record["label"]},{status}\n')

        if status == "OVER LIMIT":
            over_limit_count += 1

print(f"Total OVER LIMIT records: {over_limit_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
