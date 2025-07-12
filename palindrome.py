str = "Amma".lower()
ans = " "

for i in str:
    if i.isalpha():
        ans = ans + i
rev=" " 
for i in ans:
        rev = i + rev
if rev == ans : print("is palindrome")
else : print("not palindrome")