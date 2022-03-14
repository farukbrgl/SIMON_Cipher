#!/usr/bin/env python
# coding: utf-8

"""
SIMON Hafif Blok Şifreleyicisinin Python ile Gerçeklenmesi
Orijinal makaleye https://eprint.iacr.org/2013/404 adresinden ulaşabilirsiniz.
"""
import argparse


class Simon:
    z_const = [[1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0,
                0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1,
                0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0],
               [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0,
                0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1,
                1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0,
                1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0,
                0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
               [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0,
                1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0,
                1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
               [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0,
                1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0,
                1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1]]

    def __init__(self, plaintext, key):
        self.plaintext = plaintext
        self.key = key
        self.key_list = []
        # these constant can be changed at different versions of Simon
        self.n_word_size = 64
        self.m_key_words = 4
        self.c_const = 2**self.n_word_size - 1
        self.t_round = 72
        self.j_number = 4

    def key_generation(self, key, m_key_words, t_round):
        key_0 = int(self.key[0:
                    self.n_word_size - 1], 16)
        key_1 = int(self.key[self.n_word_size:
                    2 * self.n_word_size - 1], 16)
        key_2 = int(self.key[2 * self.n_word_size:
                    3 * self.n_word_size - 1], 16)
        key_3 = int(self.key[3 * self.n_word_size:
                    4 * self.n_word_size - 1], 16)
        for i in range(self.t_round):
            temp1 = (key_3 >> 3) | (
                key_3 << (self.n_word_size - 3)) & self.c_const
            temp2 = key_1 ^ temp1
            temp3 = (temp2 >> 1) | (
                temp2 << (self.n_word_size - 1)) & self.c_const
            temp4 = key_0 ^ temp2
            temp5 = temp3 ^ temp4
            temp6 = temp5 ^ self.c_const ^ ((self.z_const[4][i % 62])) ^ 3
            key_next = key_0
            key_0 = key_1
            key_1 = key_2
            key_2 = key_3
            key_3 = temp6
            self.key_list.append(key_next)
        return self.key_list

    def encryption(self, plaintext):
        for k in self.key_list:
            t1 = int(self.plaintext[0: self.n_word_size - 1], 16)
            t2 = int(
                self.plaintext[self.n_word_size: 2 * self.n_word_size - 1], 26)
            crol_1 = (t1 << 1) + (t1 >> (self.n_word_size - 1)) & self.c_const
            crol_2 = (t1 << 2) + (t1 >> (self.n_word_size - 2)) & self.c_const
            crol_8 = (t1 << 8) + (t1 >> (self.n_word_size - 8)) & self.c_const
            tmp1 = crol_1 & crol_8
            tmp2 = t2 ^ tmp1
            tmp3 = tmp2 ^ crol_2
            tmp4 = tmp3 ^ k
            t2 = t1
            t1 = tmp4
            cipherText_1 = t1
            cipherText_2 = t2
        return cipherText_1, cipherText_2

    def table_generator(self):
        print("Table of Every Steps for One Round")
        print("**********************************")
        print("Inputs")
        print("plainText_1   ")
        plaintext = str(self.plaintext)
        print(plaintext)

    def __repr__(self):
        # return "I am an instance of MyClass at address "+hex(id(self))
        return self.cipherText_1, self.cipherText_2


def main(name, iteration, random):
    random_iv = open("random_iv_" + str(random), "r")
    # print(random_iv.readlines())
    # with open("./results/random_iv") as file_in:
    #     lines = []
    # for line in file_in:
    #     lines.append(line)
    # print(type(int(lines[1])))
    random_list = random_iv.readlines()
    plaintext = random_list[0][0:32]
    key = random_list[1][0:64]
    # print((pt_1))
    # hex_pt_1 = hex(pt_1)
    # hex_pt_2 = hex(pt_2)
    # hex_k_3 = hex(k_3)
    # hex_k_2 = hex(k_2)
    # hex_k_1 = hex(k_1)
    # hex_k_0 = hex(k_0)

    # plainText_1_n = int(hex_pt_1, 16)
    # plainText_2_n = int(hex_pt_2, 16)

    # pt_1 = IV_1 ^ 0
    # pt_2 = IV_2 ^ 0
    # print(pt_1)
    # print(pt_2)
    f = open(name, "w")
    a, b = Simon(plaintext=plaintext, key=key)
    x = format(a, '064b')
    y = format(b, '064b')
    f.write(str(x) + str(y) + "\n")
    for i in range(iteration - 1):
        a, b = Simon.SIMON(plaintext=a, key=b)
        z = format(a, '064b')
        t = format(b, '064b')
        f.write(str(z) + str(t) + "\n")
    f.close()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--iter", required=True, help="num of iterations")
    ap.add_argument("-r", "--rand", required=True, help="num of random iv")
    ap.add_argument("-l", "--name", required=True, help="file address")
    # ap.add_argument("-pt1","--plainText_1",required = True, help = "plaintext 1")
    # ap.add_argument("-pt2","--plainText_2",required = True, help = "plaintext 2")
    # ap.add_argument("-k3","--key_3",required = True, help = "key 3")
    # ap.add_argument("-k2","--key_2",required = True, help = "key 2")
    # ap.add_argument("-k1","--key_1",required = True, help = "key 1")
    # ap.add_argument("-k0","--key_0",required = True, help = "key 0")
    args = vars(ap.parse_args())
    main(args["name"], int(args["iter"]), int(args["rand"]))
