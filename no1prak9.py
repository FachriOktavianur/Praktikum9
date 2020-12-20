def ubahHuruf(teks, a, b) :
    teks = list(teks)
    hasil = ""
    
    for huruf in teks :
        if(huruf == a) :
           huruf = b
        hasil = "".join([hasil,huruf])
    return hasil

print(ubahHuruf("MATEMATIKA", "T", "S"))

print('-------------------------')

def ubahHuruf(teks, a, b):
    teks = teks.replace(a, b)
    return teks
print(ubahHuruf('MATEMATIKA', 'T', 'S'))
