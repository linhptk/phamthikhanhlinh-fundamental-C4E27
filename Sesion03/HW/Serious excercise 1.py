
items = ["T-shirt","Sweater"]
user = input("Wellcome to our shop, what do you want (C,R,U,D)?\n")
if user =="R":
    print(items)
elif user =="C":
    Newitem1=input("Input new item:\n")
    items.append(Newitem1)
    print(items)
elif user =="U":
    Newposition = int(input("Upadate position?\n"))
    if Newposition <= len(items):
        # items.pop(Newposition - 1) 
        Newitem2 = input("New item:\n")
        items.insert((Newposition - 1), Newitem2)
    else:  
        print("Error.")
    print(items)
elif user =="D":
    Newposition2 = int(input("The position you want to delete:\n"))
    if Newposition2 <= len(items):
        items.pop(Newposition2 - 1)
        print(items)
    else:
        print("Error.")    
   
