mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print('='*70)
print('NIM'.ljust(10),'NAMA MAHASISWA'.ljust(25),'TANGGAL LAHIR'.ljust(20),'TEMPAT LAHIR')
print('-'*70)

for data in mhs :
    List           = data.split(":")
    nim                = List[0]
    nama               = List[1]
    tglLahir           = List[2]
    dataTglLahir       = tglLahir.split('-')
    formatBaruTglLahir = "{0}/{1}/{2}".format(dataTglLahir[0],dataTglLahir[1],dataTglLahir[2])

    tempatLahir        = List[3]

    print(nim.ljust(10), nama.ljust(25), formatBaruTglLahir.ljust(20), tempatLahir)

print("-" *70)
