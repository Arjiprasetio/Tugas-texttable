Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import texttable as tt

nama = []
nim = []
nilai_tugas = []
nilai_uts = []
nilai_uas = []
nilai_akhir = []

x = [[]]

jawab = "y"

tab = tt.Texttable()

while (jawab == 'y'):
    nama.append(input("Masukkan Nama: "))
    nim.append(input("Masukkan Nim: "))
    tugas = int(input("Nilai Tugas: "))
    tugas = float(tugas)
    nilai_tugas.append(tugas)
    uts = int(input("Nilai UTS: "))
    uts = float(uts)
    nilai_uts.append(uts)
    uas = int(input("Nilai UAS: "))
    uas = float(uas)
    nilai_uas.append(uas)
    hasil = (tugas+uts+uas)/3
    nilai_akhir.append(hasil)
    jawab = input("Tambah data [y/n]?  ")


for i in nama:
    idx = nama.index(i)
    x.append([idx+1,nama[idx],nim[idx],nilai_tugas[idx],nilai_uts[idx],nilai_uas[idx],nilai_akhir[idx]])
tab.add_rows(x)
tab.set_cols_align(['l','l','l','r','r','r','r'])
tab.header(['No','Nama','Nim','Nilai Tugas', 'Nilai UTS', 'Nilai UAS','Nilai Akhir'])
print (tab.draw())

