import mysql.connector
from tabulate import tabulate

conn = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "",
    database = "pbo_penjualan",
    port=3307
)

cur = conn.cursor()

# Membuat Table Pegawai
cur.execute("""CREATE TABLE IF NOT EXISTS Pegawai (
                NIK CHAR(4) NOT NULL PRIMARY KEY,
                Nama VARCHAR(50), 
                Alamat VARCHAR(255)
            )""")

# Membuat Table Transaksi
cur.execute("""CREATE TABLE IF NOT EXISTS Transaksi (
                No_Transaksi CHAR(4) NOT NULL PRIMARY KEY,
                Detail_Transaksi VARCHAR(255)
            )""")

# Membuat Table Struk
cur.execute("""CREATE TABLE IF NOT EXISTS Struk (
                No_Transaksi CHAR(4) NOT NULL,
                Nama_Pegawai VARCHAR(50),
                Nama_Produk VARCHAR(50),
                Jumlah_Produk INT,
                Total_Harga FLOAT
            )""")

# Membuat Table Produk 
cur.execute("""CREATE TABLE IF NOT EXISTS Produk (
                Kode_Produk INT NOT NULL PRIMARY KEY,
                Nama_Produk VARCHAR(50), 
                Jenis_Produk VARCHAR(20),
                Harga_Produk DECIMAL(10, 2)
            )""")

# cur.execute("""ALTER TABLE Struk
# ADD CONSTRAINT FK_StrukTransaksi FOREIGN KEY (No_Transaksi) REFERENCES Transaksi(No_Transaksi);
# """)

# cur.execute("""ALTER TABLE Transaksi
# ADD COLUMN NIK CHAR(4),
# ADD CONSTRAINT FK_TransaksiPegawai FOREIGN KEY (NIK) REFERENCES Pegawai(NIK);
# """)

# cur.execute("""ALTER TABLE Transaksi
# ADD COLUMN Kode_Produk INT,
# ADD CONSTRAINT FK_TransaksiProduk FOREIGN KEY (Kode_Produk) REFERENCES Produk(Kode_Produk);
# """)

produk = {
    "snack": {
        "P001": ("Chitato", 10000),
        "P002": ("Lays", 15000),
        "P003": ("Potabee", 12000),
    },
    "minuman": {
        "M001": ("Aqua", 3000),
        "M002": ("Jus", 7000),
        "M003": ("Susu", 5000),
    },
    "makanan": {
        "F001": ("Ayam Goreng", 8000),
        "F002": ("Nasi Goreng", 12000),
        "F003": ("Mie Ayam", 15000),
    },
}

while True:
    print("\n========== Menu Sistem Penjualan ==========")
    print("1. Tampilkan Data Produk")
    print("2. Masukkan Data Pegawai")
    print("3. Tambahkan Produk")
    print("4. Masukkan Data Transaksi")
    print("5. Tampilkan Struk")
    print("6. Ubah Data")
    print("7. Hapus Data")
    print("0. Keluar")
    menu = input("Pilih menu: ")

    if menu == '1':
        # Menampilkan Data Produk
        print("\n========== Data Produk ==========")
        for kategori, items in produk.items():
            print(f"\nKategori: {kategori.capitalize()}")
            table = [[Kode, nama, f"Rp {harga:,}"] for Kode, (nama, harga) in items.items()]
            print(tabulate(table, headers=["Kode Produk", "Nama Produk", "Harga"], tablefmt="grid"))

    elif menu == '2':
        # Input Data Pegawai
        print("\n========== Input Data Pegawai ==========")
        NIK = input("Masukkan NIK Pegawai: ")
        Nama_Pegawai = input("Masukkan Nama Pegawai: ")
        Alamat = input("Masukkan Alamat Pegawai: ")
        
        # Cek apakah NIK sudah ada
        cur.execute("SELECT * FROM Pegawai WHERE NIK = %s", [NIK])
        if cur.fetchone():
            print("NIK sudah ada. Tidak menambahkan data Pegawai.")
        else:
            try:
                cur.execute("""INSERT INTO Pegawai (NIK, Nama, Alamat) VALUES (%s, %s, %s)""",
                            [NIK, Nama_Pegawai, Alamat])
                conn.commit()
                print("Data Pegawai berhasil ditambahkan!")
            except mysql.connector.Error as err:
                print(f"Error: {err}")

    elif menu == '3':
        # Tambahkan Produk
        print("\n========== Tambahkan Produk ==========")

        # Memilih Jenis Produk
        print("Pilih Jenis Produk:")
        print("1. Snack")
        print("2. Minuman")
        print("3. Makanan")
        pilihan_jenis = input("Pilih jenis produk (1/2/3): ")

        if pilihan_jenis == '1':
            jenis_produk = "snack"
        elif pilihan_jenis == '2':
            jenis_produk = "minuman"
        elif pilihan_jenis == '3':
            jenis_produk = "makanan"
        else:
            print("Pilihan tidak valid!")
            break

        # Menampilkan Produk Berdasarkan Pilihan Jenis
        print(f"\nPilih Produk {jenis_produk.capitalize()}:")
        for kode, (nama, harga) in produk[jenis_produk].items():
            print(f"{kode}: {nama} - Rp{harga}")

        # Memilih Produk
        pilihan_produk = input(f"Masukkan kode produk yang dipilih: ")
        
        # Mengecek apakah produk yang dipilih valid
        if pilihan_produk in produk[jenis_produk]:
            nama_produk, harga_produk = produk[jenis_produk][pilihan_produk]
            print(f"\nProduk: {nama_produk}\nHarga: Rp{harga_produk}")
        else:
            print("Produk tidak valid!")
            break

        Nama_Produk = nama_produk  
        Harga_Produk = harga_produk  

        try:
            cur.execute("""INSERT INTO Produk (Kode_Produk, Nama_Produk, Jenis_Produk, Harga_Produk) 
                            VALUES (%s, %s, %s, %s)""", 
                            [pilihan_produk, Nama_Produk, jenis_produk, Harga_Produk])
            conn.commit()
            print("Produk berhasil ditambahkan!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    elif menu == '4':
        # Masukkan Data Transaksi
        print("\n========== Input Data Transaksi ==========")
        No_Transaksi = input("Masukkan No Transaksi: ")
        Detail_Transaksi = input("Masukkan Detail Transaksi: ")
        NIK = input("Masukkan NIK Pegawai: ")
        Kode_Produk = input("Masukkan Kode Produk: ")
        Jumlah_Produk = int(input("Masukkan Jumlah Produk: "))

        cur.execute("SELECT Nama_Produk, Harga_Produk FROM Produk WHERE Kode_Produk = %s", [Kode_Produk])
        produk = cur.fetchone()

        if produk:
            Nama_Produk = produk[0]
            Harga_Produk = produk[1]
            Total_Harga = Harga_Produk * Jumlah_Produk
            
            # Menyimpan Data Transaksi
            try:
                cur.execute("""INSERT INTO Transaksi (No_Transaksi, Detail_Transaksi, NIK, Kode_Produk) 
                                VALUES (%s, %s, %s, %s)""", 
                                [No_Transaksi, Detail_Transaksi, NIK, Kode_Produk])
                conn.commit()
                
                # Menyimpan Data Struk
                cur.execute("""INSERT INTO Struk (No_Transaksi, Nama_Pegawai, Nama_Produk, Jumlah_Produk, Total_Harga) 
                                VALUES (%s, %s, %s, %s, %s)""", 
                                [No_Transaksi, NIK, Nama_Produk, Jumlah_Produk, Total_Harga])
                conn.commit()

                print("Transaksi berhasil ditambahkan!")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
        else:
            print("Produk tidak ditemukan!")

    elif menu == '5':
        # Tampilkan Struk
        print("\n========== Tampilkan Struk ==========")
        No_Transaksi = input("Masukkan No Transaksi untuk menampilkan struk: ")

        cur.execute("""
            SELECT s.No_Transaksi, p.Nama AS Nama_Pegawai, s.Nama_Produk, s.Jumlah_Produk, s.Total_Harga
            FROM Struk s
            JOIN Pegawai p ON p.Nama = s.Nama_Pegawai  # Menghubungkan Nama di tabel Pegawai dan Nama_Pegawai di Struk
            WHERE s.No_Transaksi = %s
        """, [No_Transaksi])

        struk = cur.fetchall()  

        if struk:
            print("\n========== Struk Transaksi ==========")
            print(tabulate(struk, headers=["No Transaksi", "Nama Pegawai", "Nama Produk", "Jumlah Produk", "Total Harga"], tablefmt="grid"))
        else:
            print("Struk tidak ditemukan!")

    elif menu == '6':
        # Ubah Data
        print("\n========== Ubah Data ==========")
        print("1. Ubah Pegawai")
        print("2. Ubah Produk")
        print("3. Ubah Transaksi")
        pilihan_ubah = input("Pilih yang ingin diubah: ")
        if pilihan_ubah == '1':
            NIK = input("Masukkan NIK Pegawai yang ingin diubah: ")
            Nama_Baru = input("Masukkan Nama Baru: ")
            Alamat_Baru = input("Masukkan Alamat Baru: ")
            # Update data pegawai di database
            cur.execute("""UPDATE Pegawai SET Nama = %s, Alamat = %s WHERE NIK = %s""",
                        [Nama_Baru, Alamat_Baru, NIK])
            conn.commit()
            print(f"Data Pegawai dengan NIK {NIK} berhasil diubah.")
        elif pilihan_ubah == '2':
            Kode_Produk = input("Masukkan Kode Produk yang ingin diubah: ")
            Nama_Produk_Baru = input("Masukkan Nama Produk Baru: ")
            # Update data produk di database
            cur.execute("""UPDATE Produk SET Nama_Produk = %s WHERE Kode_Produk = %s""",
                        [Nama_Produk_Baru, Kode_Produk])
            conn.commit()
            print(f"Data Produk dengan Kode {Kode_Produk} berhasil diubah.")
        elif pilihan_ubah == '3':
            No_Transaksi = input("Masukkan No Transaksi yang ingin diubah: ")
            Detail_Transaksi_Baru = input("Masukkan Detail Transaksi Baru: ")
            # Update data transaksi di database
            cur.execute("""UPDATE Transaksi SET Detail_Transaksi = %s WHERE No_Transaksi = %s""",
                        [Detail_Transaksi_Baru, No_Transaksi])
            conn.commit()
            print(f"Data Transaksi dengan No {No_Transaksi} berhasil diubah.")
        else:
            print("Pilihan tidak valid.")

    elif menu == '7':
        # Hapus Data
        print("\n========== Hapus Data ==========")
        print("1. Hapus Pegawai")
        print("2. Hapus Produk")
        print("3. Hapus Transaksi")
        pilihan_hapus = input("Pilih yang ingin dihapus: ")
        if pilihan_hapus == '1':
            NIK = input("Masukkan NIK Pegawai yang ingin dihapus: ")
            # Hapus data pegawai di database
            cur.execute("""DELETE FROM Pegawai WHERE NIK = %s""", [NIK])
            conn.commit()
            print(f"Data Pegawai dengan NIK {NIK} berhasil dihapus.")
        elif pilihan_hapus == '2':
            Kode_Produk = input("Masukkan Kode Produk yang ingin dihapus: ")
            # Hapus data produk di database
            cur.execute("""DELETE FROM Produk WHERE Kode_Produk = %s""", [Kode_Produk])
            conn.commit()
            print(f"Data Produk dengan Kode {Kode_Produk} berhasil dihapus.")
        elif pilihan_hapus == '3':
            No_Transaksi = input("Masukkan No Transaksi yang ingin dihapus: ")
            # Hapus data transaksi di database
            cur.execute("""DELETE FROM Transaksi WHERE No_Transaksi = %s""", [No_Transaksi])
            conn.commit()
            print(f"Data Transaksi dengan No {No_Transaksi} berhasil dihapus.")
        else:
            print("Pilihan tidak valid.")

    elif menu == '0':
        print("Keluar dari program.")
        break

    else:
        print("Menu tidak valid. Silakan coba lagi.")
