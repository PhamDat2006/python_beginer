#Bài 1: Nhập danh sách số và tính tổng, trung bình
def test_1():
    number = []
    n =  int(int(input("nhap so phan tu: ")))
    for i in range(n + 1):
        x = int(input("nhap danh sach thu: ",{i + 1}))
        number.append(x)
    print("danh sach: ",number)
    total = number.sum(x)
    print("tong: ",total)
    print("TB: ",{total/n})
test_1()
#Bài 2: Tìm số lớn nhất và nhỏ nhất trong danh sách
def test_2():
    number = [1,2,3,4,5,6]
    max(number)
    min(number)
test_2()
#Bài 3: Sắp xếp danh sách tăng dần và giảm dần
def test_3():
    number = [1,2,3,4,5,6]
    number.sort()
    number.sort(reverse=True)
test_3()
#Bài 4: Nhập danh sách tên rồi sắp xếp theo ABC
def test_4():
    names = []
    n = int(input("nhap so luong danh sach: "))
    for i in range(n+1):
        name = str(input("nhap danh sach ten thu: ",{i + 1}))
        names.append(name)
    names.sort()
    print("Danh sách sắp xếp A-Z:", names)

    names.sort(reverse=True)
    print("Danh sách sắp xếp Z-A:", names)
test_4()
