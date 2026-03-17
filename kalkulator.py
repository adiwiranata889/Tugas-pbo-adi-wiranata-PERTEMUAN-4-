# ==========================
# KALKULATOR SEDERHANA
# ==========================

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        raise ValueError("Tidak bisa dibagi dengan nol!")
    return a / b


# Program utama (opsional untuk dijalankan)
if __name__ == "__main__":
    print("Kalkulator Sederhana")
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    operasi = input("Pilih operasi (+, -, *, /): ")

    if operasi == "+":
        print("Hasil:", tambah(a, b))
    elif operasi == "-":
        print("Hasil:", kurang(a, b))
    elif operasi == "*":
        print("Hasil:", kali(a, b))
    elif operasi == "/":
        try:
            print("Hasil:", bagi(a, b))
        except ValueError as e:
            print(e)
    else:
        print("Operasi tidak valid!")