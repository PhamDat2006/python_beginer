a = int(input("nhap a: "))
b = int(input("nhap b: "))
if a == 0 and b==0:
    print("co vo so nghiem")
elif a == 0 and b!= 0:
    print("pt vo nghiem")
else:
    print(f"phuong trinh co nghiem x = {float(-b/a)}")