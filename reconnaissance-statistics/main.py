import json

json_open = open('result/test.json', 'r')
json_load = json.load(json_open)

print(json_load)
