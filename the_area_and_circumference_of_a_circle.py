pi = 3.14

def the_area_and_circumference():
    print("1: Nhập bán kính")
    print("2: Nhập đường kính")
    i = int(input("Nhập lựa chọn: "))

    if i == 1:
        r = float(input("Nhập bán kính: "))
    else:
        d = float(input("Nhập đường kính: "))
        r = d / 2

    S = r**2 * pi
    C = 2 * r * pi

    print(f"Dien tich: {S}, Chu vi: {C}")
    return S, C

the_area_and_circumference()