#deklarasikan array
array = []
#membuat variable total
total = 0
#membuat variable n untuk menanmpung jumlah array
# n = jumlah elemen
n = int(input("Masukan Jumlah Elemen Array : "))
for x in range(n) :
#menginputkan nilai yang akan bertambah 1
    nilai = float(input("Masukan Nilai ke- {} :".format(x+1)))
    array.append(nilai)
    #menampilkan jumlah dari nilai
    print("\nHasil nilai totaL adalah: {}".format(sum(array)))
    print("Hasil Rata - Rata Adalah : {}".format(sum(array)/n))


