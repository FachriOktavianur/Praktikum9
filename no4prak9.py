import random
def shuffleString(r,n) :
    Hasil = []
    i = 0
    while i < n :
        shuffle = ''.join(random.sample(r,len(r)))
        if (shuffle not in Hasil) :
            Hasil += [shuffle]
            i += 1
    print(Hasil)


shuffleString('aku',2)
shuffleString('aku',3)
shuffleString('aku',4)

