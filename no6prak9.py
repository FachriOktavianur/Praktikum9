nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*60)
print('NIM'.ljust(7),'NAMA'.ljust(12),'MID'.ljust(7),'UAS'.ljust(7),'NILAI AKHIR'.ljust(12),'STATUS')
print('-'*60)

for isi in nilai:
    NAkhir= (isi['mid'] + 2*isi['uas'])/3
    bulat=round(NAkhir,2)
    status = 'TIDAK LULUS'
    if (NAkhir>=60):
        status= 'LULUS'
    print(isi['nim'].ljust(7),isi['nama'].ljust(12),str(isi['mid']).ljust(7),str(isi['uas']).ljust(7),str(bulat).ljust(12), status)
print('='*60)
