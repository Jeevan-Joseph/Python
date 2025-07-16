def mul(x,num=1):
    if num==11:
        return
    print(num,"*",x,"=",num*x)
    mul(x,num+1)

mul(6)