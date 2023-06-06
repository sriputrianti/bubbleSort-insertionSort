def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Melakukan perulangan untuk setiap pasangan elemen
        for j in range(0, n - i - 1):
            # Membandingkan dua elemen bersebelahan
            if arr[j] < arr[j + 1]:
                # Menukar posisi jika elemen sebelumnya lebih kecil dari elemen setelahnya
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # Menampilkan proses sorting
                print(f"Sorting: {arr}")


# Daftar nilai siswa
siswa = [("Siswa R", 80), ("Siswa U", 92), ("Siswa I", 70), ("Siswa P", 98), ("Siswa T", 89)]

# Mengambil nilai-nilai dari daftar siswa
nilai = [x[1] for x in siswa]

# Menampilkan daftar nilai sebelum diurutkan
print("Sebelum sorting:")
for s, n in siswa:
    print(f"{s}: {n}")

# Mengurutkan daftar nilai menggunakan bubble sort
print("\nProses sorting:")
bubble_sort(nilai)

# Menampilkan daftar siswa beserta nilai yang sudah diurutkan
print("\nSetelah sorting:")
for i in range(len(nilai)):
    for j in range(len(siswa)):
        if siswa[j][1] == nilai[i]:
            print(f"{siswa[j][0]}: {siswa[j][1]}")
            break
