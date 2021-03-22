

def ortakIslemler(deger,kelime):
    a = deger.lstrip(kelime)
    a = a.strip()
    a = a.split(",")
    return a[0]