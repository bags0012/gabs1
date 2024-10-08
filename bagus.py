print("====latihansederhana===")

nama=input("nama :")
nim=input("nim :")
kelas=input("kelas :")
alamat=input("alamat :")
masukanaksipertama=int(input("masukan aksi pertama :    "))
masukanaksikedua=int(input("masukan aksi kedua :      "))
hasil=(masukanaksipertama+masukanaksikedua)

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Pembagian dengan nol tidak diizinkan."


print("hasil cetak data di atas")
print("nama :"+str(nama))
print("nim"+str(nim))
print("kelas"+str(kelas))
print("masukan aksi pertama"+str(masukanaksipertama))
print("masukan aksi kedua"+str(masukanaksikedua))
print("hasil"+str(hasil))
print("Pilih operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == '1':
    print(f"Hasil: {tambah(angka1, angka2)}")
elif pilihan == '2':
    print(f"Hasil: {kurang(angka1, angka2)}")
elif pilihan == '3':
    print(f"Hasil: {kali(angka1, angka2)}")
elif pilihan == '4':
    print(f"Hasil: {bagi(angka1, angka2)}")
else:
    print("Pilihan tidak valid.")