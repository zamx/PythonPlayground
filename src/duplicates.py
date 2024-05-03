#Not allowed to use set
some_list = ['a', 'b', 'c', 'd', 'm', 'n', 'n', 'b', 'b']

duplicates = []

some_list.sort()

for item in some_list:
    if some_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print(duplicates)
