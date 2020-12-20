#Program mengucapkan selamat datang, sebagai introduction
print ("Selamat Datang di Program Menghitung Luas dan Volume Bola")

#Proses melakukan input tinggi dan jari yang akan dimasukkan
tinggi=int(input("Masukkan tinggi : "))
jari=int(input("Masukkan Jari-jari : "))

#Diketahui phi adalah 22/7 dan empatpertiga adalah 4/3
phi=22/7
empatpertiga=4/3

#Rumus luas dan volume pada bola
luas=int(4*22/7*(r*r))
volume=int(4/3*22/7*(r*r*r))

#Hasil output setelah proses perhitungan pada rumus luas dan volume pada bola
print ("Luas bola = ", luas)
print ("Volume bola = ", volume)