list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8]

lists = list1 + list2
join = []

for i in lists:
    if i not in join:
        join.append(i)

print(join)


