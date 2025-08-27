n = int(input("nhap n: "))
total = 0
for i in range(1, n+1):
    total += i
print (total)
def vong_lap_while():
    a = 1
    total_2 = 0
    while  a <= n:
        total_2 += a
        a += a
    print("tong tu 1 den",n,"=", total)
vong_lap_while()