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
                if self.checkout():  # Memeriksa status checkout
                    print("Checkout berhasil.")
                else:
                    print("Checkout gagal.")
            elif pilihan == "5":
                print("Terima kasih telah menggunakan kasir kami!")
                break
            else:
                print("Pilihan tidak valid.\n")


# Menjalankan program utama
if __name__ == "__main__":
    kasir = Kasir()  # Membuat objek dari kelas Kasir
    kasir.jalankan()  # Memulai program kasir
