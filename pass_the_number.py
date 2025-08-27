def number_5():
    for i in range(1,10):
        if i == 5:
            pass
        else:
            print(i)
number_5
def pass_even_number():
    for n in range(1,20):
        if n % 2 == 0:
            pass
        else:
            print(n)
pass_even_number
def quadratic_equation():
    pass
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Choi game")
        print("2. Xem diem")
        print("3. Thoat")

        choice = input("Nhap lua chon (1-3): ")

        if choice == "1":
            # Tạm thời chưa viết code game
            pass  
        elif choice == "2":
            # Tạm thời chưa viết code xem điểm
            pass
        elif choice == "3":
            print("Thoat chuong trinh...")
            break
        else:
            print("Lua chon khong hop le, vui long nhap lai!")
