# Program Kasir Sederhana

def tampilkan_menu():
    print("===== MENU KASIR =====")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang")
    print("3. Hapus Barang")
    print("4. Checkout")
    print("5. Keluar")
    print("======================")

# List untuk menyimpan item belanjaan
keranjang = []

# Fungsi untuk menambahkan barang ke keranjang
def tambah_barang():
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = float(input("Masukkan harga barang: "))
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    total_harga = harga_barang * jumlah_barang
    keranjang.append({"nama": nama_barang, "harga": harga_barang, "jumlah": jumlah_barang, "total": total_harga})
    print(f"{nama_barang} berhasil ditambahkan ke keranjang.\n")


  
