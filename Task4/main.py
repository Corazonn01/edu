import csv
new_dict = {}
with open('data/data.csv', 'r') as file:
    read_file = csv.DictReader(file)

    for row in read_file:
        key = row['type'].strip().lower()
        value = int(row['count'])
        new_dict[key] = value
print(new_dict)
max_key = max(new_dict, key=lambda k: new_dict[k])
min_key = min(new_dict, key=lambda k: new_dict[k])
print(max_key, new_dict[max_key],'\n', min_key, new_dict[min_key])

print("here is the current dictionary", new_dict)
user_input = input('Please write the animal or thing and it will be added to the dictionary.')
if user_input in new_dict:
    new_dict[user_input] += 1
else:
    new_dict[user_input] = 1

print("Updated dictionary:", new_dict)

with open('final.txt', 'a') as file:
    file.write(f"new_dict = {str(new_dict)}\n")


