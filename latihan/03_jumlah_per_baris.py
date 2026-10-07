# Latihan 3: Jumlah per Baris
# total_baris diinisialisasi di dalam loop luar agar ter-reset setiap perpindahan baris

for i in range(1, 5):
    total_baris = 0
    for j in range(1, 4):
        total_baris += i * j
    print(f"Jumlah baris {i} = {total_baris}")