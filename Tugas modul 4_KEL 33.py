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
                print("Nomor barang tidak valid.\n")
                def checkout(self):
        if not self.keranjang:
            print("Keranjang belanja kosong.\n")
        else:
            total_belanja = sum(item["total"] for item in self.keranjang)
            print("===== STRUK PEMBAYARAN =====")
            self.lihat_keranjang()
            print(f"Total yang harus dibayar: Rp{total_belanja}")

            # Menggunakan pengkondisian untuk memeriksa pembayaran
            while True:
                try:
                    bayar = float(input("Masukkan jumlah uang yang dibayarkan: "))
                    if bayar >= total_belanja:
                        kembalian = bayar - total_belanja
                        print(f"Pembayaran berhasil. Kembalian Anda: Rp{kembalian}\n")
                        self.keranjang.clear()  # Mengosongkan keranjang setelah checkout
                        break
                    else:
                        print("Uang tidak cukup! Silakan coba lagi.")
                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka yang benar.\n")
                    def jalankan(self):
        while True:
            self.tampilkan_menu()
            pilihan = input("Pilih menu: ")

            # Menggunakan pengkondisian untuk menangani pilihan
            if pilihan == "1":
                self.tambah_barang()
            elif pilihan == "2":
                self.lihat_keranjang()
            elif pilihan == "3":
                self.hapus_barang()
            elif pilihan == "4":
                self.checkout()
            elif pilihan == "5":
                print("Terima kasih telah menggunakan kasir kami!")
                break
            else:
                print("Pilihan tidak valid.\n")


# Menjalankan program utama
if __name__ == "__main__":
    kasir = Kasir()  # Membuat objek dari kelas Kasir
    kasir.jalankan()  # Memulai program kasir


