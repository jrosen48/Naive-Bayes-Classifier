import pandas as pd
import re

data = pd.read_csv("./scip_data.csv") # make path relative so we can use it
# ^^^ pandas is annoying AF

#for string in data.purpose:
#    print string

# use data["purpose"], data["criteria"], data["generality"], data["audience1"], data["audience2"], and data["evidence"]

def process_strings(data):
    global entry
    outlist = []
    for entry in data:
        entry = str(entry).lower() # makes text lowercase
        entry = re.sub('[0-9]+','', entry) # removes numbers
        entry = entry.strip() # strips whitespace
        outlist.append(entry)
    return outlist
    
processed_data = process_strings(data.purpose.values) # using lists instead of pandas HOLLA

print 'example from processed_data',processed_data[0]

