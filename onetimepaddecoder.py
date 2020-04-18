def str_xor(str1, str2):
    str = [chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2)]
    return ''.join(str)

def hex_xor(str1, str2):
    res = []

    for a, b in zip(str1, str2):
        x = format((int(a, 16) ^ int(b, 16)), 'x')
        res.append(x)

    return ''.join(res)

def hex_to_str(str):
    return bytes.fromhex(str).decode('utf-8')

def encrypt(dec, key):
    enc = []
    dec = dec.lower()

    for a, b in zip(dec, key):
        c = (ord(a) - ord('a') + 1) + (ord(b) - ord('a') + 1)
        if c > 26:
            c = c - 26
        c = c + ord('a') - 1
        enc.append(chr(c))

    return ''.join(enc)

def decrypt(enc, key):
    dec = []
    enc = enc.lower()

    for a, b in zip(enc, key):
        c = ord(a) - ord(b)
        if c <= 0:
            c = c + 26
        c = c + ord('a') - 1
        dec.append(chr(c))

    return ''.join(dec)

s1 = "LpaGbbfctNiPvwdbjnPuqolhhtygWhEuafjlirfPxx" # l
s2 = "WdafvnbcDymxeeulWOtpoofnilwngLhblUfecvqAxs"
s3 = "UijMltDjeumxUnbiKstvdrVhcoDasUlrvDypegublg"
s4 = "LpaAlrhGmjikgjdmLlcsnnYmIsoPcglaGtKeQcemiu"
s5 = "LpaDohqcOzVbglebjPdTnoTzbyRbuwGftflTliPiqp"

k = "rhvnwynxzttsmipsvgkzyzpyokjsnozwxaxzddlhwo"

print(decrypt(s1, k))
print(decrypt(s2, k))
print(decrypt(s3, k))
print(decrypt(s4, k))
print(decrypt(s5, k))
