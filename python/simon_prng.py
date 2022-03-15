#!/usr/bin/env python
# coding: utf-8

# execution time : 8.114 s
"""
SIMON Hafif Blok Şifreleyicisinin Python ile Gerçeklenmesi
Orijinal makaleye https://eprint.iacr.org/2013/404 adresinden ulaşabilirsiniz.
"""

"""
plaintext, ciphertext ve key oluşturuldu
encryption işlemi gerçekleştiriliyor
bunlar orijinal makaledeki n=64, m=4 durumunda verilen başlangıç vektörleri
sonuçların doğruluğunu makaleden inceleyebilirsiniz
farklı boyuttaki şifreleyici için farklı değerler vermelisiniz
"""


def SIMON(plainText_1, plainText_2, key_3, key_2, key_1, key_0, n=64, m=4):
    # plainText_1 = 0x6373656420737265 #most significant
    # plainText_2 = 0x6c6c657661727420 #least significant
    print(format(plainText_1, '0X'), format(
        plainText_2, "0X"), "plaintexts in start in hex")

    # cipherText_2 = 0x49681b1e1e54fe3f
    # cipherText_1 = 0x65aa832af84e0bbc
    # print (format(cipherText_1, '016X'), format(cipherText_2, "016X"), "ciphertexts in start in hex")

    # key_3 = 0x9ce73805171222e1  # most significant
    # key_2 = 0x67fd8bae41f85b4a
    # key_1 = 0xbde2432699ac471d
    # key_0 = 0x4a99b7f867a1886c  # least significant
    print(format(key_3, '0x'), format(key_2, "0X"), format(
        key_1, "0X"), format(key_0, "0X"), "keys in hex")

    # z sabitleri oluşturuluyor
    z_0 = [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1,
           0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
    z_1 = [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1,
           0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    z_2 = [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0,
           0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    z_3 = [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0,
           0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    z_4 = [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0,
           0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1]

    # n ve m değerleri oluşturuluyor
    # bir alttaki bölümde el ile n ve m değeri girmeyi ayarlanabilir
    # n = 16
    # m = 4

    """
    n ve m değerleri kullanıcıdan isteniyor
    bu değerlere göre T ve j oluşturuluyor
    """
    # print("n=16, 24, 32, 48, 64 olabilir\n m 2, 3, 4 olabilir")
    # n = int(input("n değerini giriniz:"))
    # m = int(input("m değerini giriniz:"))

    # sabit değer
    c = 2**(n) - 1

    T = 72
    j = 4

    key_0_list = []

    def key_generation(key_0, key_1, key_2, key_3, m, T):
        f = open("table_for_keys.txt", "w")
        f.write(
            "Round |      k_i+3     |      k_i+2     |      k_i+1     |      k_i+0   " + "\n")
        f.write("start" + " |" + (format(key_3, '016X')) + "|" + format(key_2,
                                                                        '016X') + "|" + format(key_1, '016X') + "|" + format(key_0, '016X') + "\n")

        key_0_n = key_0
        key_1_n = key_1
        key_2_n = key_2
        key_3_n = key_3
        if (m == 2):
            for i in range(T):
                temp1 = (key_1 >> 3) | (key_1 << (n - 3)) & c
                temp2 = (temp1 >> 1) | (temp1 << (n - 1)) & c
                temp3 = key_0_n ^ temp1
                temp4 = temp2 ^ temp3
                temp5 = temp4 ^ c ^ ((z_2[i % 62])) ^ 3
                key_next = key_0_n
                key_0_n = key_1
                key_1 = temp5
                key_0_list.append(key_next)
                # print ("key{} = {}".format(i, key_next)
            return key_0_n, key_1
        elif (m == 3):
            for i in range(T):
                temp1 = (key_2 >> 3) | (key_2 << (n - 3)) & c
                temp2 = (temp1 >> 1) | (temp1 << (n - 1)) & c
                temp3 = key_0_n ^ temp1
                temp4 = temp2 ^ temp3
                if (n == 24):
                    temp5 = temp4 ^ c ^ ((z_0[i % 62])) ^ 3
                elif (n == 32):
                    temp5 = temp4 ^ c ^ ((z_2[i % 62])) ^ 3
                elif (n == 48 | n == 64):
                    temp5 = temp4 ^ c ^ ((z_3[i % 62])) ^ 3
                key_next = key_0_n
                key_0_n = key_1
                key_1 = key_2
                key_2 = temp5
                key_0_list.append(key_next)
                # print ("key{} = {}".format(i, key_next)
            return key_0_list
        elif (m == 4):
            # print (key_0_n)
            # print ("key_0_n in hex",format(key_0_n, '016b'))
            for i in range(T):
                round_n = i
                # print(round_n)str(round_n)
                # print ("key{} = {}".format(i, key_0_n))
                # print ("key_0_n in hex",format(key_0_n, '016b'))
                temp1 = (key_3 >> 3) | (key_3 << (n - 3)) & c
                temp2 = key_1 ^ temp1
                temp3 = (temp2 >> 1) | (temp2 << (n - 1)) & c
                temp4 = key_0_n ^ temp2
                temp5 = temp3 ^ temp4
                if (n == 16):
                    temp6 = temp5 ^ c ^ ((z_0[i % 62])) ^ 3
                elif (n == 24):
                    temp6 = temp5 ^ c ^ ((z_1[i % 62])) ^ 3
                elif (n == 32):
                    temp6 = temp5 ^ c ^ ((z_3[i % 62])) ^ 3
                elif (n == 64):
                    temp6 = temp5 ^ c ^ ((z_4[i % 62])) ^ 3
                key_next = key_0_n
                key_0_n = key_1
                key_1 = key_2
                key_2 = key_3
                key_3 = temp6
                key_0_list.append(key_next)

                f.write(str(round_n) + "     |" + (format(key_3, '016X')) + "|" + format(key_2,
                        '016X') + "|" + format(key_1, '016X') + "|" + format(key_0_n, '016X') + "\n")

                # print ("key{} = {}".format(i, key_next)
            return key_0_list
        f.close()
    key_list = key_generation(key_0, key_1, key_2, key_3, m, T)

    # encryption
    text1_list = []
    text2_list = []
    for k in key_0_list:
        # plaintext = t1[0:3]t2[0:3]
        t1 = plainText_1
        t2 = plainText_2
        # print ("before texts 01 in hex",format(t1, '04x'), format(t2, "04X"))
        # print(key_0_list[i])
        crol_1 = (t1 << 1) + (t1 >> (n - 1)) & c
        crol_2 = (t1 << 2) + (t1 >> (n - 2)) & c
        crol_8 = (t1 << 8) + (t1 >> (n - 8)) & c
        tmp1 = crol_1 & crol_8
        tmp2 = t2 ^ tmp1
        tmp3 = tmp2 ^ crol_2
        tmp4 = tmp3 ^ k
        t2 = t1
        t1 = tmp4
        text1_list.append(t1)
        text2_list.append(t2)
        plainText_1 = t1
        plainText_2 = t2
        # return text1_list, text2_list
    print(format(text1_list[-1], '0X'),
          format(text2_list[-1], "0X"), "ciphertext hex",)
    print("********************************************************************")

    cipherText_1 = plainText_1
    cipherText_2 = plainText_2

    # key_generation(key_0, key_1, key_2, key_3, m)
    # enc(plainText_1, plainText_2, key_0)
    # a,b= enc(plainText_1, plainText_2, key_list, T)
    return cipherText_1, cipherText_2


cipherText_1 = 0
cipherText_2 = 0
IV_1 = 0x477f00c83731ec7b
IV_2 = 0x96b9fb0ffeb25ade
key_3 = 0x9ce73805171222e1  # most significant
key_2 = 0x67fd8bae41f85b4a
key_1 = 0xbde2432699ac471d
key_0 = 0x4a99b7f867a1886c  # least significant

round_n = 0
# pt_1 = IV_1 ^ 0
# pt_2 = IV_2 ^ 0
# print(pt_1)
# print(pt_2)
f = open("random_numbers_simon_10k.txt", "w")
a, b = SIMON(plainText_1=IV_1, plainText_2=IV_2, key_3=key_3,
             key_2=key_2, key_1=key_1, key_0=key_0)
x = format(a, '064b')
y = format(b, '064b')
f.write(str(x) + str(y) + "\n")
# for i in range(1):
#     a, b = SIMON(plainText_1=a, plainText_2=b, key_3=key_3,
#                  key_2=key_2, key_1=key_1, key_0=key_0)
#     z = format(a, '064b')
#     t = format(b, '064b')
#     f.write(str(z) + str(t) + "\n")
f.close()

f = open("table_for_detail.txt", "w")
f.write("SIMON Cipher 128-bit block, 256-bit key\n")
f.write("plaintext:" + (format(IV_1, '0X')) + " " + format(IV_2, '0X') + "\n")
f.write("key      :" + (format(key_3, '0X')) + " " + format(key_2,
        '0X') + " " + format(key_1, '0X') + " " + format(key_0, '0X') + "\n")
f.write("Round |  k_i+3  |  k_i+2  |  k_" + "\n")
# f.write(str(round_n) + "safad")
f.close()

# # while 1 == 1:
# #     a,b = SIMON(plainText_1 = a, plainText_2 = b)

# cipherText_1 = 0
# cipherText_2 = 0
# f = open("random_numbers_simon_20k.txt", "w")
# a, b = SIMON(plainText_1=IV_1, plainText_2=IV_2)
# x = format(a, '064b')
# y = format(b, '064b')
# f.write(str(x) + str(y) + "\n")
# for i in range(19999):
#     a, b = SIMON(plainText_1=a, plainText_2=b)
#     z = format(a, '064b')
#     t = format(b, '064b')
#     f.write(str(z) + str(t) + "\n")
# f.close()
