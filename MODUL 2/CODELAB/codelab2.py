data_mahasiswa = [
    {'nama' : 'Karina', 'matkul' : 'Pemrograman Fungsional', 'nilai' : 90},
    {'nama' : 'Seulgi', 'matkul' : 'Pemrograman Mobile', 'nilai' : 56},
    {'nama' : 'Wonyoung', 'matkul' : 'Pemrograman Web', 'nilai' : 95},
    {'nama' : 'Hanni', 'matkul' : 'Piranti Cerdas', 'nilai' : 88},
    {'nama' : 'Jihyo', 'matkul' : 'Jaringan Komputer', 'nilai' : 63},
]

# =======================================================================================
# Codelab 2.a

# Fungsi untuk menghitung nilai rata-rata
def rata_rata(data_mahasiswa):
    total_nilai = sum(mahasiswa['nilai'] for mahasiswa in data_mahasiswa)
    return total_nilai / len(data_mahasiswa)

rata2_nilai = rata_rata(data_mahasiswa)
print("Rata-rata nilai mahasiswa:", rata2_nilai)
print()

# ======================================================================================
# Codelab 2.b

# Fungsi untuk mengubah nilai mahasiswa berdasarkan kelulusan
def kelulusan(data_mahasiswa):
    hasil = []
    
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nilai'] >= 85:
            status = 'sempurna'
        elif mahasiswa['nilai'] >= 60:
            status = 'memenuhi'
        else:
            status = 'gagal'
        
        hasil.append({
            'nama': mahasiswa['nama'],
            'matkul': mahasiswa['matkul'],
            'nilai': status
        })
    
    return hasil

data_lulus = kelulusan(data_mahasiswa)

print("Data kelulusan mahasiswa:", data_lulus)
print()

# =======================================================================================
# Codelab 2.c

# Fungsi generator untuk mencetak nilai genap (karena NIM akhir genap)
def nilai_genap(data_mahasiswa):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nilai'] % 2 == 0:
            yield mahasiswa['nilai']

genap_nilai = nilai_genap(data_mahasiswa)
print("Nilai mahasiswa (genap):", list(genap_nilai))
