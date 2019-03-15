# dict laf cấu trúc dữ liệu trong python
# trong list thì cần đúng kiểu dữ liệu. dùng dict thì nhiều kiểu dữ liệu
# BT
# Viet chuong trinh giai các bài toán sau đây
# a. Nhập 1 dãy n số nguyên và tính tổng dãy số vừa Nhập
# b. Nhập 1 dãy m số nguyên và tính trung bình cộng dãy số vừa nhâp

# ls=[]
# so_nguyen = int(input("Nhập dãy n số nguyên:\n"))
# for i in range(so_nguyen):
#     print("Nhập phần tử  thứ:",i)
#     so = int(input(""))
#     ls.append(so)

    # function (Hàm): co the dùng lại (reduce)
    # - Hàm là 1 đoạn code thực hiện 1 tác vụ và đc gọi nhiều lần từ nhiều nơi
# def function_name([parameter]):
    # function_name: ten ham, nen dat de hieu
    # parameter: tham so cua ham, co hay khong co deu dc
    # Function khong tham so - khong return
# def say_hi():        ---> Khai bao ham
#     print("hi")       ---> Khai bao ham

# say_hi() ----> goi ten ham
# def say_hi():
#     print("hi")
#     print("bye")
# say_hi()

# def add_two_number():
#     a=int(input("nhap so thu nhat:"))
#     b=int(input("nhap so thu hai:"))
#     print("tong hai so la", a+b)
# add_two_number()
# --> Ham chay dc nhung khong mang lai muc dich gi, khong reuse dc

# def add_two_number(a,b):
#     print("tong hai so la:", a + b)
# num1 = int(input("nhap so thu nhat:"))
# num2 = int(input("nhap so thu hai:"))
# add_two_number(500, 1000*100)
# add_two_number(num1, num2)
# --> Nhập từ ngoài hàm (VD trên nhập từ trong hàm)
# --> Tham số (a,b): tham số là cách để hàm có thể nhận nhiều giá trị khác nhau để nó xử lý
# Function có tham số - có return
# def add_two_number(a,b):
#     return a + b
# num1 = int(input("nhap so thu nhat:"))
# num2 = int(input("nhap so thu hai:"))
# num3 = int(input("nhap so thu ba:"))
# sum_1_2 = add_two_number(num1,num2)
# sum_3 = add_two_number(sum_1_2, num3)
# print("Tong 3 so la:", sum_3)

#- Lệnh return phải nằm trong body của hàm
# - Lệnh return sẽ trả về kết quả cho lời gọi hàm: ví dụ: add_two_number(1,2)
#VD: print(add_two_number(add_two_number(1,2),3))
# def add_two_number(a,b):
#     print(a + b)
# x = 121+add_two_number(3,4)
# print(x)

# def abs_of_number(a):
#     if a > 0:
#         return a
#         print('tri tuyet doi la:', a)
#     else:
#         return -a
#         print('trị tuyet doi la:', -a)
#     print('tri tuyet doi la:', a)
# x = abs_of_number(-12)
# tong = 12 + abs_of_number(-12)
# print("x =", x)
# print("Tổng =", tong)

# return gần giống break: khi gặp return rồi thì sẽ thoát khỏi hàm
# BT:
# Viết hàm tên là evaluate, nhận vào 2 số và 1 phép tính. 
# Tính toán phép tính này với hai số đầu vào và trả về giá trị tính được
# VD:
# x = evaluate(1,3,'+')
# x sẽ có giá trị là 4

# Hướng giải
# evaluate()
# Đầu vào: 3 biến a,b,operator
# a,b là số
# operator là dấu +, *, -,... dùng lệnh if else để tìm

# def evaluate(a,b,operator):
#     if operator =="*":
#         return a*b
#     if operator =="+":
#         return a+b
#     if operator =="-":
#         return a-b
#     if operator =="/"
#         return a/b
# a = int(input("nhap so thu nhat:"))
# b = int(input("nhap so thu hai:"))
# print(evaluate(a,b,"*"))

# BT: - Viết hàm kiểm tra 1 số có phải số nguyên tố hay không.
# - Liệt kê các số < n

# C1:
# def is_prime(n):
#     if n<2:
#         return 0
#     for v in range(2,n):
#         if n % v ==0:
#             return 0
#     return 1
# so = int(input("nhập số cần kiểm tra:\n"))
# if is_prime(so) ==1:
#     print("là số nguyên tố")
# else:
#     print("không là số nguyên tố")        

# C2:
# def is_prime(n):
#     if n<2:
#         return False
#     for v in range(2,n):
#         if n % v ==0:
#             return False
#     return True
# so = int(input("nhập số cần kiểm tra:\n"))
# if is_prime(so) ==1:
#     print("là số nguyên tố")
# else:
#     print("không là số nguyên tố")        

# - Liệt kê các số < n:
def is_prime(n):
    if n<2:
        return False
    for v in range(2,n):
        if n % v ==0:
            return False
    return True
so = int(input("nhập số cần kiểm tra:\n"))
for v in range(2, so+1):
    if is_prime(v):
        print("số nguyên tố là:",v)
# if is_prime(so) ==1:
#     print("là số nguyên tố")
# else:
#     print("không là số nguyên tố")   
# def A --> chạy thứ 2
# def B
# def C
# print () --> Chạy đầu tiên 