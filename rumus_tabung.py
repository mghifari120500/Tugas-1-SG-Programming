#Program mengucapkan selamat datang, sebagai introduction
print ("Selamat Datang di Program Menghitung Luas dan Volume Lingkaran")

#Proses melakukan input tinggi dan jari yang akan dimasukkan
tinggi=int(input("Masukan Tinggi : "))
jari=int(input("Masukan Jari-jari Lingkaran : "))

#Diketahui phi adalah 22/7
phi=22/7

#Rumus luas dan volume pada tabung
luas=int(2*phi*jari*(tinggi+jari))
volume=int((phi*(jari*jari))*tinggi)

#Hasil output setelah proses perhitungan pada rumus luas dan volume pada tabung
print ("Luas tabung = ", luas)
print ("Volume tabung = ", volume)