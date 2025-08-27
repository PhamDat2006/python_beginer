def object_1():#Nhập 5 số từ bàn phím, lưu vào list và in ra.
    numbers = []
    for i in range(5):
        num = int(input(f"nhap so thu {i+1}: "))
        numbers.append(num)
    print("Danh sách vừa nhập:", numbers)
#object_1()
def object_2():#Tính tổng và giá trị trung bình của list.
    numbers = [1, 2, 3, 4, 5]
    print("Tong:", sum(numbers))
    print("TB: ", sum(numbers)/len(numbers))
#object_2()
def object_3():#Tìm số lớn nhất và nhỏ nhất trong list.
    numbers = [1, 2, 3, 4, 5]
    print(max(numbers))
    print(min(numbers))
#object_3()
def object_4():#Sắp xếp list theo thứ tự tăng dần và giảm dần.
    numbers = [1, 2, 3, 4, 5]
    numbers.sort()
    sorted_numbers = sorted(numbers, reverse=True)
    print(numbers)
    print(sorted_numbers)
#object_4()
def object_5():#Viết chương trình nhập tên của n người và in ra theo thứ tự ABC.
    names=[]
    n = int(input("so nguoi can nhap ten: "))
    for i in range(n):
        name = input(f"nhap ten {i+1}: ")
        names.append(name)
    names.sort()
    print(f"ten da sap xep",names)
object_5()