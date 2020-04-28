"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

Call_duration = {}

for i in range(len(calls)):
    for j in range(len(calls[0]) - 2):
        if not (calls[i][j] in Call_duration.keys()) :
            Call_duration[calls[i][j]] = 0
        else:
            Call_duration[calls[i][j]] += int(calls[i][-1])

max_duration = max(Call_duration.values())

Longest_call_num = [key for (key, value) in Call_duration.items() if value == max_duration]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(Longest_call_num, Call_duration[Longest_call_num[0]]))
