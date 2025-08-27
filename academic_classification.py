score = float(input("nhap diem: "))
ex,gr,nor,fl = "gioi","kha","TB","yeu"
def rating():
    if score <= 10 and score >= 0:
        if score >= 8.0:
            return ex
        elif score >= 6.5:
            return gr
        elif score >= 5.0:
            return nor
        else:
            return fl
    else:
        return"ko hop le"
print(rating())
