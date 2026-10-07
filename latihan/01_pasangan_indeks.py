# Latihan 1: Pasangan Indeks
# Loop luar (i) mengendalikan baris (1..3), loop dalam (j) mengendalikan kolom (1..4)
# Counter menghitung total pasangan yang terbentuk

count = 0
for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
        count += 1

print(f"Banyak pasangan = {count}")