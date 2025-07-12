list1 = [2,4,5,6]
list2 = [5,5,3,2,6]

lists = list1 + list2
join = []

for i in lists:
    if i not in join:
        join.append(i)

print(set(join))