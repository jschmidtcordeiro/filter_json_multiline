import sys
from src.parse import Parse
import json
import pandas as pd

input_path = sys.argv[1]
output_path = sys.argv[2]

# Open the input file passed as a command line argument
with open(input_path) as f:
    lines = f.readlines()

# Parse lines of input
for i_line in range(len(lines)):
    p = Parse(lines[i_line])
    p.str_to_list()
    p.list_to_dict()
    lines[i_line] = p.get_parsed_dict()


# Send to CSV
df = pd.DataFrame.from_records(lines)
df.to_csv(output_path, index=False)
