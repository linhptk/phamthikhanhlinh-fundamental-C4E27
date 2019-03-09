# 2.1
# print("Hello, Hiep and these are my sheep sizes:\n")
# sheep_size = [5,7, 300, 90, 24, 50, 75]
# print(sheep_size)

# 2.2
# max_sheep_size = print(max(sheep_size))
# print("Now my biggest sheep has size:", max(sheep_size), end=' ') 
# print("let's shear it")

# # 2.3
# index_max_size = sheep_size.index(max(sheep_size))
# sheep_size.remove(max(sheep_size))
# new_sheep_size = sheep_size.insert(index_max_size,8)
# print("After shearing, here is my flock:\n", end=' ')
# print(sheep_size)  

# # 2.4
# for i in range(len(sheep_size)):
#     sheep_size[i] = sheep_size[i] + 50
# print("One month has passed, now here is my flock:\n",sheep_size)   

#2.5
# Month 1
# sheep_size2 = [5,7,300,90,24,50,75]
# print("Hello, my name is Hiep and there is my flock:\n", sheep_size2)
# for i in range(1,4):
#     print("Month", i)
#     for j in range(len(sheep_size2)):
#         sheep_size2[j] = sheep_size2[j] + 50
#     print ("One month has passed, now here is my flock:\n", sheep_size2)
#     print("Now my biggest sheep has size:",max(sheep_size2),"let's shear it")
#     index_sheep_size2 = sheep_size2.index(max(sheep_size2))
#     sheep_size2.remove(max(sheep_size2))
#     new_sheep_size2 = sheep_size2.insert(index_sheep_size2,8)
#     print("After shearing, here is my flock\n", sheep_size2)

# 2.6
sheep_size3 = [5,7,300,90,24,50,75]
print("Hello, my namne is Hiep and there is my flock:\n", sheep_size3)
so_thang = int(input("how many months?"))
for i in range(0,so_thang):
    if i ==0:
        print("Now my biggest sheep size is:", max(sheep_size3), "let's shear it")
        index_new_sheep3 = sheep_size3.index(max(sheep_size3))
        sheep_size3.remove(max(sheep_size3))
        new_sheep_size3 = sheep_size3.insert(index_new_sheep3,8)
        print("After shearing,here is my flock\n", sheep_size3)
   
    elif i ==(so_thang -1):
        print("Month", (so_thang -1))
        for j in range(len(sheep_size3)):
            sheep_size3[j] = sheep_size3[j] + 50
        print ("One month has passed, now here is my flock:\n", sheep_size3)
        print("My flock has size in total:\n", sum(sheep_size3))
        price = sum(sheep_size3) * 2
        print("I would get", sum(sheep_size3), "*2$ =  ", price, "$")
   
    else:
        print("Month", i)
        for j in range(len(sheep_size3)):
            sheep_size3[j] = sheep_size3[j] + 50
        print ("One month has passed, now here is my flock:\n", sheep_size3)
        print("Now my biggest sheep has size:",max(sheep_size3),"let's shear it")
        index_sheep_size3 = sheep_size3.index(max(sheep_size3))
        sheep_size3.remove(max(sheep_size3))
        new_sheep_size3 = sheep_size3.insert(index_sheep_size3,8)
        print("After shearing, here is my flock\n", sheep_size3)
    