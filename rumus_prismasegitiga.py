#Program mengucapkan selamat datang, sebagai introduction
print ("Selamat Datang di Program Menghitung Luas dan Volume Prisma Segitiga")

#Proses melakukan input tinggi dan jari yang akan dimasukkan
tinggi=int(input("Masukkan tinggi : "))
luasalas=int(input("Masukkan luas alas : "))
luasalas_segitiga=int(input("Masukkan luas alas segitiga : "))
kelilingalas=int(input("Masukkan keliling alas :"))

#Rumus luas dan volume pada prisma segitiga
luas=int((kelilingalas*tinggi) + (2 * luasalas_segitiga))
volume=int(luasalas*tinggi)

#Hasil output setelah proses perhitungan pada rumus luas dan volume pada bola
print ("Luas permukaan prisma segitiga = ", luas)
print ("Volume prisma segitiga = ", volume)