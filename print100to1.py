
def iterate(num):
    if num==1:
        return 1
    print(num)
    return iterate(num-1)


print(iterate(100))