result = {}
with open('data/data.txt', 'r') as file:
    for i in file:
        for each_line in i:
            if each_line.isdigit():
                if each_line in result:
                    result[each_line] += 1
                else:
                    result[each_line] = 1

if result == {'1': 7, '2': 6, '3': 5, '4': 3, '5': 2}:
    print("Ты молодец")
else:
    print("Ещё нет")




