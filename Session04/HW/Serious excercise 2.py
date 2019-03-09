prices ={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock ={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
# loop in dict
for i in prices:
    print(i)
    print("price:", prices[i])
    print("stock:", stock[i])
# Total money
    total = 0
    money = int(prices[i]*stock[i])
    total = total + money
    print("Total money:", total)