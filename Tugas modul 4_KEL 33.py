class Kasir:
    def __init__(self):
        self.keranjang = []

    def tampilkan_menu(self):
        print("===== MENU KASIR =====")
        print("1. Tambah Barang")
        print("2. Lihat Keranjang")
        print("3. Hapus Barang")
        print("4. Checkout")
        print("5. Keluar")
        print("======================")

    def tambah_barang(self):
        # Menggunakan variabel dan tipe data
        nama_barang = input("Masukkan nama barang: ")
        harga_barang = float(input("Masukkan harga barang: "))
        jumlah_barang = int(input("Masukkan jumlah barang: "))
        
        # Menghitung total harga
        total_harga = harga_barang * jumlah_barang
        
        # Menambahkan item ke keranjang (array/list)
        self.keranjang.append({
            "nama": nama_barang,
            "harga": harga_barang,
            "jumlah": jumlah_barang,
            "total": total_harga
        })
        print(f"{nama_barang} berhasil ditambahkan ke keranjang.\n")

   
