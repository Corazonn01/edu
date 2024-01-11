new_file = []
with open("numbers.txt", "r") as file:
    for i in file:
        splitting = [int(k) for k in i.split()]
        new_file.extend(splitting)

test_list = sorted(set(new_file))

print(new_file)
print(test_list)

with open("result.txt", "a") as f:
    f.write(str(test_list))

