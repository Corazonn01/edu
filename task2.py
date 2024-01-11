new_file = []
with open('one.txt', 'r') as file1, open('two.txt', 'r') as file2, open('three.txt', 'r') as file3:
    for line1, line2, line3 in zip(file1, file2, file3):
        one = line1.strip(), line2.strip(), line3.strip()
        new_file.extend(one)

all_numbers = [int(num) for sublist in new_file for num in sublist.split(', ')]

duplicates = [number for number in all_numbers if all_numbers.count(number) > 1]
unique_duplicates = list(set(duplicates))
print("here you can see the numbers that were repeated: ", unique_duplicates)
print("And the number of duplicate numbers: ", len(unique_duplicates))

delete_el = (sorted(list(set(all_numbers))))
print(delete_el)
with open ('four.txt', 'w') as file4:
    file4.write(str(delete_el) + '\n')





