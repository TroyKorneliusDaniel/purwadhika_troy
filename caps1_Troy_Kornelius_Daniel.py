from tabulate import tabulate
import sys

games = [ 
    [1, "BLACK MYTH WUKONG", "SOULS", 800000, 10],
    [2, "COUNTER STRIKE 2", "FPS", 250000, 5],
    [3, "MINECRAFT", "SANDBOX", 300000, 20]
    ] # Data games disimpan dalam bentuk list dari list
game_id_counter = len(games) + 1 # Untuk memberi ID unik ke setiap game

# Fungsi untuk cek judul game duplikat
def cek_duplikasi(title):
    for game in games:
        if game[1] == title:
            return True  # Game ditemukan duplikat dan menghentikan loop
    return False # Game tidak duplikan dan melanjutkan loop

# Fungsi untuk menambah game (Create)
def create_game():
    global game_id_counter
    while True:
        while True:
            title = input("Masukkan judul game (Tidak Boleh Singkatan): ").upper()
            if title.strip() == "":  # Cek apakah input kosong setelah menghapus spasi
                print("Judul game tidak boleh kosong/invalid!")
            elif cek_duplikasi(title):
                print(f"Game dengan judul '{title}' sudah ada dalam daftar game.")
                show_menu_create()  # Kembali ke sub menu create jika duplikat
            else:
                break  # Keluar dari loop jika input valid

        while True:
            genre = input("Masukkan genre game: ").upper()
            if genre.strip() == "":  # Cek apakah input genre kosong setelah menghapus spasi
                print("Genre game tidak valid!")
            elif genre.isalpha():
                genre = str(genre)
                break
            else:
                print("Input tidak valid")

        while True:
            price = input("Masukkan harga game: ")
            if price.isdigit():
                price = int(price)
                break  # Exit the loop if input is a valid number
            else:
                print("Masukkan harga yang valid!")

        while True:
            stock = input("Masukkan jumlah stok: ")
            if stock.isdigit():
                stock = int(stock)
                break  # Exit the loop if input is a valid number
            else:
                print("Masukkan jumlah stok yang valid!")

        new_id = game_id_counter  # Use the generated unique game ID
        # Confirm with user and display the game details in a table
        while True:
            confirmation_table = [
                ["ID", "Title", "Genre", "Price (Rp)", "Stock"],
                [new_id, title, genre, price, stock]
            ]
            print("\nKonfirmasi penambahan game baru:")
            print(tabulate(confirmation_table, headers="firstrow", tablefmt="fancy_grid"))
            
            validasi_create_game = input(
                f'Apakah Anda yakin ingin menambahkan game dengan ID: {new_id}, Title: {title}, Genre: {genre}, Price: Rp.{price}, Stock: {stock}? (Y/N) :\n'
            ).upper()
            
            if validasi_create_game == "Y":
                print(f"Game dengan judul {title} berhasil ditambah.")
                new_game = [new_id, title, genre, price, stock]
                games.append(new_game)
                game_id_counter += 1  # Update game ID for the next game
                show_menu_create()  # kembali ke sub menu create
            elif validasi_create_game == "N":
                print("Tidak Jadi menambah Game.")
                show_menu_create()  # kembali ke sub menu create
            else:
                print("Masukkan Pilihan Valid (Y/N)")

# Fungsi untuk Sub Menu Create
def show_menu_create():
    while True:
        print("\n=== Menu Tambah Game ===")
        print("1. Tambah Game")
        print("2. Kembali Ke Menu Utama")
        
        choice_create = input("Pilih operasi (1/2): ")
        
        if choice_create == "1":
            create_game()
        elif choice_create == "2":
            show_menu()
            break  # Keluar dari loop untuk kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk memunculkan seluruh data game (Read)
def read_games():
    if games:
        headers = ["ID", "Title", "Genre", "Price (Rp)", "Stock"]
        print(tabulate(games, headers=headers, tablefmt="fancy_grid"))
    else:
        print("Tidak ada game yang tersedia.")

    show_menu_read()

# Fungsi untuk memunculkan seluruh data game berdasarkan index
def read_spesifik():
    try:
        game_id = int(input("Masukkan game ID yang ingin dicari: "))
        found = False
        for game in games:
            if game[0] == game_id:
                game_id, title, genre, price, stock = game
                print(f"ID: {game_id}, Title: {title}, Genre: {genre}, Price: Rp.{price}, Stock: {stock}")
                found = True
                headers = ["ID", "Title", "Genre", "Price (Rp)", "Stock"]
                print(tabulate([game], headers=headers, tablefmt="fancy_grid"))
                break
        if not found:
            print(f"Game dengan ID {game_id} tidak ditemukan.")
    except ValueError:
        print("Input harus berupa angka. Silakan masukkan game ID yang valid.")
    show_menu_read()

#Fungsi untuk memunculkan genre game yang ada di list
def show_genres():
    genres = set()  # Menggunakan set untuk menghindari genre yang duplikat
    for game in games:
        genres.add(game[2])  # Menambahkan genre game ke dalam set
    
    if not games:  # Memeriksa apakah list games kosong
        print("Tidak ada data game yang tersedia.")
        show_menu_read()  # Kembali ke menu delete jika tidak ada game
    elif genres:
        print("\nGenre yang tersedia:")
        genre_list = [[genre] for genre in genres]  
        headers = ["Genre"]
        print(tabulate(genre_list, headers=headers, tablefmt="fancy_grid"))
    else:
        print("Tidak ada genre yang tersedia.")

# Fungsi untuk memnuculkan seluruh data game berdasarkan genre
def read_by_genre():
    show_genres()
    genre_input = input("Masukkan genre yang ingin dicari: ").upper()
    found_games = []  #list kosong untuk menambahkan data game berdasarkan input

    #Loop untuk mencari data game yang memiliki genre sesuai input
    for game in games:
        if game[2] == genre_input:  # cek genre pada game apakah sesuai dengan input
            found_games.append(game)  # menambahkan game ke found_games
    
    if found_games:
        print(f"\nGame dengan genre '{genre_input}' ditemukan:")
        headers = ["ID", "Title", "Genre", "Price (Rp)", "Stock"]
        print(tabulate(found_games, headers=headers, tablefmt="fancy_grid"))
    else:
        print(f"Tidak ada game dengan genre '{genre_input}' yang ditemukan.")
    
    show_menu_read()

# Fungsi untuk mengurutkan data game berdasarkan harga terendah
def bubble_sort(games, sort_by, order):
    if not games:  # Memeriksa apakah list games kosong
        print("Tidak ada data game yang tersedia.")
        return

    n = len(games)
    sort_index = {"price": 3, "name": 1, "genre": 2, "stock":4}  # Indeks kolom berdasarkan kategori
    index = sort_index.get(sort_by, 3)  # Default sorting by price jika pilihan tidak valid

    for i in range(n):
        for j in range(0, n - i - 1):
            if (order == "asc" and games[j][index] > games[j + 1][index]) or (order == "desc" and games[j][index] < games[j + 1][index]):
                games[j], games[j + 1] = games[j + 1], games[j]

    headers = ["ID", "Title", "Genre", "Price (Rp)", "Stock"]
    print(tabulate(games, headers=headers, tablefmt="fancy_grid"))

def show_sorting_menu():
    while True:
        print("\n=== Menu Sorting ===")
        print("1. Sorting Berdasarkan Harga")
        print("2. Sorting Berdasarkan Nama")
        print("3. Sorting Berdasarkan Genre")
        print("4. Sorting berdasarkan stock")
        print("5. Kembali ke Menu Utama")
        sort_choice = input("Pilih metode sorting (1/2/3/4/5): ")
        
        if sort_choice == "1":
            sort_by = "price"
        elif sort_choice == "2":
            sort_by = "name"
        elif sort_choice == "3":
            sort_by = "genre"
        elif sort_choice =="4":
            sort_by = "stock"
        elif sort_choice == "5":
            return  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue  # Mengulang menu jika pilihan tidak valid

        # Meminta input untuk urutan pengurutan (ascending/descending)
        while True:
            print("\nPilih urutan sorting:")
            print("1. Ascending")
            print("2. Descending")
            order_choice = input("Masukkan pilihan (1/2): ")

            if order_choice == "1":
                order = "asc"
                break  # Keluar dari loop jika input valid
            elif order_choice == "2":
                order = "desc"
                break  # Keluar dari loop jika input valid
            else:
                print("Pilihan tidak valid. Silakan masukkan 1 untuk Ascending atau 2 untuk Descending.")

        # Melakukan pengurutan setelah pilihan valid diterima
        bubble_sort(games, sort_by, order)
        break  # Keluar dari loop setelah sorting selesai

# Fungsi untuk Sub Menu Read
def show_menu_read():
    while True:
        print("\n=== Menu Lihat Game ===")
        print("1. Lihat Semua Game")
        print("2. Lihat Game Spesifik")
        print("3. Cari Berdasarkan Genre")
        print("4. Sorting")
        print("5. Kembali Ke Menu Utama")
        choice_read = input("Pilih operasi (1/2/3/4/5): ")
        
        if choice_read == "1":
            read_games()
        elif choice_read == "2":
            read_spesifik()
        elif choice_read == "3":
             read_by_genre()
        elif choice_read == "4":
             show_sorting_menu()
        elif choice_read == "5":
             show_menu()
             break  # Keluar dari loop untuk kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    show_menu_read()

# Fungsi untuk Sub Menu Update
def show_menu_update():
    while True:
        print("\n=== Menu Update Data Game ===")
        print("1. Update Data Game")
        print("2. Kembali Ke Menu Utama")
        choice_create = input("Pilih operasi (1/2): ")
        
        if choice_create == "1":
            update_game()
        elif choice_create == "2":
            show_menu()
            break  # Keluar dari loop untuk kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk mengubah judul game
def update_title(game):
    while True:
        new_title = input("Masukkan judul baru: ").upper()
        if new_title.strip() == "":  # Validasi jika input kosong
            print("Judul tidak boleh kosong.")
            continue  # Memaksa untuk memasukkan input valid
        if cek_duplikasi(new_title):  # Validasi jika judul sudah ada
            print(f"Game dengan judul '{new_title}' sudah ada dalam daftar game.")
            show_menu_update() # Memaksa untuk memasukkan input valid
        else:
            while True:
                confirmation = input(f"Apakah Anda yakin ingin mengubah judul menjadi '{new_title}'? (Y/N)").upper()
                if confirmation == "Y":
                    game[1] = new_title
                    print(f"Title berhasil diperbarui menjadi: {new_title}")
                    show_menu_update() # Keluar dari loop setelah pembaruan berhasil
                elif confirmation == "N":
                    print("Perubahan judul dibatalkan.")
                    show_menu_update()  # Keluar dari loop tanpa mengubah data
                else:
                    print("Masukkan pilihan yang valid (Y/N).")

# Fungsi untuk mengubah genre game
def update_genre(game):
    while True:
        new_genre = input("Masukkan genre baru : ").upper()
        if new_genre.strip() == "":  # Validasi jika input kosong
            print("Genre tidak boleh kosong.")
            continue # Memaksa untuk memasukkan input valid
        while True:
            confirmation = input(f"Apakah Anda yakin ingin mengubah genre menjadi '{new_genre}'? (Y/N)").upper()
            if confirmation == "Y":
                game[2] = new_genre
                print(f"Genre berhasil diperbarui menjadi: {new_genre}")
                show_menu_update()  # Keluar dari loop setelah pembaruan berhasil
            elif confirmation == "N":
                print("Perubahan genre dibatalkan.")
                show_menu_update()  # Keluar dari loop tanpa mengubah data
            else:
                print("Masukkan pilihan yang valid (Y/N).")

# Fungsi untuk mengubah harga game
def update_price(game):
    while True:
        new_price = input("Masukkan harga baru : ")
        if new_price.strip() == "":  # Validasi jika input kosong
            print("Harga tidak boleh kosong.")
            continue  # Memaksa untuk memasukkan input valid
        elif new_price.isdigit():  # Validasi jika input adalah angka
            while True:
                confirmation = input(f"Apakah Anda yakin ingin mengubah harga menjadi Rp.{new_price}? (Y/N)").upper()
                if confirmation == "Y":
                    game[3] = int(new_price)
                    print(f"Harga berhasil diperbarui menjadi: Rp.{new_price}")
                    show_menu_update() # Keluar dari loop setelah pembaruan berhasil
                elif confirmation == "N":
                    print("Perubahan harga dibatalkan.")
                    show_menu_update() # Keluar dari loop tanpa mengubah data
                else:
                    print("Masukkan pilihan yang valid (Y/N).")
        else:
            print("Harga tidak valid. Masukkan angka yang benar untuk harga.")

# Fungsi untuk mengubah stok game
def update_stock(game):
    while True:
        new_stock = input("Masukkan stok baru :")
        if new_stock.strip() == "":  # Validasi jika input kosong
            print("Stok tidak boleh kosong.")
            continue # Memaksa untuk memasukkan input valid
        elif new_stock.isdigit():  # Validasi jika input adalah angka
            while True:
                confirmation = input(f"Apakah Anda yakin ingin mengubah stok menjadi {new_stock}? (Y/N)").upper()
                if confirmation == "Y":
                    game[4] = int(new_stock)
                    print(f"Stok berhasil diperbarui menjadi: {new_stock}")
                    show_menu_update()  # Keluar dari loop setelah pembaruan berhasil
                elif confirmation == "N":
                    print("Perubahan stok dibatalkan.")
                    show_menu_update()  # Keluar dari loop tanpa mengubah data
                else:
                    print("Masukkan pilihan yang valid (Y/N).")
        else:
            print("Stok tidak valid. Masukkan angka yang benar untuk stok.")

# Fungsi utama untuk memperbarui data game (Update)
def update_game():
    try:
        while True:
            if not games:  # Memeriksa apakah list games kosong
                print("Tidak ada data game yang tersedia.")
                show_menu_update()  # Kembali ke menu update
                return  # Keluar jika tidak ada game

            headers = ["ID", "Title", "Genre", "Price (Rp)", "Stock"]
            print(tabulate(games, headers=headers, tablefmt="fancy_grid"))

            game_id = int(input("Masukkan ID game yang ingin diperbarui: "))

            # Loop untuk mencari game dengan ID yang dimasukkan
            found = False
            for game in games:
                if game[0] == game_id:
                    found = True
                    print(f"Data saat ini - ID: {game[0]}, Title: {game[1]}, Genre: {game[2]}, Price: Rp.{game[3]}, Stock: {game[4]}")

                    # Pilihan kolom untuk diperbarui
                    while True:
                        print("\nPilih kolom yang ingin diperbarui:")
                        print("1. Title")
                        print("2. Genre")
                        print("3. Price")
                        print("4. Stock")
                        print("5. Cancel Update")
                        
                        choice = input("Masukkan pilihan (1/2/3/4/5): ")

                        if choice == "1":  # Update title
                            update_title(game)
                            break

                        elif choice == "2":  # Update genre
                            update_genre(game)
                            break

                        elif choice == "3":  # Update price
                            update_price(game)
                            break

                        elif choice == "4":  # Update stock
                            update_stock(game)
                            break

                        elif choice == "5":  # Cancel update
                            print("Perubahan Data Game Dibatalkan.")
                            break  # Kembali keluar dari loop pilihan

                        else:
                            print("Masukkan pilihan yang valid (1/2/3/4/5).")
                    
                    # Menampilkan data setelah perubahan
                    print("\nData Game setelah diperbarui:")
                    print(f"ID: {game[0]}, Title: {game[1]}, Genre: {game[2]}, Price: Rp.{game[3]}, Stock: {game[4]}")
                    break

            if not found:
                print(f"Game dengan ID {game_id} tidak ditemukan.")
                show_menu_update()  # Kembali ke menu update jika game tidak ditemukan

    except ValueError:
        print("Input tidak valid. ID harus berupa angka.")

# Fungsi untuk menghapus game dari daftar (Delete)
def delete_game():
    while True:
        try:
            if len(games) > 0:
                headers = ["ID", "Title", "Genre", "Price (Rp)", "Stock"]
                print(tabulate(games, headers=headers, tablefmt="fancy_grid"))
   
            game_id = int(input("Masukkan ID game yang ingin dihapus: "))
            
            # Cek apakah game ditemukan
            found = False
            for game in games:
                if game[0] == game_id:
                    found = True
                    game_id, title, genre, price, stock = game
                    while True:
                        validasi_delete_game = input(
                            f'Apakah Anda yakin ingin menghapus ID: {game_id}, Title: {title}, Genre: {genre}, Price: Rp.{price}, Stock: {stock}? (Y/N) :\n'
                        ).upper()
                        if validasi_delete_game == "Y":
                            print(f"Game dengan ID: {game_id}, Title: {title}, Genre: {genre}, Price: Rp.{price}, Stock: {stock} berhasil dihapus.")
                            games.remove(game)
                            show_menu_delete() # kembali ke sub menu delete

                        elif validasi_delete_game == "N":
                            print("Tidak Jadi Menghapus Game")
                            show_menu_delete() # kembali ke sub menu delete

                        else:
                            print("Masukkan Pilihan Valid (Y/N)")
                            #memaksa memasukan input y/n yang valid
                    
            if not found:
                print(f"Game dengan ID {game_id} tidak ditemukan.")
                show_menu_delete() # kembalu ke sub menu delete kalau game_id tidak ditemukan
        except ValueError:
            print("Input tidak valid. ID harus berupa angka.")

# Fungsi untuk menghapus seluruh data game
def kosongkan_list():
    validasi_kosongkan = input("Apakah Anda yakin ingin mengosongkan daftar game? (Y/N): ").upper()
    
    if validasi_kosongkan == "Y":
        global games, game_id_counter
        games.clear()  # Clears all elements from the list
        game_id_counter = 1
        print("Semua Data Games Berhasil Dihapus.")
    elif validasi_kosongkan == "N":
        print("Penghapusan Data Games Dibatalkan.")
    else:
        print("Masukkan Pilihan Valid (Y/N).")
    show_menu_delete()

#Fungsi untuk Sub Menu Delete
def show_menu_delete():
    while True:
        print("\n=== Menu Hapus Game ===")
        print("1. Hapus Game")
        print("2. Hapus Semua Data Game")
        print("3. Kembali Ke Menu Utama")
        
    
        choice_create = input("Pilih operasi (1/2/3): ")
        
        if choice_create == "1":
            delete_game()
            break
        elif choice_create == "2":
            kosongkan_list()
        elif choice_create == "3":
            show_menu()
             # Keluar dari loop untuk kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            show_menu_delete()

# Fungsi untuk menampilkan menu
def show_menu():
    while True:
        print("\n=== Menu Penjualan Game ===")
        print("1. Tambah Game")
        print("2. Tampilkan Daftar Game")
        print("3. Perbarui Game")
        print("4. Hapus Game")
        print("5. Keluar")
        choice_main = input("Pilih operasi (1/2/3/4/5): ")
            
        if choice_main == "1":
            show_menu_create()
        elif choice_main == "2":
            show_menu_read()
        elif choice_main == "3":
            show_menu_update()
        elif choice_main == "4":
            show_menu_delete()
        elif choice_main == "5":
            print("Terima kasih telah menggunakan program penjualan game.")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

show_menu()
