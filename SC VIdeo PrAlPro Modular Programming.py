
def prima(n):
    hasil = "2 "
    for i in range(3, n):
        angka = 1
        for j in range(2,i-1):
            if (i % j == 0):
                angka = 0
        if (angka == 1):
            hasil += str(i) + " "
    return hasil

n = int(input("Masukkan batas angka :"))
print(prima(n))
