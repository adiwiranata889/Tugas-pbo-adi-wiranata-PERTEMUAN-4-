print("Program penjumlahan (ketik 'stop' untuk keluar)")

while True:
    try:
        angka1 = input("Masukkan angka pertama: ")
        
        if angka1.lower() == "stop":
            break

        angka2 = input("Masukkan angka kedua: ")
        
        if angka2.lower() == "stop":
            break

        # Konversi ke integer
        angka1 = int(angka1)
        angka2 = int(angka2)

        hasil = angka1 + angka2
        print(f"Hasil: {hasil}\n")

    except ValueError:
        print("Input tidak valid! Harus berupa angka.\n")