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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

Total_unique_num = set()

"""
Read the total number of records from texts and call into a set data structure
Print the length of the set in the desired format.
"""

for text_index in texts:
    for num_info in range(len(texts[0]) - 1):  # Account for incoming and answering number in each texts record 
        Total_unique_num.add(text_index[num_info])

        
for call_index in calls:
    for num_info in range(len(calls[0]) - 2):  # Account for incoming and answering number in each calls record
        Total_unique_num.add(call_index[num_info])


print("There are {} different telephone numbers in the records.".format(len(Total_unique_num)))

        
