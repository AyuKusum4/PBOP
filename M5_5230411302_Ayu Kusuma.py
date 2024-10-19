class Music:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

    def display(self):
        print(f"{self.judul.ljust(30)} {self.penyanyi.ljust(30)}")

def display_music_by_genre(music_list, genre):
    filtered_songs = [music for music in music_list if music.genre == genre]
    
    if filtered_songs:
        print(f"\n=============== {genre} ===============")
        for song in filtered_songs:
            song.display()
    else:
        print(f"\nTidak ada lagu di genre {genre}.")

def search_by_singer(music_list, penyanyi):
    found_music = [music for music in music_list if music.penyanyi.lower() == penyanyi.lower()]
    if found_music:
        print(f"Musik dari penyanyi '{penyanyi}':")
        for music in found_music:
            music.display()
    else:
        print(f"Tidak ada lagu yang ditemukan untuk penyanyi {penyanyi}.")

def display_all_music(music_list):
    sorted_list = sorted(music_list, key=lambda music: music.judul)
    print("Daftar Musik (Sorted A-Z):")
    for music in sorted_list:
        music.display()

music_list = [
    Music("Gata Only", "Cris MJ dan FloyyMenor", "S-Song"),
    Music("Danza Kuduro", "Don Omar", "S-Song"),
    Music("Love Nwantiti", "Splice Records", "S-Song"),
    Music("Waka Waka", "Shakira", "S-Song"),
    Music("Gasolina", "Daddy Yanke", "S-Song"),
    Music("Magnetic", "illit", "K-Song"),
    Music("Sticky", "Kiss Of Life", "K-Song"),
    Music("Woke Up", "XG", "K-Song"),
    Music("Perfect Night", "Le Sserafim", "K-Song"),
    Music("Touch", "Katseye", "K-Song"),
    Music("Shinunoga E-Wa", "Fujii Kaze", "J-Song"),
    Music("Lemon", "Kenshi Yonezu", "J-Song"),
    Music("Suki Dakara", "Yuika", "J-Song"),
    Music("Kokoronashi", "Gumi", "J-Song"),
    Music("memories", "One Piece", "J-Song")
]

while True:
    print("\n============= Playlist Music =============")
    print("1. Display Spanish Songs")
    print("2. Display Korean Songs")
    print("3. Display Japanese Songs")
    print("4. Display All")
    print("5. Search Music")
    print("0. Keluar")
    pilihan = input("Masukkan Pilihan Menu: ")

    if pilihan == "1":
        display_music_by_genre(music_list, "S-Song")

    elif pilihan == "2":
        display_music_by_genre(music_list, "K-Song")

    elif pilihan == "3":
        display_music_by_genre(music_list, "J-Song")

    elif pilihan == "4":
        display_all_music(music_list)
    
    elif pilihan == "5":
        penyanyi = input("Masukkan Penyanyi yang Ingin Dicari: ")
        search_by_singer(music_list, penyanyi)

    elif pilihan == "0":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")