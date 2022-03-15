import secrets
for k in range(2):
    f = open("random_iv_" + str(k), "w")
    for i in range(6):
        random_iv_line = (secrets.token_hex(32))
        print(type(random_iv_line))
        # if len(random_iv_line) != 20:
        #     pass
        # else:
        #     print((random_iv_line))
        f.write((random_iv_line) + "\n")
    f.close()
