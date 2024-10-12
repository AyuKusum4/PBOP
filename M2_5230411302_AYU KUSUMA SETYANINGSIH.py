def cek_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def cek_ganjil(n):
    return n % 2 != 0

def cek_genap(n):
    return n % 2 == 0

def menu():
    while True:
        print("\nMenu:")
        print("1. Tampilkan Bilangan Prima")
        print("2. Tampilkan Bilangan Ganjil")
        print("3. Tampilkan Bilangan Genap")
        print("0. Keluar")
        
        pilihan = input("Masukkan pilihan menu): ")
        
        if pilihan == "1":
            print("============Cek Bilangan Prima============")
            bilangan_awal = int(input("Masukkan bilangan awal: "))
            bilangan_akhir = int(input("Masukkan bilangan akhir: "))
            print(f"Bilangan prima dari {bilangan_awal} hingga {bilangan_akhir}:")
            for i in range(bilangan_awal, bilangan_akhir + 1):
                if cek_prima(i):
                    print(i, end=" ")
            print() 
        
        elif pilihan == "2":
            print("============Cek Bilangan Ganjil============")
            bilangan_awal = int(input("Masukkan bilangan awal: "))
            bilangan_akhir = int(input("Masukkan bilangan akhir: "))
            print(f"Bilangan ganjil dari {bilangan_awal} hingga {bilangan_akhir}:")
            for i in range(bilangan_awal, bilangan_akhir + 1):
                if cek_ganjil(i):
                    print(i, end=" ")
            print()  
        
        elif pilihan == "3":
            print("============Cek Bilangan Genap============")
            bilangan_awal = int(input("Masukkan bilangan awal: "))
            bilangan_akhir = int(input("Masukkan bilangan akhir: "))
            print(f"Bilangan genap dari {bilangan_awal} hingga {bilangan_akhir}:")
            for i in range(bilangan_awal, bilangan_akhir + 1):
                if cek_genap(i):
                    print(i, end=" ")
            print()  
        
        elif pilihan == "0":
            print("Keluar dari sistem.")
            break
        
        else:
            print("Pilihan Tidak Ada Di Menu")
        
        input("Enter Untuk Melanjutkan...")

if __name__ == "__main__":
    menu()

