def triangle():
    n = 5 
    for i in range(n):
        print(' '*  (n - i -1) + '*'*(2 * i + 1))
triangle()
def new_triangle():
    n = 6
    for i in range(n+1):
        print(" " * (n - i), end="")
        for j in range(1,2*i):
            if j == 1 or j == 2*i-1 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()
new_triangle()
def rectangle():
    n = 6
    m = 7
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
rectangle()
def matrix():
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

# Duyệt qua từng hàng, từng phần tử
for row in matrix:
    for value in row:
        total += value

print("Tong cac phan tu cua ma tran la:", total)
matrix()