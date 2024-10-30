tipe_tiket = input("masukan tipe tiket (regular/vip): ").lower()
status_member = input("apakah anda memiliki kartu member? (yes/no): ").lower()
harga_tiket = 50000 if tipe_tiket == "regular" else 100000
diskon = 0.2 if status_member == "yes" else 0
total_harga = harga_tiket * (1 - diskon)
print("total harga yang harus dibayar: Rp", int(total_harga))