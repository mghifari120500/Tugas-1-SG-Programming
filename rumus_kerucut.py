#Program mengucapkan selamat datang, sebagai introduction
print ("Selamat Datang di Program Menghitung Luas dan Volume Kerucut")

#Proses melakukan input tinggi dan jari yang akan dimasukkan
tinggi=int(input("Masukkan tinggi : "))
jari=int(input("Masukkan Jari-jari : "))
pelukis=int(input("Masukkan garis pelukis : "))

#Diketahui phi adalah 22/7 dan sepertiga adalah 1/3
phi=22/7
sepertiga=1/3

#Rumus luas dan volume pada kerucut
luas=int(phi*jari*(jari+pelukis))
volume=int(sepertiga*phi*jari*jari*tinggi)

#Hasil output setelah proses perhitungan pada rumus luas dan volume pada kerucut
print ("Luas kerucut = ", luas)
print ("Volume kerucut = ", volume)