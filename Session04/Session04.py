# Can luu tru danh sach cac mat hang trong cua hang
#  - Bad: dung tap cac bien de luu. Mat_hang_1, mat_hang_2 ...mat_hang_n
# mat_hang_1 = "Quan jean"
# mat_hang_2 = "Ao so mi"
# mawt_hang_3 = "Ao phong"
# --> dai dong. Khi can tong hop, in ra cac mat hang thi sao?
# --> Them hang moi bo hang cu thi sao?
# Can co 1 cau truc du lieu luu tru linh dong, ngan gon, tuong thich tot voi cac vong lap


# cau truc du lieu + thuat toan = chuong trinh
# Listy la cac phan tu lien tiep nhau
# String la 1 mang cac ky tu
# List = [1,2,3,4] 
# string = "helllo"
# len(list) --> do dai list
# len(str)--> do dai chuoi
# range(5)??????????????

# colors=("red","green", "blue")
# b=colors
# # b[0]= "yellow" --> khong tao ra list moi ma tro den 1 list da co ??????????????????????????????
# print(colors[0])

# 4 thao tac co ban cua co so du lieu: CRUD
# Create, read, update, delete
# Create:
# - Append: list.append(element) --> Them phan tu vao sau cung
# - Insert: list.insert(index, element) --> chen vao vi tri
# - Extend: list.extend(list2)
# Update:
# Delete: --> 
# - Delete by index: del.colors[index] --> khong tra ve gia tri
# - Delete by index:     colors.pop(index) --> xoa va tra ve gia tri da xoa
# - Delete first item: 

# Slices:
# - list.reverse()
# - list.clean()
# BT:
# Nhap n so nguyen tu ban phim:
# - In ra day so vua nhap
# - Tim cac cap so trong day co tong la 1 so chan

# n=input("Nhap so n:\n")
# print("day so ban vua nhap la:", n)
# print(n)
# 0 --> 0,1,2
# 1--> 0,1,2
# --> 2 vong for long nhau
# m=3
# n=4
# ds=[1,5,2,4]
# # ds[1]
# for i in range(m):
#     for j in range(i+1,n):
#         print('i=', i,'j=',j,'cap la:',ds[i],'-',ds[j])
#         if (ds[i]+ds[j])% 2 ==0:
#             print('cap so can tim la:',ds[i],' ', ds[j])

#BT: Tim bo ba so x, y,z sao cho:
# 0<= x,y,z<+ 100
# x^2 + y^2 + z^2 = x.y.z

# a = []
# n=int(input("nhap n:"))
# for i in range(n):
#     n = int(input("nhap gia tru:",j))
#     a.append(n)
# for i in range(n):
#     for j in range(i+1,n):
#         if (a[1]+a[j])% 2 ==0:
#             print(a[i],a[j])

# Dictionary --> cau truc luu tru du lieu --> 4 thao tac co ban: CRUD
# Cap key value pair:  <key>.<value>
# - Bieu dien ro rang, de hieu, truc Quan
# - Truy cap de dang, chinh xac
# - Tai sao dung list lai khong tot, khi nao thui nen dung dict
# Create:
# person = {"name","Nguyen Van A"}
# person['age']
# key:
# - Phai la kieu bat bien:string, so, tuple,...
# - Khong duoc trung lap
# value:

# Read:
# dung dict vi cac phan tu khong lien tiep nhau, nen chi so khong co y nghia, can dung key.
# person ={"name":"nguyen van a",'age':12,"address":"ha noi"}
# if "address" in person:
#     addr=person['person']
# add=person['address']

# - Khi lam viec voi list thi phai xem chi so co hop le hay khong
# Update:
# cap nhat la thay the value cho 1 key da co. Neu key chua co
# Delete:
# BT:
# Tao ra 1 chuong trinh luu tru tu dien tieng anh
# - mac dinh co cac tu sau:computer, mouse, keyboard
# - Khi chay moi ng dung nhap 1 tu vao (*)
# + Neu tu do co trong tu dien thi in ra nghia cua tu:  xong quay lai *
# - Neu khong: Thong bao tu nay khong co trong tu dien: quay lai *
# + Neu nguoi dung nhap vao "exit"; "quit" thi thoat khoi ung dung

# dic = {"computer":"may tinh", "mouse":"chuot", "keyboard":"ban phim"}
# while True:
#     tukhoa = input("Nhap tu tim kiem:\n")
#     if tukhoa in dic:
#         print("Tu khong co trong tu dien")
#         print(dic[tukhoa])
#     elif tukhoa == "exit":
#         break
#     elif tukhoa == "quit":
#         break
#     else:
#         print("Tu khong co trong tu dien")

# Loop in dict
# Voi bai tu dien da lam. lam sao de biet dc trong tu dien da co nhung tu nao?
# - duyet theo key: for v in dict:
# - duyet theo value: for v in dic.value(:)
# - duyet theo key-value: 
# Dict va List:

tap_nguoi=[]
nguoi_1={
    "name":"nguyn van a",
    "age":"12",
    "add":"ha noi",
    "sdt":["01234", "45678"]
}
tap_nguoi.append{nguoi_2}
print{tap_nguoi[0]['age']}
for v in tap_nguoi:
    print([tap_nguoi])