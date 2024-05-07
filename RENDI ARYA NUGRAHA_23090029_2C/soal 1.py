def is_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

tahun = int(input("Masukkan tahun: "))

if is_kabisat(tahun):
    print(tahun, "adalah tahun kabisat.")
else:
    print(tahun, "bukan tahun kabisat.")
