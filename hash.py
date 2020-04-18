def hashStr(y, str):
    for c in str:
        y = y + dict[c]
        y = y * 521
        y = y % 10000
        y = y + 450
        y = y % 967

    return y

dict = {
        'A': 23,
        'B': 47,
        'I': 397,
        'L': 507,
        'O': 581,
        'P': 635,
        'R': 687,
        'U': 763,
        'Y': 901,
        '0': 405,
        '1': 73
       }

for x in [734]:
    v1 = hashStr(x, "PAYBOB100")
    v2 = hashStr(x, "BILLBOB1000")
    v3 = hashStr(x, "PAYROB1000")

    print("v1:", v1, "v2:", v2, "v3:", v3)
