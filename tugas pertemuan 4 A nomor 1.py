# Meminta input nama dari pengguna
nama = input("Masukkan nama Anda: ")

# Menyimpan nama ke dalam file guest.txt
with open("guest.txt", "w") as file:
    file.write(nama)

print("Nama berhasil disimpan ke guest.txt")