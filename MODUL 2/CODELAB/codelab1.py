def tambah_nilai(data_mahasiswa, nama_matkul, jumlah_nilai):
    hasil = []
    
    for item in data_mahasiswa:
        if item['matkul'] == nama_matkul:
            item_baru = item.copy() 
            item_baru['nilai'] += jumlah_nilai
            print(f"Nilai {nama_matkul} ditambahkan {jumlah_nilai}.\nTotal Nilai {nama_matkul} saat ini {item_baru['nilai']}")
            hasil.append(item_baru)
        else:
            hasil.append(item)

    # Memeriksa apakah mata kuliah ditemukan
    if all(item['matkul'] != nama_matkul for item in hasil):
        print(f"Mata Kuliah {nama_matkul} tidak ditemukan dalam daftar!")
    
    return hasil

def cetak_nilai(data_mahasiswa, nim_akhir_genap):
    for item in data_mahasiswa:
        if nim_akhir_genap:  
            if item['nilai'] % 2 == 0:  
                yield item
        else:  
            if item['nilai'] % 2 != 0:  
                yield item

data_mahasiswa = [
    {'matkul': 'Pemrograman Fungsional', 'nilai': 90},
    {'matkul': 'Pemrograman Mobile', 'nilai': 56},
    {'matkul': 'Pemrograman Web', 'nilai': 95},
    {'matkul': 'Piranti Cerdas', 'nilai': 88},
    {'matkul': 'Jaringan Komputer', 'nilai': 63},
]

print("Nilai Awal : ", data_mahasiswa)

nama_matkul = input("Masukkan nama mata kuliah tambahan: ")
jumlah_nilai = int(input("Masukkan jumlah nilai yang ingin ditambahkan: "))

data_mahasiswa_baru = tambah_nilai(data_mahasiswa, nama_matkul, jumlah_nilai)

print("Nilai Update : ", data_mahasiswa_baru)
print()

nim_akhir_genap = True  

nilai_gen = cetak_nilai(data_mahasiswa_baru, nim_akhir_genap)

if nim_akhir_genap:
    print("Nilai dengan NIM Genap (Menggunakan next()):")
    try:
        while True:
            print(next(nilai_gen))
    except StopIteration:
        pass
else:
    print("Nilai dengan NIM Ganjil (Menggunakan for loop):")
    for nilai in nilai_gen:
        print(nilai)
