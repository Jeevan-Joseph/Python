a = [2,3,4,4,6,8,3,18,2,54,54]
seta=set(a)
list1=list(seta)
n=len(list1)
temp=0

for i in range(n):
    for j in range(i+1,n):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
print(list1)
print("The first largest: ",list1[-1])
print("The second largest: ",list1[-2])

