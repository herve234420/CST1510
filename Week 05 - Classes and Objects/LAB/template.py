"""
RECORD CHECK  -  my version
===========================

Name  :  Ndizeye Sangwa Herve
Lane  :  Cyber 
Date  :  23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

class Record:
    """Store a record label, value, and limit."""

    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Store the record details and track over-limit totals."""
        self.label = label
        self.value = value
        self.limit = limit

        if self.value > self.limit:
            Record.over_limit_count += 1

    def status(self):
        """Return the record status based on its value and limit."""
        if self.value >= self.limit:
            return "OVER LIMIT"
        if self.value >= self.limit * 0.9:
            return "WARNING"
        return "OK"


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.


def load_records(path):
    """Read a data file and return a list of Record objects."""
    records = []
    try:
        with open(path) as data_file:
            for line in data_file:
                line = line.strip()
        
                if not line:
                    continue

            label, value, limit = [item.strip() for item in line.split(",")]
            records.append(Record(label, int(value), int(limit)))

    except FileNotFoundError:   
        print(f"File not found:{path}")
    
    return records


records = load_records("RE.txt")


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

over_limit_total = 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"Label : {record.label}")
    print(f"Value : {record.value}")
    print(f"Limit : {record.limit}")
    print(f"Status: {record.status()}")
    print(f"Percent: {round((record.value / record.limit) * 100, 1)}%")

    if record.status() == "OVER LIMIT":
        over_limit_total += 1

    print("=" * 34)

print()
print("=" * 34)
print(f"OVER LIMIT RECORDS: {over_limit_total}")
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
""