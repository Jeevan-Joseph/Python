list = [1,2,3,3,5,10,20,10,22,8,18]

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]+list[j]==20:
            print("The numbers:",i,"and",j)
            exit()
print("Not found")
