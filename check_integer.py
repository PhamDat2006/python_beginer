def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
num  = int(input("Nhap so "))
if is_prime(num):
    print(num,"la so nguyen to")
else:
    print(num,"khong la so nguyen to")
        