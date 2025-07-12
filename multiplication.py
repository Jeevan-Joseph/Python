a=int(input("Enter a Number:"))
b=1
while a>0:
    c=a*b
    print(a,"*",+b,"=",+c)
    b=b+1
    if b==11:
        break

#for loop

x=int(input("Enter a Number"))
for i in range(1,21):
    y=x*i
    print(x,"*",+i,"=",+y)