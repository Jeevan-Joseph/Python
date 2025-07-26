
def longestCommonPrefix(list1):
    list1.sort()
    x = list1[0]
    y = list1[-1]
    ans = ""
    for i in range(min(len(x),len(y))):
        if x[i] != y[i]:
            return ans
        ans += x[i]
        
    
a =["flight","flower","flag"]

print(longestCommonPrefix(a))