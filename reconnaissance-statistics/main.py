import os
import csv

# set read file path
base = os.path.dirname(os.path.abspath(__file__))
name = os.path.normpath(os.path.join(base, './csv/section-eighth.csv'))
file_name = name

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
