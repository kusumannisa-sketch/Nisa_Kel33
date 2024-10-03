def total_belanja(self) -> float:
        """Menghitung total belanja."""
        return sum(item["total"] for item in self.keranjang)

    def checkout(self) -> bool:
        """Proses checkout dan mengembalikan status pembayaran."""
        if not self.keranjang:
            print("Keranjang belanja kosong.\n")
            return False
        
        total_belanja = self.total_belanja()  # Menggunakan metode total_belanja
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
                    return True  # Mengembalikan True jika pembayaran berhasil
                else:
                    print("Uang tidak cukup! Silakan coba lagi.")
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka yang benar.\n")
                return False  # Mengembalikan False jika ada kesalahan input
