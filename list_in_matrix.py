#Bài 1: Nhập ma trận và in ra
def test_1():    
    rows = int(input("nhap so dong: "))
    cols = int(input("nhap so cot: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            x = int(input(f"nhap phan tu: [{i},{j}]"))
            row.append(x)
        matrix.append(row)
    print("Ma tran vua nhap: ")
    for row in matrix:
        print(row)
    #Bài 2: Tính tổng các phần tử trong ma trận
    total = 0 
    for row in matrix:
        total += sum(row)
    print("Tổng các phần tử trong ma trận:", total)
    #Bài 3: Tính tổng từng hàng
    for i in range(rows):
        print(f"Tong hang {i + 1}: ", sum(matrix[i]))
    #Bài 4: Tính tổng từng cột
    for j in range(cols):
        col_sum = 0
        for i in range(rows):
            col_sum += matrix[i][j]
        print(f"Tong cot {j+1}: ", col_sum)
    #Bài 5: Tìm phần tử lớn nhất trong ma trận
    max_val = matrix[0][0]
    for row in matrix:
        if max(row) > max_val:
            max_val = max(row)
    print("Phan tu lon nhat trong ma tran: ", max_val)