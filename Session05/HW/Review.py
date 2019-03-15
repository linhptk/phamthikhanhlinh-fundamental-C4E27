Review
# 1. Why should we use functions at all?  
# --> Vì hàm có thế sử dụng lại, có thể gọi hàm nhiều lần trong 1 chương trình hoặc có thể quay lại chương trình 
# cũ tìm các hàm cần và sử dụng hàm đó trong chương trình mới.

# 2. How to define/declare a function? 
# --> "def functionName( parameters ):
#     ""Mô tả ngắn về hàm""
#     codes ...
#     return [expression]
# - Một hàm bắt đầu bởi từ khóa def (Viết tắt của từ define), theo sau đó 
# là tên của hàm.
# - Tiếp theo là danh sách các tham số nằm trong cặp đấu ngặc ( ) và dấu 
# hai chấm ( : ), hàm có thể có 0, 1 hoặc nhiều tham số, các tham số cách 
# nhau bởi dấu phẩy.
# - Dòng đầu tiên của thân hàm (function body) là một chuỗi mô tả ngắn về 
# hàm (Không bắt buộc).

# 3. How to call/use a function?
# -->    Để gọi một hàm, chỉ cần gõ tên hàm và truyền 
# các tham số thích hợp.

# 4. What is return, why and how do we use it?
# --> return là lệnh trả về 1 giá trị (hoặc 1 biểu thức hoặc không gì cả)
#  Khi lệnh return được thực thi hàm sẽ kết thúc

# 5. Do we have to use return in every function?
# --> return là lệnh không bắt buộc phải có trong thân hàm

# 6.What are function arguments/parameters, why and how we use it?
# --> arguments: các đối số để truyền cho tham số 
# parameters: các tham số để truyền cho hàm

# 7. How to use function from a different file other than our currently 
# working file?
# --> Viết from file import function và gọi hàm. 
# Khi muốn sử dụng hàm từ file này cho file khác cần phải chắc chắn rằng cả 2 file đều nằm trong cùng 1 thư mục