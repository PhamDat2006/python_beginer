a,b,c = int(input("nhap a: ")),int(input("nhap b: ")),int(input("nhap c: "))
def check():
    if a >= b and a >= c:
        return a
    elif a <= b and a <= c:
        if b > c :
            return b
    else:
        return c
print("so lon nhat la: ",check())