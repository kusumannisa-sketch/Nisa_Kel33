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
