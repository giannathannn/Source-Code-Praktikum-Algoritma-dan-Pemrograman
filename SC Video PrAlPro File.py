
print("^^^^^ DATA AKUN ^^^^^")

while True:

    print("Menu: ")
    print("1. Tambah Akun")
    print("2. Menampilkan Akun")
    print("3. Keluar")

    Readln = int(input("Masukkan menu yang diinginkan: "))

    if Readln == 1:

        HandleWrite = open('dataakun.txt','w')

        Akun = str(input("Masukkan jenis akun: "))
        Username = str(input("Masukkan username: "))
        Password = str(input("Masukkan password: "))

        Line1 = "Akun " + Akun + "\n"
        Line2 = "username: " + Username + "\n"
        Line3 = "password: " + Password + "\n"
        HandleWrite.write(Line1)
        HandleWrite.write(Line2)

        Readln2 = str(input("Apakah passwordnya akan dienkripsi(Y/N): "))

        if Readln2 == "N":
            HandleWrite.write(Line3)
        elif Readln2 == "Y":
            Hasil = ''
            for char in Password:
                KeAscii = ord(char)
                Encrypt = 3 * KeAscii + 11
                HasilEncrypt = chr(Encrypt)
                Hasil += HasilEncrypt
            Line3 = "password: " + Hasil + "\n"
            HandleWrite.write(Line3)
        HandleWrite.close()

    elif Readln == 2:
        HandleRead = open('dataakun.txt','r')
        print("Data Akun")
        for line in HandleRead:
            print(line)

    elif Readln == 3:
        break
    
    else:
        print("Input Salah")