import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import csv

class AppMusic:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pengelolaan Koleksi Musik")
        self.root.geometry("600x750") #Lebar dan Tinggi ukuran awal jendela
        self.root.config(bg="#DDA0DD")

        # Data musik
        self.music_data = []

        # Memanggil metode untuk membuat widget
        self.widget_create()

    def widget_create(self):
        # Title Label
        title_label = tk.Label(self.root, text="Aplikasi Pengelolaan Koleksi Musik",
                               font=("Times New Roman", 24, 'bold'), fg="#333", bg="#DDA0DD")
        title_label.pack(pady=40)

        # Frame Input
        frame_input = tk.Frame(self.root, bg="#DDA0DD")
        frame_input.pack(pady=10)

        # Judul Musik
        judul_label = tk.Label(frame_input, text="Judul Musik :", bg="#DDA0DD", font=("Arial", 10))
        judul_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_title = tk.Entry(frame_input, width=25)
        self.entry_title.grid(row=0, column=1, padx=10, pady=5)
        self.entry_title.bind("<Return>", lambda event: self.entry_artist.focus())

        # Nama Artis
        artis_label = tk.Label(frame_input, text="Nama Artis :", bg="#DDA0DD", font=("Arial", 10))
        artis_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_artist = tk.Entry(frame_input, width=25)
        self.entry_artist.grid(row=1, column=1, padx=10, pady=5)
        self.entry_artist.bind("<Return>", lambda event: self.entry_album.focus())

        # Album
        album_label = tk.Label(frame_input, text="Album :", bg="#DDA0DD", font=("Arial", 10))
        album_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.entry_album = tk.Entry(frame_input, width=25)
        self.entry_album.grid(row=0, column=3, padx=10, pady=5)
        self.entry_album.bind("<Return>", lambda event: self.combo_genre.focus())

        # Genre
        genre_label = tk.Label(frame_input, text="Genre :", bg="#DDA0DD", font=("Arial", 10))
        genre_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        self.genre_var = tk.StringVar()
        self.combo_genre = ttk.Combobox(frame_input, textvariable=self.genre_var, width=23)
        self.combo_genre['values'] = ["Klasik", "Jazz", "Pop", "R&B", "Hip-hop"]
        self.combo_genre.set("Pilih Genre")
        self.combo_genre.grid(row=1, column=3, padx=10, pady=5)

        # Tombol Tambah Musik
        add_button = tk.Button(self.root, text="Tambah", font=("Arial", 11, 'bold'), bg="#9370DB", fg="white", command=self.add_music)
        add_button.pack(pady=10)

        # Filter Genre
        filter_frame = tk.Frame(self.root, bg="#DDA0DD")
        filter_frame.pack(pady=10)

        filter_label = tk.Label(filter_frame, text="Pilih Genre:", bg="#DDA0DD", font=("Arial", 12))
        filter_label.pack(side=tk.LEFT, padx=5)

        self.filter_genre_var = tk.StringVar()
        self.filter_combobox = ttk.Combobox(filter_frame, textvariable=self.filter_genre_var, width=23)
        self.filter_combobox['values'] = ["Semua"] + ["Klasik", "Jazz", "Pop", "R&B", "Hip-hop"]
        self.filter_combobox.set("Semua")
        self.filter_combobox.pack(side=tk.LEFT, padx=5)
        self.filter_combobox.bind("<<ComboboxSelected>>", self.update_table)

        # Frame untuk Tabel
        frame_table = tk.Frame(self.root, bg="#F0F8FF")
        frame_table.pack(pady=10)

        # Table musik
        music_table_label = tk.Label(frame_table, text="Koleksi Musikmu", bg="#F0F8FF", font=("Arial", 14, "bold"))
        music_table_label.pack(pady=10)

        self.music_table = ttk.Treeview(frame_table, columns=("ID", "Judul", "Artis", "Album", "Genre"), show="headings")
        self.music_table.heading("ID", text="ID")
        self.music_table.heading("Judul", text="Judul")
        self.music_table.heading("Artis", text="Artis")
        self.music_table.heading("Album", text="Album")
        self.music_table.heading("Genre", text="Genre")
        self.music_table.column("ID", width=50, anchor="center")
        self.music_table.column("Judul", width=150)
        self.music_table.column("Artis", width=150)
        self.music_table.column("Album", width=150)
        self.music_table.column("Genre", width=100)
        self.music_table.pack(pady=10)

        button_frame = tk.Frame(self.root, bg="#DDA0DD")
        button_frame.pack(pady=5)

        # Tombol Hapus Pilihan
        delete_button = tk.Button(button_frame, text="Hapus Pilihan", font=("Arial", 11, 'bold'), bg="#9370DB", fg="white", command=self.delete_selected)
        delete_button.pack(side=tk.LEFT, padx=5)

        # Tombol Hapus Semua
        delete_all_button = tk.Button(button_frame, text="Hapus Semua", font=("Arial", 11, 'bold'), bg="#9370DB", fg="white", command=self.delete_all)
        delete_all_button.pack(side=tk.LEFT, padx=5)

        # Tombol Simpan Data
        save_button = tk.Button(self.root, text="Simpan", font=("Arial", 11, 'bold'), bg="#9370DB", fg="white", command=self.save_to_file)
        save_button.pack(pady=10)

    def add_music(self):
        title = self.entry_title.get()
        artist = self.entry_artist.get()
        album = self.entry_album.get()
        genre = self.genre_var.get()

        # Validasi input
        if not title or not artist or not album or genre == "Pilih Genre":
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi!") # Jika ada kolom yang kosong, muncul pesan peringatan
            return

        # Menambahkan data ke dalam list musik
        music_id = len(self.music_data) + 1
        self.music_data.append({"ID": music_id, "Judul": title, "Artis": artist, "Album": album, "Genre": genre})
        self.update_table()
        self.reset_input()

    def update_table(self, event=None):
        # Hapus semua data di tabel
        for item in self.music_table.get_children():
            self.music_table.delete(item)

        # Dapatkan genre yang dipilih
        selected_genre = self.filter_genre_var.get()

        # Filter dan tambahkan data ke tabel
        for music in self.music_data:
            if selected_genre == "Semua" or music["Genre"] == selected_genre:
                self.music_table.insert("", "end",
                                        values=(music["ID"], music["Judul"], music["Artis"], music["Album"], music["Genre"]))

    def delete_selected(self):
        selected_item = self.music_table.selection()
        if not selected_item:
            messagebox.showwarning("Error", "Silakan pilih baris untuk dihapus!")
            return
        confirm = messagebox.askquestion("Konfirmasi", "Yakin ingin menghapus lagu yang dipilih?")
        if confirm == "yes":
            for item in selected_item:
                values = self.music_table.item(item, "values")
                music_id = int(values[0])
                self.music_table.delete(item)
                self.music_data = [music for music in self.music_data if music["ID"] != music_id]

    def delete_all(self):
        confirm = messagebox.askquestion("Konfirmasi", "Yakin ingin menghapus semua lagu?")
        if confirm == "yes":
            self.music_data.clear()
            self.update_table()

    def save_to_file(self):
        # Menyimpan data koleksi musik ke dalam file CSV
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Judul", "Artis", "Album", "Genre"])
                    for music in self.music_data:
                        writer.writerow([music["ID"], music["Judul"], music["Artis"], music["Album"], music["Genre"]])
                messagebox.showinfo("Berhasil", f"Data berhasil disimpan ke file '{file_path}'")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menyimpan data: {e}")

    def reset_input(self):
        # Mengosongkan atau mereset semua input form
        self.entry_title.delete(0, tk.END)
        self.entry_artist.delete(0, tk.END)
        self.entry_album.delete(0, tk.END)
        self.combo_genre.set("Pilih Genre")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppMusic(root)
    root.mainloop()
