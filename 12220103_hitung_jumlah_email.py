# TUGAS 8 PEMROGRAMAN KOMPUTER K-01 
# MUHAMMAD NAUFAL AQIL ZUHDI (12220103)
# 9 NOVEMBER 2021
# PROGRAM HITUNG JUMLAH EMAIL

#Membuka file mbox-short.txt
fhand = open("mbox-short.txt")

#Membuat list untuk menyimpan alamat email dari baris yang diawali dengan 'From '
list = []
for line in fhand:
    if not line.startswith("From "): 
        continue
    line = line.split()
    list.append(line[1])

#Membuat dictionary berisi key dan value untuk masing-masing alamat email
counts = {}
for word in list:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] = counts.get(word,0) + 1

#Membuat tuple dengan mempertimbangkan parameter (value, key) pada dictionary counts lalu memasukkannya ke dalam tmp
tmp = []
for key, value in counts.items():
    newtup = (value, key)
    tmp.append(newtup)

#Melakukan sort terhadap tmp untuk mendapatkan urutan nilai dari yang tertinggi
tmp = sorted(tmp, reverse = True)

print("Tiga besar alamat email dengan pengirim pesan terbanyak adalah:" )
#Mengambil 3 value tertinggi dari tmp
for value, key in tmp[:3]:
    print(key,"dengan jumlah", value, "pesan")
