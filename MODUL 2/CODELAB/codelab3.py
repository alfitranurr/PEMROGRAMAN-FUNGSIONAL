while True:
    try:
        tanggal_lahir = int(input("Masukkan tanggal lahir (angka): "))
        if tanggal_lahir <= 0:
            raise ValueError("Tanggal lahir harus berupa angka positif.")
        break  
    except ValueError as e:
        print(f"Kesalahan: {e}. Silakan masukkan angka yang valid.")

kelipatan = (i for i in range(1000) if i % tanggal_lahir == 0)

hasil = list(kelipatan)[:10]

print(hasil)
