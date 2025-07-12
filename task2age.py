year=int(input("Enter ur birth year:"))
age=2025-year
print(age)

if age<13:
    print("child")
    print("Not eligible for vote")
elif age<20:
    print("Teeneage")
    if(age>17):
        print("Eligible for vote")
elif age<60:
    print("Adult")
    print("Eligible for vote")
else:
    print("Senior citizen")
    print("Eligible for vote")