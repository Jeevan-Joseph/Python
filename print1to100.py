
def iterate(num):
    if num==100:
        return 100
    print(num)
    return iterate(num+1)


print(iterate(1))