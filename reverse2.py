u = "Hello World"
ans = " "
arr = u.split()

for i in arr:
    rev=" "
    for j in i:
        rev = j + rev
    ans += rev
print(ans)