class Order:
    next_id = 0  

    def __init__(self, name, details):
        self._ID = Order.next_id
        Order.next_id += 1
        self.name = name
        self.details = details

    def set_order(self):
        print(f"Pesanan dibuat untuk {self.name} dengan detail: {self.details}")
    
    def update_details(self, new_details):
        self.details = new_details
        print(f"Detail pesanan diperbarui menjadi: {self.details}")
        
    def get_id(self):
        return self._ID


class Delivery:
    next_id = 0  

    def __init__(self, name, information, date, address):
        self._id = Delivery.next_id
        Delivery.next_id += 1
        self.name = name
        self.information = information
        self.date = date
        self.address = address

    def process_delivery(self):
        print(f"Memproses pengiriman untuk {self.name} ke alamat: {self.address} pada tanggal {self.date}")

    def update_address(self, new_address):
        self.address = new_address
        print(f"Alamat pengiriman diperbarui menjadi: {self.address}")
    
    def get_id(self):
        return self._id


def menu():
    orders = []
    deliveries = []

    while True:
        print("\n================= Menu Pengiriman =================")
        print("1. Buat Pesanan Baru")
        print("2. Perbarui Detail Pesanan")
        print("3. Lihat Pesanan")
        print("4. Buat Pengiriman Baru")
        print("5. Perbarui Alamat Pengiriman")
        print("6. Proses Pengiriman")
        print("7. Keluar")
        
        pilihan = input("Pilih opsi: ")
        
        if pilihan == '1':
            nama = input("Masukkan nama pesanan: ")
            detail = input("Masukkan detail pesanan: ")
            pesanan = Order(name=nama, details=detail)
            pesanan.set_order()
            orders.append(pesanan)
            
        elif pilihan == '2':
            if not orders:
                print("Tidak ada pesanan yang tersedia untuk diperbarui.")
            else:
                try:
                    order_id = int(input("Masukkan ID pesanan untuk diperbarui: "))
                    if 0 <= order_id < len(orders):
                        detail_baru = input("Masukkan detail pesanan baru: ")
                        orders[order_id].update_details(detail_baru)
                    else:
                        print("ID pesanan tidak valid.")
                except ValueError:
                    print("ID harus berupa angka.")
                
        elif pilihan == '3':
            if not orders:
                print("Tidak ada pesanan yang tersedia.")
            else:
                for order in orders:
                    print(f"ID Pesanan: {order.get_id()}, Nama: {order.name}, Detail: {order.details}")

        elif pilihan == '4':
            nama = input("Masukkan nama pengiriman: ")
            informasi = input("Masukkan informasi pengiriman: ")
            tanggal = input("Masukkan tanggal pengiriman: ")
            alamat = input("Masukkan alamat pengiriman: ")
            pengiriman = Delivery(name=nama, information=informasi, date=tanggal, address=alamat)
            pengiriman.process_delivery()
            deliveries.append(pengiriman)
            
        elif pilihan == '5':
            if not deliveries:
                print("Tidak ada pengiriman yang tersedia untuk diperbarui.")
            else:
                try:
                    delivery_id = int(input("Masukkan ID pengiriman untuk memperbarui alamat: "))
                    if 0 <= delivery_id < len(deliveries):
                        alamat_baru = input("Masukkan alamat pengiriman baru: ")
                        deliveries[delivery_id].update_address(alamat_baru)
                    else:
                        print("ID pengiriman tidak valid.")
                except ValueError:
                    print("ID harus berupa angka.")
                    
        elif pilihan == '6':
            if not deliveries:
                print("Tidak ada pengiriman yang tersedia untuk diproses.")
            else:
                for delivery in deliveries:
                    print(f"ID Pengiriman: {delivery.get_id()}, Nama: {delivery.name}, Alamat: {delivery.address}, Tanggal: {delivery.date}")
                    
        elif pilihan == '7':
            print("Keluar dari program.")
            break
        
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()
