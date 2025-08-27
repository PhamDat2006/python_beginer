import random
treasure = random.randint(1,10)
while True:
    n = int(input("nhap so can doan: "))
    if n == treasure:
        print("doan dung")
        break
    else:
        print("nhap lai")
