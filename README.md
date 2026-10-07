# Pertemuan 06 Nested Loop Python

- **Nama:** SULASTRI
- **NIM:** 2225250152
- **Kelas:** B

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan
```bash
python tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3
- **Loop Luar (`i`):** Mengendalikan baris dari 1 sampai n dan menginisialisasi `total_baris = 0` pada setiap iterasi[cite: 11].
- **Loop Dalam (`j`):** Mengendalikan kolom dari 1 sampai n untuk menghitung `hasil = i * j`, mencetak nilai sel, serta menambahkan nilai ke `total_baris` dan `total_semua`[cite: 11].
- **Akumulator:**
  - `total_baris`: Direset setiap awal iterasi loop luar untuk menghitung jumlah per baris[cite: 7, 11].
  - `total_semua`: Dideklarasikan di luar kedua loop untuk mengakumulasi seluruh nilai tabel[cite: 7, 11].
- **Counter (`count_genap`):** Bertambah 1 setiap kali `hasil % 2 == 0`[cite: 7, 11].

## Hasil Pengujian

| Input ($n$) | Jumlah Pasangan | Expected Total | Actual Total | Expected Genap | Actual Genap | Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1 | 1 | 1 | 0 | 0 | PASS |
| 2 | 4 | 9 | 9 | 3 | 3 | PASS |
| 3 | 9 | 36 | 36 | 5 | 5 | PASS |

## Analisis Efisiensi
Untuk input $n$, pernyataan `hasil = i * j` di dalam badan loop dalam akan dieksekusi sebanyak $n \times n$ ($n^2$) kali[cite: 5, 11, 12].

## Refleksi
Kesalahan umum pada nested loop adalah menempatkan akumulator `total_baris` di luar loop luar (sehingga nilainya terus membesar dan akumulasi tidak direset per baris) atau menempatkannya di dalam loop dalam (sehingga ter-reset di setiap sel)[cite: 7, 9]. Pembenahannya adalah menempatkan inisialisasi `total_baris = 0` tepat setelah loop luar dimulai dan sebelum loop dalam berjalan[cite: 7, 9].