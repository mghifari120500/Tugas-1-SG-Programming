# Membuat sambutan
print('Selamat datang di program menentukan nilai maksimum pada kedua bilangan')

def main():
# Melakukan proses input kedua bilangan yang akan dimasukkan
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
 
# Menentukan kedua nilai dengan menggunakan if else
    if a > b:
        max = a
    else:
        max = b
# Mencetak nilai maksimum berdasarkan perbandingan kedua nilai yang telah dimasukkan
    print('Nilai maksimum adalah %d' % max)
 
if __name__ == '__main__':
    main()


    