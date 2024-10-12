class DaftarMenu:
    def __init__(self):
        self.menu_makanan = {
            "Mie Ayam": 12000,
            "Bakso": 15000,
            "Soto": 8000,
            "Cilor": 5000,
            "Martabak": 20000
        }
        self.menu_minuman = {
            "Milo": 5000,
            "Matcha": 15000,
            "Jus Alpukat": 7000,
            "Milk Shake": 10000,
            "Air Putih": 3000
        }

        self.harga_otomatis = {
            "Mie Ayam": 12000,
            "Bakso": 15000,
            "Soto": 8000,
            "Cilor": 5000,
            "Martabak": 20000,
            "Milo": 5000,
            "Matcha": 15000,
            "Jus Alpukat": 7000,
            "Milk Shake": 10000,
            "Air Putih": 3000
        }

    def tambah_makanan(self, nama):
        nama = nama.title()
        if nama in self.harga_otomatis:
            harga = self.harga_otomatis[nama]
            self.menu_makanan[nama] = harga
            print(f"Makanan '{nama}' berhasil ditambahkan dengan harga Rp. {harga}")
        else:
            print(f"Makanan '{nama}' tidak ada dalam daftar harga otomatis.")

    def tambah_minuman(self, nama):
        nama = nama.title()
        if nama in self.harga_otomatis:
            harga = self.harga_otomatis[nama]
            self.menu_minuman[nama] = harga
            print(f"Minuman '{nama}' berhasil ditambahkan dengan harga Rp. {harga}")
        else:
            print(f"Minuman '{nama}' tidak ada dalam daftar harga otomatis.")

    def lihat_daftar_makanan(self):
        print("========== Daftar Makanan ==========")
        if self.menu_makanan:
            for makanan, harga in self.menu_makanan.items():
                print(f"{makanan} -> Rp. {harga}")
        else:
            print("Makanan belum ditambahkan.")

    def lihat_daftar_minuman(self):
        print("========== Daftar Minuman ==========")
        if self.menu_minuman:
            for minuman, harga in self.menu_minuman.items():
                print(f"{minuman} -> Rp. {harga}")
        else:
            print("Minuman belum ditambahkan.")

def menu():
    daftar_menu = DaftarMenu()

    while True:
        print("\n========== PILIHAN MENU ==========")
        print("1. Lihat Daftar Makanan")
        print("2. Lihat Daftar Minuman")
        print("3. Tambah Menu")
        print("0. Keluar")
        
        pilihan = input("Masukkan pilihan menu: ")
        if pilihan == "1":
            daftar_menu.lihat_daftar_makanan()

        elif pilihan == "2":
            daftar_menu.lihat_daftar_minuman()

        elif pilihan == "3":
            print("\n========== Tambah Menu ==========")
            jenis_menu = input("Apakah ingin menambahkan Makanan atau Minuman? (Makanan/Minuman): ").lower()
            if jenis_menu == "makanan":
                nama_makanan = input("Masukkan nama makanan: ")
                daftar_menu.tambah_makanan(nama_makanan)
            elif jenis_menu == "minuman":
                nama_minuman = input("Masukkan nama minuman: ")
                daftar_menu.tambah_minuman(nama_minuman)
            else:
                print("Jenis menu tidak valid.")

        elif pilihan == "0":
            print("Terima kasih! Selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()



