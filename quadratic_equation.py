import math

def quadratic_equation():
    a = float(input("Nhap a: "))
    b = float(input("Nhap b: "))
    c = float(input("Nhap c: "))

    if a == 0:  # Phương trình bậc nhất hoặc vô nghiệm
        if b == 0:
            if c == 0:
                print("Phuong trinh vo so nghiem")
            else:
                print("Phuong trinh vo nghiem")
        else:
            print(f"Phuong trinh co 1 nghiem: x = {-c / b}")
    else:  # Phương trình bậc 2
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Phuong trinh vo nghiem")
        elif delta == 0:
            x = -b / (2*a)
            print(f"Phuong trinh co nghiem kep: x1 = x2 = {x}")
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"Phuong trinh co 2 nghiem: x1 = {x1}, x2 = {x2}")

# Gọi hàm
quadratic_equation()
