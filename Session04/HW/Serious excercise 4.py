print("Answer the following algebra question:\n")
print("If x = 8, then what is the value of 4(x +3)?")
Q = {'1':'35','2':'36', '3':'40','4':'44'}
total_answer = {
    'Correct answer':int('0'),'Wrong answer': int('0')
    }
for k,v in Q.items():
    print(k,v, sep='.')
A = int(input("Your choice: "))
if A ==4:
    print("Bingo")
    total_answer['Correct answer'] += 1
else:
    print(":(")
    total_answer['Wrong answer'] += 1
print("Jack scored these marks in 5 math. What is the mean")
Q2 = {'1':'About 55','2':'About 65','3':'About 75', '4':'About 85'}
for k,v in Q2.items():
    print(k,v, sep='.')
A2 = input("Your choice: ")
if A2 ==2:
    print("Bingo")
    total_answer['Correct answer'] += 1
else:
    print(":(")
    total_answer['Wrong answer'] += 1
print(total_answer)
print("You are correctly answer", total_answer['Correct answer'], "out of 2 questions")