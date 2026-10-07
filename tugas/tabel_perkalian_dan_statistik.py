# Tugas 3: Tabel Perkalian dan Statistik
# Program membentuk tabel perkalian n x n, hitung total per baris, total semua, dan banyak hasil genap

print("Tabel Perkalian dan Statistik")

# 1. Validasi input n
n = int(input("n: "))
while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

# 2. Inisialisasi akumulator keseluruhan dan counter genap
total_semua = 0
count_genap = 0

# 3. Nested loop untuk proses tabel
for i in range(1, n + 1):
    total_baris = 0  # Inisialisasi total per baris
    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4}", end="")  # Format rata kanan 4 karakter
        total_baris += hasil
        total_semua += hasil
        if hasil % 2 == 0:
            count_genap += 1
    print(f"  | Jumlah baris = {total_baris}")

# 4. Tampilkan statistik akhir
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")