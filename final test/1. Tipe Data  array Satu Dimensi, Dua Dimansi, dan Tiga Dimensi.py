# ================================
# ARRAY / LIST 1 DIMENSI
# ================================
array1D = [10, 20, 30, 40, 50]

print("Array 1 Dimensi:")
print(array1D)               # tampilkan isi
print("Elemen ke-3:", array1D[2])  # akses elemen indeks ke-2
print()


# ================================
# ARRAY / LIST 2 DIMENSI (MATRIKS)
# ================================
array2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Array 2 Dimensi:")
for baris in array2D:
    print(baris)

print("Akses elemen baris 2 kolom 3:", array2D[1][2])  # 6
print()


# ================================
# ARRAY / LIST 3 DIMENSI
# Contoh: 2 blok, tiap blok berisi 2x3 angka
# ================================
array3D = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print("Array 3 Dimensi:")
for blok in array3D:
    for baris in blok:
        print(baris)
    print("--- blok selesai ---")

print("Akses elemen blok 2, baris 1, kolom 3:", array3D[1][0][2])  # 9
