import random

welcome_message = "welcome cuppy games!"
cuppy_posisi = random.randint(1,3)
# print("##########################")
print(f"## {welcome_message} ##")
# print("##########################")
nama_user = input ("masukan nama anda : ")

print(f'''hai {nama_user}! coba perhatikan goa di bawah ini
  L_l L_l L_l''')

pilihan_user = int(input(" menurut kamu dimana cupy berada?[1][2][3] "))


if pilihan_user == cuppy_posisi:
    print(f"selamat {nama_user} kamu giting!kamu memilih{cuppy_posisi} dan kamu bebas giting disini {pilihan_user}.")
else:
    print(f"kamu kalah cuppy yang giting! seharusnya giting disni {cuppy_posisi} disini tempat cuppy giting di {pilihan_user}.")



