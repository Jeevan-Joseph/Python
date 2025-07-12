a=[20,30,50,23,34]
n=len(a)
temp=0

for i in range(n):
    for j in range(i+1,n):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(a)