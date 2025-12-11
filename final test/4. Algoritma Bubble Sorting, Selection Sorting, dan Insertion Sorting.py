# ==========================================
# BUBBLE SORT
# ==========================================

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]   # tukar
    return arr


# ==========================================
# SELECTION SORT
# ==========================================

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # cari nilai terkecil
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # tukar
    return arr


# ==========================================
# INSERTION SORT
# ==========================================

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # geser elemen yang lebih besar ke kanan
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # tempatkan key di posisi yang benar
    return arr


# ==========================================
# DEMO PROGRAM
# ==========================================

if __name__ == "__main__":
    data1 = [64, 34, 25, 12, 22, 11, 90]
    data2 = data1.copy()
    data3 = data1.copy()

    print("Data awal:", data1)

    print("\n=== BUBBLE SORT ===")
    print(bubble_sort(data1))

    print("\n=== SELECTION SORT ===")
    print(selection_sort(data2))

    print("\n=== INSERTION SORT ===")
    print(insertion_sort(data3))
