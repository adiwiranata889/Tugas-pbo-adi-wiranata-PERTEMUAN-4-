# Membuat list untuk menampung nama
daftar_nama = []

print("Masukkan nama (ketik 'stop' untuk berhenti):")

while True:
    nama = input("Nama: ")
    
    if nama.lower() == "stop":
        break
    daftar_nama.append(nama)

# Menyimpan semua nama ke file
with open("guest_book.txt", "w") as file:
    for nama in daftar_nama:
        file.write(nama + "\n")  # setiap nama di baris baru

print("Semua nama berhasil disimpan ke guest_book.txt")