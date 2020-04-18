def decrypt(l):
    x = len(l)
    i = 0
    j = start
    while i < x:
        decrypted.append(l[j])
        j += 13
        if j >= x:
            j -= x
        i += 1

str = "TGPRGWTADEKI HI6OYNODONAT ES4LOCIINTB} FC4LURSDTHO_ LO1IRYAEEIU_ AM{NOPBAVNT_"
l = list(str)
decrypted = []
start = 0
decrypt(l)
str = ''.join(decrypted)
print(str)
