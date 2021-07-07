import datetime
from time import process_time_ns

x = datetime.datetime.now()

print("========================================================")
print("                     input Slip Gaji                  ")
print("             Tanggal : ",x.strftime("%x"))
print("========================================================")


golongan = ['1','2','3']
gajipokok = [2500000,4500000,6500000]

nama = input("Nama                    =       ")
g= input("Golongan                =       ")
gol = int(g)
if gol == 1 :
    idx = 0
    tunjangan = 0.01
elif gol == 2:
    idx = 1
    tunjangan = 0.03
elif gol == 3:
    idx = 2
    tunjangan = 0.05
else :
    print("Masukkan kembali golongan dengan benar")

print("Laki - Laki atau Perempuan")
jenis_kelamin = input("Jenis kelamin           =      ")
print ("Kawin atau belum")
status_kawin = input("status Kawin            =      ")
status_anak = input("Apakah punya anak       =      ")

#istri
if jenis_kelamin == "Laki Laki" or "Laki laki" or "laki laki" and status_kawin == "Kawin" or "kawin":
   tunjanganistri = int(gajipokok[idx]) * tunjangan
else :
    tunjanganistri = 0
#Anak
if status_kawin == "Kawin" or "kawin" and status_anak == "Iya" or "iya":
    tunjangananak = int(gajipokok[idx]) * 0.02
else :
    tunjangananak = 0
#Bruto
gajibruto = int(gajipokok[idx]) + int(tunjanganistri) + int(tunjangananak)

#Jabatan
biayajabatan = int(gajibruto) * 0.05

#Pensiun
iuran_pensiun = 15500

#Organsasi
iuran_organisasi = 3500

#Net
GajiNetto = int(gajibruto) - int(iuran_organisasi) - int(iuran_pensiun)
 


    

    


print("========================================================")
print("                         Slip Gaji                  ")
print("                 Tanggal : ",x.strftime("%x"))
print("========================================================")
print("Nama                     " + nama)
print("Golongan                 " + str(gol))
print("jenis kelamin            " + jenis_kelamin)
print("Staus Kawin              " + status_kawin)
print("Gaji Pokok               Rp " + format(gajipokok[idx],',.2f'))
print("Tunjangan istri          Rp " + format(tunjanganistri,',.2f'))
print("Tunjangan Anak           Rp " + format(tunjangananak,',.2f'))
print(">>Gaji bruto             Rp " + format(gajibruto,',.2f'))
print("========================================================")
print("Biaya Jabatan            Rp " + format(biayajabatan,',.2f'))
print("Iuran Pensiun            Rp " + format(iuran_pensiun,',.2f'))
print("Iuran Organisasi         Rp " + format(iuran_organisasi,',.2f'))
print(">>Gaji Netto             Rp " + format(GajiNetto,',.2f'))
