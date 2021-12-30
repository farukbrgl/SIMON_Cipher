#!/usr/bin/env python
# coding: utf-8


# def SIMON(n,m, plainText, key):
#     return cipherText




import numpy
numpy.set_printoptions(formatter={'int':hex})


###### n ve m değeri girildi
#bu değerlere göre T ve j oluşturuldu

print("n=16, 24, 32, 48, 64 olabilir\nm 2, 3, 4 olabilir")
n = int(input("n değerini giriniz:"))
m = int(input("m değerini giriniz:"))
z_0 = [1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0]
z_1 = [1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0]
z_2 = [1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1]
z_3 = [1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1,1,1,1]
z_4 = [1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1]

T = 0
j = 0
if (n == 16 and m == 4):
    T = 32
    j = 0
    print(T,j)
elif (n == 24 and m == 3):
    T = 36
    j = 0
    print(T,j)
elif (n == 24 and m == 4):
    T = 36
    j = 1
    print(T,j)
elif (n == 32 and m == 3):
    T = 42
    j = 2
    print(T,j)
elif (n == 32 and m == 4):
    T = 44
    j = 3
    print(T,j)
elif (n == 48 and m == 2):
    T = 52
    j = 2
    print(T,j)
elif (n == 48 and m == 3):
    T = 54
    j = 3
    print(T,j)
elif (n == 64 and m == 2):
    T = 68
    j = 2
    print(T,j)
elif (n == 24 and m == 3):
    T = 69
    j = 3
    print(T,j)
elif (n == 64 and m == 4):
    T = 72
    j = 4
    print(T,j)
else:
    print("yanlış değer girdiniz\ndevam etmeyiniz")




#plaintext ve key oluşturuldu
import random
# plainText_1 = numpy.array([random.randint(0, 15) for i in range(n)])
# plainText_2 = numpy.array([random.randint(0, 15) for i in range(n)])
plainText_1 = 0x6565
plainText_2 = 0x6877

# print (plainText_1, plainText_2)
print (format(plainText_1, '04x'), format(plainText_2, "04X"))




# key_0 = [random.randint(1, 10) for i in range(n)]
# key_1 = [random.randint(1, 10) for i in range(n)]
# key_2 = [random.randint(1, 10) for i in range(n)]
# key_3 = [random.randint(1, 10) for i in range(n)]
key_0 = 0x1918
key_1 = 0x1110
key_2 = 0x0908
key_3 = 0x0100
#key = [[random.randint(1, 10)] for i in range(255) for j in range(255)]
print(key_0, key_1, key_2, key_3)
print (format(key_0, '04x'), format(key_1, "04X"), format(key_2, "04X"), format(key_3, "04X"))
#print (key)




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
key_0_list= []
def key_generation(key_0, key_1, key_2, key_3, m, T):
    if (m == 2):
        for i in range(0, T-1):
            temp1 = numpy.roll(key_1, -3)
            temp2 = numpy.roll(temp1, -1)
            temp3 = key_0 ^ temp1
            temp4 = temp2 ^ temp3
            temp5 = temp4 ^ c ^ z_2[i]
            key_0 = key_1
            key_1 = temp5
#             print(key_0, key_1)
        return key_0, key_1
    elif (m == 3):
        temp1 = numpy.roll(key_2, -3)
        temp2 = numpy.roll(temp1, -1)
        temp3 = key_0 ^ temp1
        temp4 = temp2 ^ temp3
        if (n == 24):
            temp5 = temp4 ^ c ^ z_0[i]
        elif (n == 32):
            temp5 = temp4 ^ c ^ z_2[i]
        elif (n == 32):
            temp5 = temp4 ^ c ^ z_3[i]
        key_0 = key_1
        key_1 = key_2
        key_2 = temp5
        print(key_0, key_1, key_2)
        return key_0, key_1, key_2
    elif (m == 4):
        for i in range(0, T-1):
            key_0_list.append(key_0)
            temp1 = numpy.roll(key_3, -3)
            temp2 = key_1 ^ temp1
            temp3 = numpy.roll(temp2, -1)
            temp4 = key_0 ^ temp2
            temp5 = temp3 ^ temp4
            if (n == 16):
                temp6 = temp5 ^ c ^ z_0[i]
            elif (n == 32):
                temp6 = temp5 ^ c ^ z_2[i]
            elif (n == 32):
                temp6 = temp5 ^ c ^ z_3[i]
            key_0 = key_1
            key_1 = key_2
            key_2 = key_3
            key_3 = temp6
            print("key{} = {}\nkey{} = {}\nkey{} = {}\nkey{} = {}\n".format(i, key_0, i+1, key_1, i+2, key_2, i+3, key_3))
        key_0_list.append(key_0)

        return key_0, key_1, key_2, key_3




def enc(plainText_1, plainText_2, key_0, T):
    t1 = plainText_1
    t2 = plainText_2
    for i in range (T-1):
        tmp = t2
        t2 = t1 ^ (numpy.roll(t2, 1) & numpy.roll(t2, 8)) ^ (numpy.roll(t2, 2)) ^ key_0_list[i]
        t1 = tmp
        # print(plainText_1, p16lainText_2)
        # print(key_0)
    print(t1,t2)
    return t1, t2




c=0
c = 2**n - 1
print(c)
# z_0
# key_generation(key_0, key_1, key_2, key_3, m)
# enc(plainText_1, plainText_2, key_0)




# for i in range(0, T-1):
key_0, key_1, key_2, key_3 =key_generation(key_0, key_1, key_2, key_3, m, T)
a,b= enc(plainText_1, plainText_2, key_0, T)
# print(type(key_0))
# print(type(key_1))
# print(type(key_2))
# print(type(key_3))
# print(type(m))
# print(type(plainText_1))
# print(type(plainText_2))
print (format(a, '04x'), format(b, "04X"))




# print (format(plainText_1, '04x'), format(plainText_2, "04X"))