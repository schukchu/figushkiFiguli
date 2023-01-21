cod = str("8"*86)
while cod.count("8888")>=1 or cod.count("1111")>=1:
    if cod.count("1111")>=1:
        cod = cod.replace("1111", "8", 1)
    else:
        cod = cod.replace("8888", "11", 1)
print(cod)
