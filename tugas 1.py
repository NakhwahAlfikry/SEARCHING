def sequential_search(arr, nama_b):
    for i in range(len(arr)):
        if arr[i]['nama'] == nama_b:
            return i
    return -1

def print_menu():
    print("\nMenu:")
    print("1. Tambah barang")
    print("2. Lihat barang")
    print("3. Hapus barang")
    print("4. Cek data barang")
    print("5. Keluar")

def tambah_barang(arr):
    nama = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga barang: "))
    stok = int(input("Masukkan stok barang: "))
    item = {
        'nama': nama,
        'harga': harga,
        'stok': stok
    }
    arr.append(item)
    print("Barang berhasil ditambahkan.")

def lihat_barang(arr):
    if not arr:
        print("Belum ada barang tersedia.")
    else:
        print("Daftar Barang:")
        for idx, item in enumerate(arr):
            print(f"{idx + 1}. {item['nama']} - Harga: {item['harga']}, Stok: {item['stok']}")

def hapus_barang(arr):
    nama = input("Masukkan nama barang yang akan dihapus: ")
    idx = sequential_search(arr, nama)
    if idx != -1:
        del arr[idx]
        print(f"Barang {nama} berhasil dihapus.")
    else:
        print(f"Barang {nama} tidak ditemukan.")

def cek_data(arr):
    nama = input("Masukkan nama barang yang akan dicek: ")
    idx = sequential_search(arr, nama)
    if idx != -1:
        item = arr[idx]
        print(f"Detail Barang {nama}:")
        print(f"Nama: {item['nama']}")
        print(f"Harga: {item['harga']}")
        print(f"Stok: {item['stok']}")
    else:
        print(f"Barang {nama} tidak ditemukan.")

def main():
    arr = []
    while True:
        print_menu()
        choice = input("Pilih menu (1/2/3/4/5): ")

        if choice == '1':
            tambah_barang(arr)
        elif choice == '2':
            lihat_barang(arr)
        elif choice == '3':
            hapus_barang(arr)
        elif choice == '4':
            cek_data(arr)
        elif choice == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

if __name__ == "__main__":
    main()
