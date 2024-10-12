from typing import List, Dict, Optional

# Data penjualan alat musik
data_penjualan: List[Dict[str, Optional[str]]] = [
    {"id_produk": "GN001", "nama_produk": "Gitar Akustik", "harga": 1500000, "quantity": 3, "tanggal": "2024-08-05"},
    {"id_produk": "GN002", "nama_produk": "Piano Digital", "harga": 7500000, "quantity": 1, "tanggal": "2024-08-05"},
    {"id_produk": "GN003", "nama_produk": "Biola", "harga": 3000000, "quantity": 2, "tanggal": "2024-08-05"},
    {"id_produk": "GN004", "nama_produk": "Drum Set", "harga": 5000000, "quantity": 1, "tanggal": "2024-08-06"},
    {"id_produk": "GN005", "nama_produk": "Ukulele", "harga": 500000, "quantity": 5, "tanggal": "2024-08-06"},
    {"id_produk": "GN006", "nama_produk": "Saxophone", "harga": 4500000, "quantity": 1, "tanggal": "2024-08-06"},
    {"id_produk": "GN007", "nama_produk": "Keyboard", "harga": 2000000, "quantity": 4, "tanggal": "2024-08-07"},
    {"id_produk": "GN008", "nama_produk": "Clarinet", "harga": 3000000, "quantity": 2, "tanggal": "2024-08-07"},
    {"id_produk": "GN009", "nama_produk": "Tamborin", "harga": 750000, "quantity": 6, "tanggal": "2024-08-07"},
    {"id_produk": "GN010", "nama_produk": "Flute", "harga": 1200000, "quantity": 3, "tanggal": "2024-08-08"},
    {"id_produk": "GN011", "nama_produk": "Trompet", "harga": 2500000, "quantity": 2, "tanggal": "2024-08-08"},
    {"id_produk": "GN012", "nama_produk": "Gitar Listrik", "harga": 2000000, "quantity": 2, "tanggal": "2024-08-08"},
]

def tampilkan_judul() -> None:
    """Menampilkan judul laporan."""
    print("===== Laporan Data Penjualan Ramd's Music =====\n")

def hitung_pendapatan(data: List[Dict[str, Optional[str]]]) -> List[Dict[str, Optional[float]]]:
    """Menghitung pendapatan dari setiap produk."""
    hasil = []
    for item in data:
        total_pendapatan = item['harga'] * item['quantity']
        hasil.append({
            "id_produk": item["id_produk"],
            "nama_produk": item["nama_produk"],
            "harga": item["harga"],
            "quantity": item["quantity"],
            "tanggal": item["tanggal"],
            "pendapatan": total_pendapatan
        })
    return hasil

def average_penjualan(data: List[Dict[str, Optional[str]]], tanggal: str) -> float:
    """Menghitung rata-rata penjualan pada tanggal tertentu."""
    total_pendapatan = 0
    total_produk = 0
    for item in data:
        if item['tanggal'] == tanggal:
            total_pendapatan += item['harga'] * item['quantity']
            total_produk += item['quantity']
    if total_produk == 0:
        raise ValueError("Tidak ada penjualan pada tanggal tersebut")
    return total_pendapatan / total_produk  # Rata-rata pendapatan per unit terjual

def total_penjualan(data: List[Dict[str, Optional[float]]]) -> Dict[str, float]:
    """Menghitung total penjualan per tanggal."""
    total_per_tanggal = {}
    for item in data:
        tanggal = item['tanggal']
        total_per_tanggal[tanggal] = total_per_tanggal.get(tanggal, 0) + item['pendapatan']
    return total_per_tanggal

def tampilkan_pendapatan(data: List[Dict[str, Optional[float]]]) -> None:
    """Menampilkan informasi pendapatan."""
    for item in data:
        print(f"Product ID: {item['id_produk']}")
        print(f"Nama Produk: {item['nama_produk']}")
        print(f"Harga: Rp {item['harga']}")
        print(f"Jumlah: {item['quantity']}")
        print(f"Tanggal: {item['tanggal']}")
        print(f"Pendapatan: Rp {item['pendapatan']}\n")

def tampilkan_total_penjualan(total_per_tanggal: Dict[str, float]) -> None:
    """Menampilkan total penjualan per tanggal."""
    print("\nTotal Penjualan per Tanggal:")
    for tanggal, total in total_per_tanggal.items():
        print(f"Tanggal: {tanggal}, Total Penjualan: Rp {total}")

def validasi_tanggal(tanggal: str) -> bool:
    """Validasi format tanggal."""
    try:
        # Cek format tanggal YYYY-MM-DD
        year, month, day = map(int, tanggal.split('-'))
        if year < 1 or month < 1 or month > 12 or day < 1 or day > 31:
            return False
        return True
    except ValueError:
        return False

def validasi_id_produk(id_produk: str) -> Optional[Dict[str, Optional[str]]]:
    """Validasi ID Produk dan kembalikan informasi produk."""
    id_produk = id_produk.upper()  # Konversi ke huruf besar
    for item in data_penjualan:
        if item['id_produk'] == id_produk:
            return item
    return None

def input_data_penjualan() -> Dict[str, Optional[str]]:
    """Input data penjualan manual dari pengguna."""
    try:
        id_produk = input("Masukkan ID Produk: ")
        produk = validasi_id_produk(id_produk)  # ID produk sudah bisa huruf kecil atau besar
        if produk is None:
            raise ValueError(f"ID Produk '{id_produk}' tidak valid.")

        quantity = int(input("Masukkan Jumlah: "))
        
        tanggal = input("Masukkan Tanggal (YYYY-MM-DD): ")
        if not tanggal:  # Memastikan tanggal tidak kosong
            raise ValueError("Tanggal wajib diisi.")

        if not validasi_tanggal(tanggal):
            raise ValueError("Format tanggal tidak valid. Harus dalam format YYYY-MM-DD.")

        return {
            "id_produk": produk["id_produk"],  # Tetap dalam huruf besar
            "nama_produk": produk["nama_produk"],
            "harga": produk["harga"],
            "quantity": quantity,
            "tanggal": tanggal
        }
    except ValueError as e:
        print(f"Kesalahan: {e}")
        return {}

def main_menu() -> None:
    """Menampilkan menu utama dan menjalankan program sesuai pilihan pengguna."""
    while True:
        print("\n===== RAMD`S MUSIC =====")
        print("1. Laporan Data Penjualan Ramd's Music")
        print("2. Input Data Penjualan Manual")
        print("3. Exit Program")

        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == '1':
            tampilkan_judul()  # Menampilkan judul laporan
            pendapatan = hitung_pendapatan(data_penjualan)
            tampilkan_pendapatan(pendapatan)

            # Menghitung total penjualan per tanggal
            total_per_tanggal = total_penjualan(pendapatan)

            # Loop untuk meminta tanggal atau keluar
            while True:
                tanggal_input = input("\nMasukkan tanggal yang ingin dicari untuk melihat rata-rata penjualan (YYYY-MM-DD) atau ketik 'exit' untuk keluar: ")
                if tanggal_input.lower() == 'exit':
                    print("Kembali ke menu utama.")
                    break
                if not validasi_tanggal(tanggal_input):
                    print("Masukkan tanggal dalam format YYYY-MM-DD")
                    continue
                try:
                    rata_rata = average_penjualan(data_penjualan, tanggal_input)
                    print(f"Rata-rata penjualan pada tanggal {tanggal_input}: Rp {rata_rata:.2f}")
                except ValueError as e:
                    print(e)

                # Menampilkan total penjualan per tanggal setelah menghitung rata-rata
                tampilkan_total_penjualan(total_per_tanggal)

        elif pilihan == '2':
            data_baru = input_data_penjualan()
            if data_baru:
                data_penjualan.append(data_baru)
                print("Data penjualan berhasil ditambahkan.")

        elif pilihan == '3':
            print("Terima kasih Sudah Mampir di Toko Ramd's Music.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan menu utama
main_menu()
