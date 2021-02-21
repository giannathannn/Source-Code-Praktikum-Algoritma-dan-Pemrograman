#Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. 
#On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. 
#Each flagstone is of the size a × a.

#What is the least number of flagstones needed to pave the Square? 
#It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. 
#It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.

#Input 
n = int(input("Masukkan ukuran n : ")) 
m = int(input("Masukkan ukuran m : ")) 
a = int(input("Masukkan ukuran a : ")) 

#Proses 
if n % a == 0 :
    panjang = n//a 
else :
    panjang = n//a + 1

if m % a == 0 :
    lebar = m//a 
else :
    lebar = m//a + 1 

hasil = panjang * lebar

#Output 
print("Jadi jumlah flagstone yang dibutuhkan untuk menutupi Theatre Square adalah ",hasil)
