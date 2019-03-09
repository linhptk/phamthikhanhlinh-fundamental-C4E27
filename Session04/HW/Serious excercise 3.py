print("Answer the following algebra question:\n")
print("If x =8, then what is the value of 4(x+3)?\n")
# print("1. 35\n")
# print("2. 36\n")
# print("3. 40\n")
# print("4. 44\n")
A = {'1':'35', '2': '36', '3':'40', '4':'44'}
for k,v in A.items():
    print(k,v, sep='.')
Q = int(input("Your choice: "))
if Q ==4:
    print("Bingo")
else:
    print(":(")