class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        self.harga = harga

    def info_produk(self):
        return f"{self.nama_produk}, Rp {self.harga}"


class Snack(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, "Snack", harga)


class Makanan(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, "Makanan", harga)


class Minuman(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, "Minuman", harga)


class Pegawai:
    def __init__(self, nip, nama, alamat):
        self.nip = nip
        self.nama = nama
        self.alamat = alamat

    def info_pegawai(self):
        return f"Pegawai: {self.nama}, NIP: {self.nip}, Alamat: {self.alamat}"


class Transaksi:
    def __init__(self, no_transaksi, pegawai, produk, jumlah):
        self.no_transaksi = no_transaksi
        self.pegawai = pegawai
        self.produk = produk
        self.jumlah = jumlah

    def total_harga(self):
        return self.produk.harga * self.jumlah

    def info_transaksi(self):
        return (f"Transaksi No: {self.no_transaksi}\n"
                f"Pegawai: {self.pegawai.nama}\n"
                f"Produk: {self.produk.nama_produk}, Jumlah: {self.jumlah}, Total Harga: Rp {self.total_harga()}.")


def main():

    snacks = [
        Snack("S001", "Keripik Kentang", 10000),
        Snack("S002", "Cokelat", 15000),
        Snack("S003", "Kacang Atom", 12000)
    ]

    makanan = [
        Makanan("M001", "Nasi Goreng", 20000),
        Makanan("M002", "Mie Goreng", 25000),
        Makanan("M003", "Ayam Penyet", 30000)
    ]

    minuman = [
        Minuman("D001", "Teh Botol", 5000),
        Minuman("D002", "Air Mineral", 3000),
        Minuman("D003", "Kopi Susu", 10000)
    ]

    pegawai = None
    transaksi = None

    while True:
        print("\n=============== Menu ===============")
        print("1. Pegawai")
        print("2. Lihat Produk")
        print("3. Transaksi")
        print("4. Struk")
        print("5. Perbarui Transaksi")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan (1-6): ")

        if pilihan == '1':
            print("\n=============== PEGAWAI ===============")
            nip = input("Masukkan NIP Pegawai: ")
            nama = input("Masukkan Nama Pegawai: ")
            alamat = input("Masukkan Alamat Pegawai: ")
            pegawai = Pegawai(nip, nama, alamat)
            print("Data pegawai berhasil disimpan.")

        elif pilihan == '2':
            print("\n=============== LIHAT PRODUK ===============")
            print("Pilih produk:")
            print("1. Snack")
            print("2. Makanan")
            print("3. Minuman")

            produk_choice = input("Masukkan pilihan (1-3): ")

            if produk_choice == '1':
                print("Daftar Snack:")
                for index, snack in enumerate(snacks, start=1):
                    print(f"{index}. {snack.info_produk()}")
            elif produk_choice == '2':
                print("Daftar Makanan:")
                for index, food in enumerate(makanan, start=1):
                    print(f"{index}. {food.info_produk()}")
            elif produk_choice == '3':
                print("Daftar Minuman:")
                for index, drink in enumerate(minuman, start=1):
                    print(f"{index}. {drink.info_produk()}")
            else:
                print("Pilihan tidak valid.")

        elif pilihan == '3':
            print("\n=============== TRANSAKSI ===============")
            if pegawai is None:
                print("Silakan masukkan data pegawai terlebih dahulu.")
                continue
            
            no_transaksi = input("Masukkan No Transaksi: ")
            print("Pilih produk untuk transaksi:")
            print("1. Snack")
            print("2. Makanan")
            print("3. Minuman")

            produk_choice = input("Masukkan pilihan (1-3): ")
            if produk_choice == '1':
                for index, snack in enumerate(snacks, start=1):
                    print(f"{index}. {snack.info_produk()}")
                produk_index = int(input("Pilih snack (1-3): ")) - 1
                produk = snacks[produk_index]
            elif produk_choice == '2':
                for index, food in enumerate(makanan, start=1):
                    print(f"{index}. {food.info_produk()}")
                produk_index = int(input("Pilih makanan (1-3): ")) - 1
                produk = makanan[produk_index]
            elif produk_choice == '3':
                for index, drink in enumerate(minuman, start=1):
                    print(f"{index}. {drink.info_produk()}")
                produk_index = int(input("Pilih minuman (1-3): ")) - 1
                produk = minuman[produk_index]
            else:
                print("Pilihan tidak valid.")
                continue

            jumlah = int(input("Masukkan jumlah produk: "))
            transaksi = Transaksi(no_transaksi, pegawai, produk, jumlah)
            print("Transaksi berhasil dibuat.")

        elif pilihan == '4':
            print("\n=============== STRUK ===============")
            if transaksi is not None:
                print(transaksi.info_transaksi())
            else:
                print("Belum ada transaksi yang dibuat.")

        elif pilihan == '5':
            print("\n=============== PERBARUI TRANSAKSI ===============")
            if transaksi is not None:
                print("Pilih detail transaksi yang ingin diperbarui:")
                print(f"1. Jumlah Produk (Saat ini: {transaksi.jumlah})")
                print(f"2. Produk (Saat ini: {transaksi.produk.nama_produk})")
                update_choice = input("Masukkan pilihan (1-2): ")

                if update_choice == '1':
                    jumlah_baru = int(input("Masukkan jumlah baru: "))
                    transaksi.jumlah = jumlah_baru
                    print("Jumlah produk berhasil diperbarui.")
                elif update_choice == '2':
                    print("Pilih produk baru:")
                    print("1. Snack")
                    print("2. Makanan")
                    print("3. Minuman")

                    produk_choice = input("Masukkan pilihan (1-3): ")
                    if produk_choice == '1':
                        for index, snack in enumerate(snacks, start=1):
                            print(f"{index}. {snack.info_produk()}")
                        produk_index = int(input("Pilih snack (1-3): ")) - 1
                        transaksi.produk = snacks[produk_index]
                    elif produk_choice == '2':
                        for index, food in enumerate(makanan, start=1):
                            print(f"{index}. {food.info_produk()}")
                        produk_index = int(input("Pilih makanan (1-3): ")) - 1
                        transaksi.produk = makanan[produk_index]
                    elif produk_choice == '3':
                        for index, drink in enumerate(minuman, start=1):
                            print(f"{index}. {drink.info_produk()}")
                        produk_index = int(input("Pilih minuman (1-3): ")) - 1
                        transaksi.produk = minuman[produk_index]
                    else:
                        print("Pilihan tidak valid.")
                else:
                    print("Pilihan tidak valid.")
            else:
                print("Belum ada transaksi yang dibuat.")

        elif pilihan == '6':
            print("Terima kasih! BYE BYE.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()
