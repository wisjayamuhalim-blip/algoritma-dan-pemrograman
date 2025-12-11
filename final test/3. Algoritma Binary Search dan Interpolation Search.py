# ==========================================
# BINARY SEARCH
# ==========================================

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        print(f"Memeriksa indeks {mid}, nilai {arr[mid]}")  # tracking proses

        if arr[mid] == target:
            return mid  # ditemukan
        elif arr[mid] < target:
            low = mid + 1  # cari di kanan
        else:
            high = mid - 1  # cari di kiri

    return -1  # tidak ditemukan


# ==========================================
# INTERPOLATION SEARCH
# (lebih cepat pada data yang seragam/terurut rapi)
# ==========================================

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:

        # Hindari pembagian nol
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            else:
                return -1

        # Rumus posisi perkiraan
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        print(f"Memperkirakan indeks {pos}, nilai {arr[pos]}")

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1  # tidak ditemukan


# ==========================================
# DEMO PROGRAM
# ==========================================

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    print("=== BINARY SEARCH ===")
    hasil = binary_search(data, 70)
    print("Hasil pencarian:", hasil)

    print("\n=== INTERPOLATION SEARCH ===")
    hasil = interpolation_search(data, 70)
    print("Hasil pencarian:", hasil)
