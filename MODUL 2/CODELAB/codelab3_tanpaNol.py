while True:
    try:
        # Meminta input tanggal lahir dari pengguna
        tanggal_lahir = int(input("Masukkan tanggal lahir (angka): "))
        
        # Memastikan tanggal lahir adalah angka positif
        if tanggal_lahir <= 0:
            raise ValueError("Tanggal lahir harus berupa angka positif.")
        break  # Keluar dari loop jika input valid
    except ValueError as e:
        print(f"Kesalahan: {e}. Silakan masukkan angka yang valid.")

# Generator expression untuk mencari kelipatan tanggal lahir, mulai dari 1
kelipatan = (i for i in range(1, 1000) if i % tanggal_lahir == 0)

# Casting ke list dan slicing untuk mengambil 10 data pertama
hasil = list(kelipatan)[:10]

# Menampilkan hasil
print(hasil)
