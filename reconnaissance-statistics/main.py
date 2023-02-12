import os
import csv

# set read file path
base = os.path.dirname(os.path.abspath(__file__))
name = os.path.normpath(os.path.join(base, './csv/section-eighth.csv'))

# with open(name, encoding='utf8') as f:
#     print(f.read())
    # csvreader = csv.reader(f)
    # for row in csvreader:
    #     print(row)

def count_min_max(file_name):
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile)
        # skip header row
        next(reader)

        min_count = 0
        max_count = 0
        for row in reader:
            # skip first column (date column)
            values = [float(val.strip('%')) for val in row[1:]]
            min_val = min(values)
            max_val = max(values)
            min_count += values.count(min_val)
            max_count += values.count(max_val)
        return (min_count, max_count)
    
file_name = name
min_count, max_count = count_min_max(file_name)
print("Minimum value count:", min_count)
print("Maximum value count:", max_count)