n = input("Enter a number:\n")
print("------------------------------")
n = int(n)
result = 1
for i in range(1,n+1):
    result = result * i
    print(str(result))
print(str(result))