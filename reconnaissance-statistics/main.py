import os
import csv

base = os.path.dirname(os.path.abspath(__file__))
name = os.path.normpath(os.path.join(base, './csv/section-eighth.csv'))

with open(name, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row)