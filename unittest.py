# ==========================
# UNIT TEST KALKULATOR
# ==========================

import unittest

# Import fungsi dari kalkulator
# (Jika file terpisah, gunakan: from kalkulator import tambah, kurang, kali, bagi)

class TestKalkulator(unittest.TestCase):

    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)

    def test_kurang(self):
        self.assertEqual(kurang(5, 3), 2)

    def test_kali(self):
        self.assertEqual(kali(2, 4), 8)

    def test_bagi(self):
        self.assertEqual(bagi(10, 2), 5)

    def test_bagi_nol(self):
        with self.assertRaises(ValueError):
            bagi(10, 0)


# Menjalankan test
if __name__ == "__main__":
    unittest.main()