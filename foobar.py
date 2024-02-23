from math import sqrt

# inisiasi list angka 1-100
list_number = list(range(1,101))

# balik urutan angka 1-100 ke 100-1
list_number.reverse()

# looping untuk cek angka di dalam list_number
for x in list_number:
    prime_checker = False # inisiasi checker bilangan prima

    # lakukan looping pengecekan bilangan prima jika x > 1
    if x > 1 :
        for y in range(2,int(sqrt(x))+1) : # cek angka 2 sampai dengan akar dari x + 1 
            if (x % y) == 0 :
                prime_checker = False
                break
            else :
                prime_checker = True
    
    # pengecualian untuk angka 1 
    else :
        prime_checker = False
    
    # pengecekan kondisi print untuk angka atau huruf
    if prime_checker is False :
        if x % 3 == 0 and x % 5 == 0 :
            print('FooBar',end=' ')
        elif x % 3 == 0 :
            print('Foo',end=' ')
        elif x % 5 == 0 :
            print('Bar',end=' ')
        else :
            print(x,end=' ')
