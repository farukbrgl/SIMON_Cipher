#!/usr/bin/env python
# coding: utf-8

"""
SIMON Hafif Blok Şifreleyicisinin Python ile Gerçeklenmesi
Orijinal makaleye https://eprint.iacr.org/2013/404 adresinden ulaşabilirsiniz.
"""

"""
plaintext, ciphertext ve key oluşturuldu
encryption ve decryption işlemlerinin ikisi de gerçekleştiriliyor
bunlar orijinal makaledeki n=16, m=4 durumunda verilen başlangıç vektörleri
sonuçların doğruluğunu makaleden inceleyebilirsiniz
farklı boyuttaki şifreleyici için farklı değerler vermelisiniz
"""
def SIMON(plainText_1 = 0x74206e69206d6f6f, plainText_2 = 0x6d69732061207369, key_3 = 0x1f1e1d1c1b1a1918, key_2 = 0x1716151413121110, key_1 = 0x0f0e0d0c0b0a0908, key_0 = 0x0706050403020100, n = 64, m = 4):
    # plainText_1 = 0x6373656420737265 #most significant
    # plainText_2 = 0x6c6c657661727420 #least significant
    print (format(plainText_1, '0X'), format(plainText_2, "0X"), "plaintexts in start in hex")

    # cipherText_2 = 0x49681b1e1e54fe3f
    # cipherText_1 = 0x65aa832af84e0bbc
    # print (format(cipherText_1, '016X'), format(cipherText_2, "016X"), "ciphertexts in start in hex")

    # key_3 = 0x1918 #most significant
    # key_2 = 0x121110
    # key_1 = 0x0f0e0d0c0b0a0908
    # key_0 = 0x0706050403020100 #least significant
    print (format(key_3, '0x'), format(key_2, "0X"), format(key_1, "0X"), format(key_0, "0X"),"keys in hex")

    #z sabitleri oluşturuluyor
    z_0 = [1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0]
    z_1 = [1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0]
    z_2 = [1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1]
    z_3 = [1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1,1,1,1]
    z_4 = [1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1]


    #n ve m değerleri oluşturuluyor
    #bir alttaki bölümde el ile n ve m değeri girmeyi ayarlanabilir
    # n = 16
    # m = 4

    """
    n ve m değerleri kullanıcıdan isteniyor
    bu değerlere göre T ve j oluşturuluyor
    """
    # print("n=16, 24, 32, 48, 64 olabilir\n m 2, 3, 4 olabilir")
    # n = int(input("n değerini giriniz:"))
    # m = int(input("m değerini giriniz:"))

    ##sabit değer
    c = 2**(n) - 1


    T = 0
    j = 0
    if (n == 16 and m == 4):
        T = 32
        j = 0
    elif (n == 24 and m == 3):
        T = 36
        j = 0
    elif (n == 24 and m == 4):
        T = 36
        j = 1
    elif (n == 32 and m == 3):
        T = 42
        j = 2
    elif (n == 32 and m == 4):
        T = 44
        j = 3
    elif (n == 48 and m == 2):
        T = 52
        j = 2
    elif (n == 48 and m == 3):
        T = 54
        j = 3
    elif (n == 64 and m == 2):
        T = 68
        j = 2
    elif (n == 24 and m == 3):
        T = 69
        j = 3
    elif (n == 64 and m == 4):
        T = 72
        j = 4
    else:
        print("yanlış değer girdiniz\ndevam etmeyiniz")


    key_0_list= []
    def key_generation(key_0, key_1, key_2, key_3, m, T):
        key_0_n = key_0
        key_1_n = key_1
        key_2_n = key_2
        key_3_n = key_3
        if (m == 2):
            for i in range(T):
                temp1 = (key_1 >> 3)|(key_1 << (n - 3)) & c
                temp2 = (temp1 >> 1)|(temp1 << (n - 1)) & c
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
                temp1 = (key_2 >> 3)|(key_2 << (n - 3)) & c
                temp2 = (temp1 >> 1)|(temp1 << (n - 1)) & c
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
                # print ("key{} = {}".format(i, key_0_n))
                # print ("key_0_n in hex",format(key_0_n, '016b'))
                temp1 = (key_3 >> 3)|(key_3 << (n - 3)) & c
                temp2 = key_1 ^ temp1
                temp3 = (temp2 >> 1)|(temp2 << (n - 1)) & c
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
                # print ("key{} = {}".format(i, key_next)
            return key_0_list

    key_list =key_generation(key_0, key_1, key_2, key_3, m, T)

    ### encryption
    text1_list= []
    text2_list= []
    for k in key_0_list:
        ### plaintext = t1[0:3]t2[0:3]
        t1 = plainText_1
        t2 = plainText_2
        # print ("before texts 01 in hex",format(t1, '04x'), format(t2, "04X"))
        # print(key_0_list[i])
        crol_1 = (t1 << 1) + (t1 >> (n-1)) & c
        crol_2 = (t1 << 2) + (t1 >> (n-2)) & c
        crol_8 = (t1 << 8) + (t1 >> (n-8)) & c
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
    print (format(text1_list[-1], '0X'), format(text2_list[-1], "0X"), "ciphertext hex",)
    print ("********************************************************************")



    """
    ### decryption
    cp_text1_list= []
    cp_text2_list= []
    # def enc(plainText_1, plainText_2, key_0, T):
    for k in reversed(key_0_list):
        #plaintext = t1[0:3]t2[0:3]
        ct1 = cipherText_1
        ct2 = cipherText_2
        # print ("before texts 01 in hex",format(t1, '04x'), format(t2, "04X"))
        # print(key_0_list[i])
        crol_1 = (ct1 << 1) + (ct1 >> (n-1)) & c
        crol_2 = (ct1 << 2) + (ct1 >> (n-2)) & c
        crol_8 = (ct1 << 8) + (ct1 >> (n-8)) & c
        tmp1 = crol_1 & crol_8
        tmp2 = ct2 ^ tmp1
        tmp3 = tmp2 ^ crol_2
        tmp4 = tmp3 ^ k
        ct2 = ct1
        ct1 = tmp4

        #print(key_0)
        # t1 = tmp
        cp_text1_list.append(ct1)
        cp_text2_list.append(ct2)
        # print(t1, t2)

        # print(text1_list)
        # print(text2_list)
        # print("key {} = {}".format(key_0_list.index(),k))
        cipherText_1 = ct1
        cipherText_2 = ct2
    # print(t1,t2)
        # return text1_list, text2_list
    print (format(cp_text2_list[-1], '016X'), format(cp_text1_list[-1], "016X"), "plaintext hex")
    """
    cipherText_1 = plainText_1
    cipherText_2 = plainText_2

    # key_generation(key_0, key_1, key_2, key_3, m)
    # enc(plainText_1, plainText_2, key_0)
    # a,b= enc(plainText_1, plainText_2, key_list, T)
    return cipherText_1, cipherText_2

cipherText_1 = 0
cipherText_2 = 0
IV_1 = 0x74206e69206d6f6f
IV_2 = 0x6d69732061207369
# pt_1 = IV_1 ^ 0
# pt_2 = IV_2 ^ 0
# print(pt_1)
# print(pt_2)
f = open("random_numbers.txt", "a")
a,b = SIMON(plainText_1 = IV_1, plainText_2 = IV_2)
f.write(str(a)+str(b))
# for i in range (10000):
#     a,b = SIMON(plainText_1 = a, plainText_2 = b)
# while 1 == 1:
#     a,b = SIMON(plainText_1 = a, plainText_2 = b)
