def find_max():
    list_1 = []
    n = 3
    for i in range(n):
        m = int(input(f"Nhap so thu: {i + 1}"))
        list_1.append(m)
    print(f"So lon nhat: {max(list_1)}")
find_max()
def check_integer():
    number = int(input("nhap so: "))
    if number < 2:
        print("isn't prime")
        return
    
    for i in range(2, number - 1):
        if number % i == 0:
            print("isn't prime")
            return
    else:
        print("is prime")
check_integer()
def sum_list():
    number = []
    n = int(input("Nhap danh sach: "))
    for i in range(1, n+1):
        m = int(input(f"Nhap so thu: {i}"))
        number.append(m)
        print(f"Tong 3 so: {sum(number)}")
sum_list()
def multiplication_table():
    n = int(input(f"nhap bang cuu chuong: "))
    for i in range(1,11):
        print(n,'x',i,'=',n*i)
    for i in range(1,11):
        print(n,':',i,'=',n/i)
multiplication_table()