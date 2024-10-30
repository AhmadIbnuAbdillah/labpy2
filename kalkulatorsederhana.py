angka1 = float(input("masukan angka pertama: "))
angka2 = float(input("masukan angka kedua: "))
operator = input("masukan operator aritmatika (+, -, *, /): ")

if operator == '+':
    hasil = angka1 + angka2
elif operator == '-':
    hasil = angka1 - angka2
elif operator == '*':
    hasil = angka1 * angka2
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "error: pembagian dengan nol tidak diperbolehkan"
else:
    hasil = "error: operator tidak valid"

print("hasil: ", hasil)