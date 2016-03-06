import nltk
import pandas as pd
import re

data = pd.read_csv("/Users/joshuarosenberg/Dropbox/research/cluster-compare-text/csv/scip_data.csv")

# use data["purpose"], data["criteria"], data["generality"], data["audience1"], data["audience2"], and data["evidence"]

def process_strings(data):
    data = data.str.lower()
    return data

processed_data = process_strings(data.purpose)
