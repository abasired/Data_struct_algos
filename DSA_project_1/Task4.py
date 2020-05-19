"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""



outgoing_num = set()
non_tele_num = set()

for call_index in calls:
    
    outgoing_num.add(call_index[0])
    non_tele_num.add(call_index[1])
    
for text_index in texts:
    
    non_tele_num.add(text_index[0])
    non_tele_num.add(text_index[1])
    
tele_set = outgoing_num - non_tele_num
        
print("These numbers could be telemarketers: ")

print("\n".join(sorted(tele_set)))

