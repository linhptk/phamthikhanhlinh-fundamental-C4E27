#           1. what is Boolean?
# --> Boolean values are the two constant objects False and True
# e.g 1:
Password = input("What is your password? \n")
Password = int(Password)
if Password == 12345:
    print("True!")
else:
    print("False!")

# e.g 2:
x = input("Am I teenager? \n")
x = int(x)
if x <= 18:
    print("True!\n")
else:
    print("False!")

# e.g 3:
x = input("Is the answer correct? \n")
x = float(x)
if x <= 10:
    print("False!")
else:
    print("True!")

#           2.What is flowchart?
# --> flowchart la so do bieu dien thuat toan. Flowchart rat can thiet khi viet chuong trinh hoac giai thich cho nguoi khac
 
#           3.What is nested conditionals?
# --> Nested conditional: cac dieu kien lien quan den nhau,  dieu kien nay co the thuoc dieu kien khac
#           Write a piece of code that uses nested conditionals
x = input("Enter your age:\n")
x = int(x)
if x < 18:
    print("You are teenager!\n")
else:
    if 18 < x < 50:
        print("You are adult!")
    else:
        print("You are the elder!")

