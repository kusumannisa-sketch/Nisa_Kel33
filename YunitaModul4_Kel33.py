class Kasir:
    def _init_(self):
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

    def lihat_keranjang(self):
        if not self.keranjang:
            print("Keranjang belanja kosong.\n")
        else:
            print("===== KERANJANG BELANJA =====")
            for i, item in enumerate(self.keranjang, 1):
                # Menggunakan pengulangan untuk menampilkan setiap item
                print(f"{i}. {item['nama']} - {item['jumlah']} x Rp{item['harga']} = Rp{item['total']}")
            print("==============================\n")

    def hapus_barang(self):
        self.lihat_keranjang()
        if self.keranjang:
            pilihan = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
            # Menggunakan pengkondisian untuk memeriksa validitas input
            if 0 <= pilihan < len(self.keranjang):
                barang_terhapus = self.keranjang.pop(pilihan)
                print(f"{barang_terhapus['nama']} berhasil dihapus dari keranjang.\n")
            else:
