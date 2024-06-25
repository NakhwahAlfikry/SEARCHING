def binary_search(arr, x):
    
    low = 0 
    high = len(arr) -1
    mid = 0
    
    while low <= high:
        mid = (high + low) // 2
        
        if arr[mid] < x:
            low = mid + 1
            
        elif arr[mid] > x:
            high = mid - 1
            
        else:
            return mid
            
            
        return -1
        
        
def main ():
    arr = list(map(int, input("masukan daftar elemen yang sudah terurut (pisahkan dengan spasi): ").splitt()))
    
    x  = int(input("masukan elemen yang akan dicari: "))
    
    result = binary_search (arr, x)
    
    if result != -1:
        print(f"elemen ditemukan pada indeks {result}")
    else:
        print("elemen tidak ditemukan dalam daftar")
        
if __name__ == "__main__":
    main ()