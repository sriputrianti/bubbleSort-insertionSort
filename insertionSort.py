def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

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

# Mengurutkan daftar nilai menggunakan insertion sort
print("\nProses sorting:")
insertion_sort(nilai)

# Menampilkan daftar siswa beserta nilai yang sudah diurutkan
print("\nSetelah sorting:")
for i in range(len(nilai)):
    for j in range(len(siswa)):
        if siswa[j][1] == nilai[i]:
            print(f"{siswa[j][0]}: {siswa[j][1]}")
            break
