customers=[]

while True:
    a=input("Is there any customer available y/n: ")
    if a=='n':
        break

    name = input("Enter customer name:")
    items=[]
    
    print("Enter items one by one (type 'stop' to finish):")
    while True:
        item = input("Item: ")
        if item == "stop":
            break
        if item:
            items.append(item)
    
    customers.append({"name": name,"items": items})

print("\n customer Purchase List:")
i=0
while i<len(customers):
    customer = customers[i]
    name = customer["name"]
    items = customer["items"]

    item_str = ",".join(items)

    print("Customer:",name,", Items:",item_str)
    i+=1      