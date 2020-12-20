def bintang(n):
    n= n//2 +1
    for bintang in range (n):
       bintang = bintang + 1
       print(('*' * (2*bintang-1)).center(2*n-1, ' '))

     
    for bintang2 in range (n,0,-1):
        bintang2 = bintang2-1
        print((''*(n-bintang2) + '*'*(bintang2)+'*'*(bintang2-1)).center(2*n-1, ' '))     
bintang(7)




































