#Program mengucapkan selamat datang, sebagai introduction
print ("Selamat Datang di Program Menghitung Luas dan Volume Balok")

#Proses melakukan input tinggi dan jari yang akan dimasukkan
panjang=int(input("Masukkan panjang : "))
lebar=int(input("Masukkan lebar : "))
tinggi=int(input("Masukkan tinggi : "))


#Rumus luas dan volume pada balok
luas=int(2 * (panjang*lebar) + (panjang*tinggi) + (lebar*tinggi))
volume=int(panjang * lebar * tinggi)

#Hasil output setelah proses perhitungan pada rumus luas dan volume pada balok
print ("Luas balok = ", luas)
print ("Volume balok = ", volume)