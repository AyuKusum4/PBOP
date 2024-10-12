debitur_list = [
    {"nama": "Itsuki", "ktp": "234", "limit_pinjaman": 22000000},
    {"nama": "Ryuki", "ktp": "345", "limit_pinjaman": 1800000},
    {"nama": "Sakuya", "ktp": "147", "limit_pinjaman": 6200000},
    {"nama": "Yushi", "ktp": "246", "limit_pinjaman": 8000000},
    {"nama": "Sion", "ktp": "987", "limit_pinjaman": 2000000}
]

pinjaman_list = []

def tampilkan_semua_debitur():
    print("\n=========== Daftar Debitur ============")
    print(f"{'Nama Debitur':<15} {'No KTP':<10} {'Limit Pinjaman'}")
    print("---------------------------------------")
    for debitur in debitur_list:
        print(f"{debitur['nama']:<15} {debitur['ktp']:<10} Rp.{debitur['limit_pinjaman']:,}")
    print("=========================================")

def cari_debitur(nama):
    for debitur in debitur_list:
        if debitur['nama'].lower() == nama.lower():
            return debitur
    return None

def tambah_debitur():
    nama = input("Masukkan Nama Debitur: ")
    ktp = input("Masukkan No KTP Debitur: ")
    limit_pinjaman = int(input("Masukkan Limit Pinjaman: "))

    for debitur in debitur_list:
        if debitur["ktp"] == ktp:
            print("Debitur dengan KTP ini sudah ada. Gagal menambah debitur.")
            return

    debitur_list.append({"nama": nama, "ktp": ktp, "limit_pinjaman": limit_pinjaman})
    print("Debitur berhasil ditambahkan.")

def tambah_pinjaman():
    nama = input("Masukkan Nama Debitur: ")
    debitur = cari_debitur(nama)

    if debitur:
        pinjaman = int(input("Masukkan Jumlah Pinjaman: "))
        
        if pinjaman > debitur['limit_pinjaman']:
            print("Pinjaman melebihi limit! Gagal menambahkan pinjaman.")
        else:
            bunga = float(input("Masukkan Bunga (%): "))
            bulan = int(input("Masukkan Jangka Waktu (bulan): "))
            angsuran = round((pinjaman + (pinjaman * bunga / 100)) / bulan)
            pinjaman_list.append({"nama": nama, "pinjaman": pinjaman, "bunga": bunga, "bulan": bulan, "angsuran": angsuran})
            print("Pinjaman berhasil ditambahkan.")
    else:
        print("Debitur tidak ditemukan. Gagal menambahkan pinjaman.")

def tampilkan_pinjaman():
    print("\n======================== Daftar Pinjaman ========================")
    print(f"{'Nama Debitur':<15} {'Pinjaman':<10} {'Bunga (%)':<10} {'Bulan':<6} {'Angsuran / Bulan'}")
    print("-------------------------------------------------------------------")
    for pinjaman in pinjaman_list:
        print(f"{pinjaman['nama']:<15} Rp.{pinjaman['pinjaman']:<10} {pinjaman['bunga']:<10} {pinjaman['bulan']:<6} Rp.{pinjaman['angsuran']:,}")
    print("===================================================================")

def menu_utama():
    while True:
        print("\n============ Aplikasi Admin Pinjol ============")
        print("1. Kelola Debitur")
        print("2. Pinjaman")
        print("0. Keluar")
        pilihan = input("Masukkan Pilihan: ")
        
        if pilihan == "1":
            kelola_debitur()
        elif pilihan == "2":
            menu_pinjaman()
        elif pilihan == "0":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

def kelola_debitur():
    while True:
        print("\n============ Kelola Debitur ============")
        print("1. Tampilkan Semua Debitur")
        print("2. Cari Debitur")
        print("3. Tambah Debitur")
        print("0. Kembali")
        pilihan = input("Masukkan Pilihan Sub Menu: ")
        
        if pilihan == "1":
            tampilkan_semua_debitur()
        elif pilihan == "2":
            nama = input("Masukkan Nama Debitur: ")
            debitur = cari_debitur(nama)
            if debitur:
                print(f"\nNama: {debitur['nama']}\nNo KTP: {debitur['ktp']}\nLimit Pinjaman: Rp.{debitur['limit_pinjaman']:,}")
            else:
                print("Debitur tidak ditemukan.")
        elif pilihan == "3":
            tambah_debitur()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

def menu_pinjaman():
    while True:
        print("\n============ Menu Pinjaman ============")
        print("1. Tambah Pinjaman")
        print("2. Tampilkan Pinjaman")
        print("0. Kembali")
        pilihan = input("Masukkan Pilihan Sub Menu: ")
        
        if pilihan == "1":
            tambah_pinjaman()
        elif pilihan == "2":
            tampilkan_pinjaman()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

menu_utama()
