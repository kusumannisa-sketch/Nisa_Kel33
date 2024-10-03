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
                print("Nomor barang tidak valid.\n")
