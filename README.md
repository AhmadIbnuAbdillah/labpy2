# labpy2

Ahmad Ibnu Abdillah

Bahasa Pemrograman

312410489

TI.24.A.5

#Penjelasan Kode Bioskop
``` Python
tipe_tiket = input("masukan tipe tiket (regular/vip): ").lower()
```
Program meminta input dari pengguna untuk menentukan tipe tiket (apakah "regular" atau "vip").
Input ini dikonversi menjadi huruf kecil (lower()), sehingga input tidak case-sensitive (misalnya, "VIP" dan "vip" diperlakukan sama).

``` Python
status_member = input("apakah anda memiliki kartu member? (yes/no): ").lower()
```
Program meminta input untuk mengetahui apakah pengguna memiliki kartu member atau tidak.
Sama seperti sebelumnya, input dikonversi menjadi huruf kecil.

``` Python
harga_tiket = 50000 if tipe_tiket == "regular" else 100000
```
Jika tipe tiket adalah "regular", maka harga tiket adalah 50.000, jika tidak (berarti "vip"), harga tiket adalah 100.000.

``` Python
diskon = 0.2 if status_member == "yes" else 0
```
Jika pengguna memiliki kartu member (status_member adalah "yes"), maka diskon sebesar 20% (0.2), jika tidak, tidak ada diskon (diskon = 0)

``` Python
total_harga = harga_tiket * (1 - diskon)
```
Total harga dihitung dengan mengurangi diskon dari harga tiket. Jika ada diskon 20%, berarti harga tiket akan dikalikan dengan 80% dari harga aslinya

``` Python
print("total harga yang harus dibayar: Rp", int(total_harga))
```
Program menampilkan total harga tiket yang harus dibayar oleh pengguna. total_harga dikonversi menjadi bilangan bulat dengan int() untuk menghindari angka desimal pada hasil akhir.

# Flowchart
![Foto](https://github.com/AhmadIbnuAbdillah/Foto/blob/1021970f8247d21f76ebd29d96687f1c4d3f171e/Screenshot%202024-10-29%20212035.png)

# Hasil Kode
![Foto](https://github.com/AhmadIbnuAbdillah/Foto/blob/742ae7e116c78302493f147e10536a8aaa1b1ec1/Screenshot%202024-10-29%20195501.png)

# Penjelasan Kode Kalkulator
``` Python
angka1 = float(input("masukan angka pertama: "))
angka2 = float(input("masukan angka kedua: "))
operator = input("masukan operator aritmatika (+, -, *, /): ")
```
Program meminta input dari pengguna untuk dua angka (angka1 dan angka2).
Input ini dikonversi menjadi tipe float (bilangan desimal) agar bisa menangani operasi desimal.
Kemudian program meminta pengguna untuk memilih operator aritmatika seperti +, -, *, atau /.

``` Python
if operator == '+':
    hasil = angka1 + angka2
```
Jika pengguna memasukkan operator +, maka program melakukan penjumlahan antara angka1 dan angka2.

``` Python
elif operator == '-':
    hasil = angka1 - angka2
```
Jika operator adalah -, program mengurangkan angka2 dari angka1.

``` Python
elif operator == '*':
    hasil = angka1 * angka2
```
Jika operator adalah *, program mengalikan kedua angka.

``` Python
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "error: pembagian dengan nol tidak diperbolehkan"
```
Jika operator adalah /, program melakukan pembagian. Sebelum itu, dicek apakah angka2 bukan nol, karena pembagian dengan nol tidak diperbolehkan. Jika angka2 nol, maka program memberikan pesan kesalahan

``` Python
else:
    hasil = "error: operator tidak valid"
```
Jika operator yang dimasukkan tidak termasuk +, -, *, atau /, maka program menampilkan pesan kesalahan "operator tidak valid".

``` Python
print("hasil: ", hasil)
```
Program mencetak hasil operasi yang telah dihitung di atas, atau pesan kesalahan jika ada.

# Flowchart
![Foto](https://github.com/AhmadIbnuAbdillah/Foto/blob/95ec522d89e2192d0d1fe406c964070fd0d004a6/Screenshot%202024-10-29%20223812.png)

# Hasil Kode
![Foto](https://github.com/AhmadIbnuAbdillah/Foto/blob/c8e12b6f13ebe55dec68c9c5ad950c5097a0b880/Screenshot%202024-10-29%20201646.png)
