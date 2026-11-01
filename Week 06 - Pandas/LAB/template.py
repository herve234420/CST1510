"""
RECORD CHECK  -  my version
===========================

Name  : Ndizeye Sangwa Herve
Lane  :  Cyber
Date  : 30/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt



# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.read_csv("records_sample.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

df["percent"] = (df["value"] / df["limit"]) *100

#give each reccord a status
df["status"] =df ["percent"].apply(
   lambda percent: "OVER LIMIT" if percent >= 100
    else "WARNING" if percent >= 90
    else "OK"
)


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

#print full dataframe
print("\nFULL RECORD REPORT")
print(df)

print("\nRECORDS NEEDING ATTENTION")
print(df[df["status"] != "OK"])

# Count records in each status group
print("\nSTATUS COUNTS")
status_count = df.groupby("status").size()
print(status_count)

# save the new data frame to a new CSV file 
df.to_csv("record_report.csv", index=False)

# Create and save a bar chart
status_count.plot(kind="bar")
plt.title("Record Status Count")
plt.xlabel("Status")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig("status_show.png")
plt.show()


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
