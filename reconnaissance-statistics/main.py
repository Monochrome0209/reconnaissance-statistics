import os
import csv

# set read file path
base = os.path.dirname(os.path.abspath(__file__))
name = os.path.normpath(os.path.join(base, './csv/section-eighth.csv'))
file_name = name

# with open(name, encoding='utf8') as f:
#     print(f.read())
    # csvreader = csv.reader(f)
    # for row in csvreader:
    #     print(row)

max_counts = {"α":0, "β":0, "γ":0}
min_counts = {"α":0, "β":0, "γ":0}

# def count_min_max(file_name):
with open(file_name, 'r') as csvFile:
    reader = csv.reader(csvFile)
    header = next(reader)

    for row in reader:
        row_float = [float(x.strip('%')) for x in row[1:]]
        if not row_float:
            continue
        max_value = max(row[1:])
        min_value = min(row[1:])
        max_column = header[row.index(str(max_value))]
        min_column = header[row.index(str(min_value))]
        max_counts[max_column] += 1
        min_counts[min_column] += 1

print("Max count:")
print(max_counts)
print("Mix count:")
print(min_counts)


        # min_count = 0
        # max_count = 0
        # for row in reader:
        #     # skip first column (date column)
        #     values = [float(val.strip('%')) for val in row[1:]]
        #     min_val = min(values)
        #     max_val = max(values)
        #     min_count += values.count(min_val)
        #     max_count += values.count(max_val)
        # return (min_count, max_count)
    
# min_count, max_count = count_min_max(file_name)
# print("Minimum value count:", min_count)
# print("Maximum value count:", max_count)