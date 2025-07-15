
def iterate(num):
    if num==0:
        return 
    print(num)
    return iterate(num-1)

user = int(input("Enter any number:"))
iterate(100)