def bintang(n):
    for bintang in range (n):
       bintang = bintang + 1
       print(('*' * (2*bintang-1)).center(2*n-1, ' '))
        
bintang(4)

