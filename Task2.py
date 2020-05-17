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

for call_index in calls:
    
    if call_index[0] in Call_duration:
        Call_duration[call_index[0]] += int(call_index[3])
    else:
        Call_duration[call_index[0]] = int(call_index[3])
        
    if call_index[1] in Call_duration:
        Call_duration[call_index[1]] += int(call_index[3])
    else:
        Call_duration[call_index[1]] = int(call_index[3])


max_duration = max(Call_duration.values())

Longest_call_num = max(Call_duration, key = Call_duration.get)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(Longest_call_num, max_duration))
