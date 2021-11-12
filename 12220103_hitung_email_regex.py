# TUGAS 9 PEMROGRAMAN KOMPUTER K-01 
# MUHAMMAD NAUFAL AQIL ZUHDI (12220103)
# 16 NOVEMBER 2021
# PROGRAM SORT JUMLAH ALAMAT EMAIL DENGAN REGEX

#Memanggil library regular expression
import re

#Membuka file mbox-short.txt
fhand = open("mbox-short.txt")

#Membuat list untuk menyimpan alamat email dari baris yang diawali dengan 'From ' dengan bantuan regex
list = []
for line in fhand:
    x = re.findall('^From ([a-zA-Z0-9]\S*@\S*[a-zA-Z0-9])', line)
    if len(x) > 0:
        list.append(x[0])     
        
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

print("Urutan alamat email unik pada mbox-short.txt dengan jumlah terbanyak adalah sebagai berikut:")
for v, k in tmp:
    print("Alamat email", k, "dengan jumlah sebanyak", v)
