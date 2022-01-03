#!/usr/bin/env python
# coding: utf-8

"""
SIMON Hafif Blok Şifreleyicisinin Python ile Gerçeklenmesi
Orijinal makaleye https://eprint.iacr.org/2013/404 adresinden ulaşabilirsiniz.
"""

"""
plaintext ve key oluşturuldu
bunlar orijinal makaledeki n=16, m=4 durumunda verilen başlangıç vektörleri
sonuçların doğruluğunu makaleden inceleyebilirsiniz
farklı boyuttaki şifreleyici için farklı değerler vermelisiniz
"""
plainText_1 = 0x6565 #most significant
plainText_2 = 0x6877 #least significant
print ("plaintexts in decimal",plainText_1, plainText_2)
print ("plaintexts in hex",format(plainText_1, '04x'), format(plainText_2, "04X"))

key_3 = 0x1918 #most significant
key_2 = 0x1110
key_1 = 0x0908
key_0 = 0x0100 #least significant
print ("keys 0123 in decimal",key_0, key_1, key_2, key_3)
print ("keys 0123 in hex",format(key_0, '04x'), format(key_1, "04X"), format(key_2, "04X"), format(key_3, "04X"))

#z sabitleri oluşturuluyor
z_0 = [1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0]
z_1 = [1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0]
z_2 = [1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1]
z_3 = [1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1,1,1,1]
z_4 = [1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1]


"""
n ve m değerleri kullanıcıdan isteniyor
bu değerlere göre T ve j oluşturuluyor
"""
print("n=16, 24, 32, 48, 64 olabilir\n m 2, 3, 4 olabilir")
n = int(input("n değerini giriniz:"))
m = int(input("m değerini giriniz:"))
c = 0
c = 2**(n) - 1


T = 0
j = 0
if (n == 16 and m == 4):
    T = 32
    j = 0
    print("T,j:",T,j)
elif (n == 24 and m == 3):
    T = 36
    j = 0
    print("T,j:",T,j)
elif (n == 24 and m == 4):
    T = 36
    j = 1
    print("T,j:",T,j)
elif (n == 32 and m == 3):
    T = 42
    j = 2
    print("T,j:",T,j)
elif (n == 32 and m == 4):
    T = 44
    j = 3
    print("T,j:",T,j)
elif (n == 48 and m == 2):
    T = 52
    j = 2
    print("T,j:",T,j)
elif (n == 48 and m == 3):
    T = 54
    j = 3
    print("T,j:",T,j)
elif (n == 64 and m == 2):
    T = 68
    j = 2
    print("T,j:",T,j)
elif (n == 24 and m == 3):
    T = 69
    j = 3
    print("T,j:",T,j)
elif (n == 64 and m == 4):
    T = 72
    j = 4
    print("T,j:",T,j)
else:
    print("yanlış değer girdiniz\ndevam etmeyiniz")







import numpy
numpy.set_printoptions(formatter={'int':hex})
#key = [random.randint(1, 10) for i in range(m) for j in range(n)]
#sağa çembersel kaydırma fonksiyonu
#numpy.roll(key_0,1)

#print(key)
#for k in key:
##    for j in key[k]:
#        key[j] = hex(key[j])    
#for j in range(m, T-1):
#    tmp = numpy.roll(key[i][j], -3)
#    print(tmp)

"""
z değerlerinin fonksiyonu henüz düzgün değildir.
"""
print(type(z_0))
# z_rev=z_0
# z_rev.reverse()
# print(z_rev)
key_0_list= []
def key_generation(key_0, key_1, key_2, key_3, m, T):
    key_0_n = key_0
    key_1_n = key_1
    key_2_n = key_2
    key_3_n = key_3
    if (m == 2):
        for i in range(0, T-1):
            temp1 = numpy.roll(key_1, -3)
            temp2 = numpy.roll(temp1, -1)
            temp3 = key_0_n ^ temp1
            temp4 = temp2 ^ temp3
            temp5 = temp4 ^ c ^ z_2[i]
            key_0_n = key_1
            key_1 = temp5
#             print(key_0_n, key_1)
        return key_0_n, key_1
    elif (m == 3):
        temp1 = numpy.roll(key_2, -3)
        temp2 = numpy.roll(temp1, -1)
        temp3 = key_0_n ^ temp1
        temp4 = temp2 ^ temp3
        if (n == 24):
            temp5 = temp4 ^ c ^ z_0[i]
        elif (n == 32):
            temp5 = temp4 ^ c ^ z_2[i]
        elif (n == 32):
            temp5 = temp4 ^ c ^ z_3[i]
        key_0_n = key_1
        key_1 = key_2
        key_2 = temp5
        print(key_0_n, key_1, key_2)
        return key_0_n, key_1, key_2
    elif (m == 4):
        print (key_0_n)
        print ("key_0_n in hex",format(key_0_n, '016b'))
        key_0_list.append(key_0_n)
        for i in range(T):
            print ("key{} = {}".format(i, key_0_n))
            print ("key_0_n in hex",format(key_0_n, '016b'))
            temp1 = (key_3 >> 3)|(key_3 << (n - 3)) & c
            temp2 = key_1 ^ temp1
            temp3 = (temp2 >> 1)|(temp2 << (n - 1)) & c
            # temp4 = key_0_n ^ temp2
            # temp5 = temp3 ^ temp4
            if (n == 16):
                # temp6 = temp5 ^ c ^ z_rev[i]
                # c_z = c ^ 3 ^ ((z_0[i] >> ((i+m) % 62)) & 1)
                # c_z = c ^ 3
                # c_z = z_0[i]
                # c_z = (z_0[i] >> ((i) % 62)) 
                # c_z = ((z_0[i] >> ((i) % 62)) & 1)
                print(z_0[i % 62])
                print(i)
                print(z_0)
                c_z = c ^ 3 ^ ((z_0[i % 62]))
                # c_z = c ^ 3 ^ 1
                print ("z{} = {}".format(i, z_0[i]))
                # temp6 = temp2 ^ key_0_n ^ temp3 ^ c_z
                # temp6 = c_z
                # temp6 = temp3 ^ c_z
                # temp6 = temp2 ^ temp3 ^ c_z
                temp6 = temp2 ^ key_0_n ^ temp3 ^ c_z
            elif (n == 32):
                temp6 = temp5 ^ c ^ z_2[i]
            elif (n == 32):
                temp6 = temp5 ^ c ^ z_3[i]
            key_next = key_0_n
            key_0_n = key_1
            key_1 = key_2
            key_2 = key_3
            key_3 = temp6
            key_0_list.append(key_next)
        #key_0_list.append(key_0)

        return key_0_list




def enc(plainText_1, plainText_2, key_0, T):
    t1 = plainText_1
    t2 = plainText_2
    for i in range (T-1):
        tmp = t2
        #(n << d)|(n >> (INT_BITS - d))
        t2 = t1 ^ ((t2 >> 1) & (t2 >> 8)) ^ ((t2 >> 2)) ^ key_0[i]
        #print(key_0)
        t1 = tmp 
        # print(plainText_1, p16lainText_2)
        # print(key_0)
    print(t1,t2)
    return t1, t2






print(c)
# z_0
# key_generation(key_0, key_1, key_2, key_3, m)
# enc(plainText_1, plainText_2, key_0)




# for i in range(0, T-1):
key_list =key_generation(key_0, key_1, key_2, key_3, m, T)
a,b= enc(plainText_1, plainText_2, key_list, T)
# print(type(key_0))
# print(type(key_1))
# print(type(key_2))
# print(type(key_3))
# print(type(m))
# print(type(plainText_1))
# print(type(plainText_2))
print (format(a, '04x'), format(b, "04X"))




# print (format(plainText_1, '04x'), format(plainText_2, "04X"))