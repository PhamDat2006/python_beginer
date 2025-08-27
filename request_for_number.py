#Nhập vào một số, yêu cầu nhập lại đến khi nào số đó > 0 thì dừng.
while True:
    i = int(input("nhap so: "))
    if i > 0:
        break
    else:
        print("Nhap lai")
