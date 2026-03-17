try:
    angka1 = input("Masukkan angka pertama: ")
    angka2 = input("Masukkan angka kedua: ")

    # Konversi ke integer
    angka1 = int(angka1)
    angka2 = int(angka2)

    hasil = angka1 + angka2
    print(f"Hasil penjumlahan: {hasil}")

except ValueError:
    print("Oops! Input harus berupa angka, bukan teks.")