    # BT:
# Nhap n so tu ban phim va in ra tong n so bat ky vua nhap
# n = int(input("Nhap so ban muon tinh tong:\n"))
# tong = 0
# for i in range(n):
#     so = int(input("nhap so"))
#     tong = tong + so
# print(tong)

    # Session02
# Cau lenh if
# age = 8
# if age<10:
#     print("baby")
# % la phep chia lay phan du

# n = int(input("Enter a number:\n"))
# if n%2==0:
#     print("Even number")

# if <dieu kien 1>
    # <khoi lenh 1>

#if <dieu kien 1>
    # <Khoi lenh 1>
# else:
#   <khoi lenh 2> 

# if <dk 1> --> Neu dung thi lam va thoat khoi cau lenh, khong kiem tra dieu kien ben duoi nua
    # <khoi lenh>
# elif <dk 2>
# ....
# else
    #<khoi lenh n>

    # BT    
#  nhap nam sinh cua 1 nguoi va in ra man hinh nhu sau
# Neu nguoi do <10 tuoi thi in ra: "Baby"
# Neu nguoi do <16 tuoi va >=10 thi in ra: "Teen"
# Con lai thi in ra "Adult"

# x = int(input("Nhap nam sinh:\n"))
# Tuoi = 2019 - x
# if Tuoi < 10:
#     print("Baby")
# # elif 10 <= Tuoi < 16:  hoac x < 16
#     print("Teen")
# else:
#     print("Adult")

    # Session03:
# yob = input("Nhap nam sinh:")
# yob.isdigit()
# age = 2019 - int(yob)
# print("Tuoi cua ban la:", age)
# while True:
#     print("hi")
# while False:
#     print("hi")
# while <dieu kien>:   --> Khi nao dieu kien nay con dung thi se mai la khoi lenh nay. Khong co khoi lenh nay khong co cau lenh nao lam cho dieu kien tu dung thanh sai thi se mai lap lai cau lenh nay.
    # <khoi lenh>   
# Khi dung vong while phai nho la khi nao no dung lai 

# yob = input("Nhap nam sinh:")
# while not yob.isdigit():
#     print('ban nhap sai roi, moi nhap lai:')
#     yob = input("Nhap nam sinh:")
# age = 2019 - int(yob)
# print('tuoi cua ban la:', age)

# BT: nhap mat khau nho hon 8 la sai, lon hon 8 la dung
#Cach 1
#  password = input("nhap mat khau:\n")
# while not len(password)<8:
#     print("Vui long nhap lai mat khau")
#     password = input("Vui long nhap lai mat khau")  --> Nhap sai cho nhap lai

# Cach 2
# password = input("nhap mat khau:\n")
# while True:
#     if len(password)>8:
#         break
#     print("Moi ban nhap lai pass:")
#     password = input("Moi ban nhap password")

# Lenh break de thoat khoi vong lap for hoac while
# khac nhau giua for va while:
# so lan lap biet trc thi dung for
# so lan lap chua biet truoc va phai co dieu kien thi dung while

# for i in range(3):
#     print(i) 
# --> lam the nao de in ra i ma dung vong while

# loop_count = 0
# while loop_count<3:
#     print('loop count:', loop_count)
#     # loop_count-=1
#     loop_count = loop_count + 1

# loop_count = 0
# while True:
#     print('loop count:', loop_count)
#     # loop_count-=1
#     loop_count = loop_count + 1
#     if loop_count>=3:
#         break
# print ("abc")

# += --> x=x+1 <=> x+=1
# *= --> x=x*3 <=> x*=3

# BT: Nhap 3 so a,b,c
# Giai phuong trinh ax^2 + bx +c = 0
# Can bac hai: a**0.5 hoac import math va math.sqrt(a)

# a = float(input("Nhap so a:\n"))
# b = float(input("Nhap so b:\n"))
# c = float(input("Nhap so c:\n"))
# delta = b**2 - 4*a*c
# if delta < 0:
#     print("Phuong trinh vo nghiem")
# if delta == 0:
#     x = -b/2*a
#     print("Phuong trinh co nghiem duy nhat")
# if delta > 0:
#     x1 = (-b + (delta**0.5)/(2*a))
#     x2 = (-b - (delta**0.5)/(2*a))
#     print("Phuong trinh co 2 nghiem phan biet")
#     print("x1=", x1)
#     print("x2=", x2)

# BT:
# Cho day n so nguyen 
# + Tinh tong day vua nhap
# + Tinh tong cac so le
# + Tinh tong cac so cham
# + Tinh trung binh cong cac so chan
# List: a = [1,2,3,4]

# list = [1,2,3,4,5,6,7]
# sum list
# list.append(8)
# a.remove
# BT:
# cho day m so nguyen. In ra tong day so vua nhap
ls=[]
n = int(input("Moi ban nhap so phan tu:"))
for i in range(n):
    print("Nhap phan tu thu:",i)
    so=int(input(""))
    ls.append(so)
print("day ban vua nhap la:")
print(ls)

print("Tong day vua nhap:")
print(sum(ls))

print("Phan tu thu 2 trong day")
print(ls[1])

# a = [1,2,3,4]
# x = a[2] --> x =3
# x = a[0] --> x=1
# x = a[len(a)-1] --> 4-1 --> a=3