"""
RECORD CHECK  -  my version
===========================

Name  :  NDIZEYE SANGWA HERVE
Lane  :  Cyber
Date  :  07/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.
def parse_line(raw_line):
    """Cleans and parses one cyber security record into a dictionary."""

    clean_line = raw_line.strip()
    parts = clean_line.split(",")

    record = {}

    for part in parts:
        key, value = part.split("=", 1)

        key = key.strip().lower()
        value = value.strip()

        if key == "attempts":
            record[key] = int(value)
        else:
            record[key] = value.upper() if key == "result" else value

    return record

def status_of(record):
    """Checks whether a security record is flagged."""

    if record["result"] == "FAILED":
        return "FLAGGED"
    else:
        return "OK"

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.
raw_records = []

with open(r"C:\Users\ISHIMWE BRIAN\OneDrive\Documents\MDX ASSIGNEMENTS\CST1510\Week 07 - Strings and Text Manipulation\LAB\messy_lines.txt", "r") as file:
    for line in file:
        raw_records.append(line)


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

flagged_count = 0
for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)

    print(record, status)

    if status == "FLAGGED":
        flagged_count += 1

print("Total records:", len(raw_records))
print("Flagged records:", flagged_count)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
try:
    test_record = parse_line("SRC=10.0.0.9,ATTEMPTS=unknown,RESULT=FAILED")
except ValueError as error:
    print("Error:", error)