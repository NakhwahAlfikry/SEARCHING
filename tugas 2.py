def binary_search(arr, low, high, x):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def print_menu():
    print("\nMenu:")
    print("1. Input data")
    print("2. Lihat data")
    print("3. Hapus data")
    print("4. Cek data")
    print("5. Keluar")

def input_data(arr):
    data = int(input("Masukkan angka untuk ditambahkan: "))
    arr.append(data)
    arr.sort()
    print("Data berhasil ditambahkan.")

def lihat_data(arr):
    print("Data saat ini:", arr)

def hapus_data(arr):
    data = int(input("Masukkan angka yang akan dihapus: "))
    idx = binary_search(arr, 0, len(arr)-1, data)
    if idx != -1:
        arr.pop(idx)
        print("Data", data, "telah dihapus.")
    else:
        print("Data tidak ditemukan.")

def cek_data(arr):
    data = int(input("Masukkan angka yang ingin dicek: "))
    idx = binary_search(arr, 0, len(arr)-1, data)
    if idx != -1:
        print("Data", data, "ditemukan pada indeks", idx)
    else:
        print("Data", data, "tidak ditemukan.")

def main():
    arr = []
    while True:
        print_menu()
        choice = input("Pilih menu (1/2/3/4/5): ")

        if choice == '1':
            input_data(arr)
        elif choice == '2':
            lihat_data(arr)
        elif choice == '3':
            hapus_data(arr)
        elif choice == '4':
            cek_data(arr)
        elif choice == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

if __name__ == "__main__":
    main()
