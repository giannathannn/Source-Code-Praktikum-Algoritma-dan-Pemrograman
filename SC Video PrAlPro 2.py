#Bola bermassa 1,2 kg dilemparkan ke atas dari tanah dengan laju 16 m/s.
#Waktu yang diperlukan bola untuk tiba kembali di tanah adalah ... (g = 10 m/s^2)

#Input
massa_bola  = 1.2
kecepatan_awal = 16 
gaya_gravitasi = 10
kecepatan_setelah = 0
#Proses
t = (kecepatan_setelah-kecepatan_awal)/(-gaya_gravitasi)
hasil = 2*t
#Output
print("Waktu yang diperlukan bola untuk tiba kembali di tanah adalah : ",hasil," s")
