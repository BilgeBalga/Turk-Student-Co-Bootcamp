# 1)

#kullanıcıdan iki sayı alarak bu sayıları toplayan bir program kodu
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# Sayıları topla
toplam = sayi1 + sayi2

# Sonucu ekrana yazdır
print("Sayıların toplamı:", toplam)

# 2)
# 1'den 100'e kadar olan sayıları topla
toplam = sum(range(1, 101))

# Sonucu ekrana yazdır
print("1'den 100'e kadar olan sayıların toplamı:", toplam)

# 3)
# Asal sayı kontrolü yapan fonksiyon
def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True

# Kullanıcıdan sayı al
sayi = int(input("Bir sayı girin: "))

# Sonucu ekrana yazdır
if asal_mi(sayi):
    print(sayi, "bir asal sayıdır.")
else:
    print(sayi, "asal bir sayı değildir.")


# 4)
# Bir dizideki elemanların tekrar edip etmediğini kontrol eden kod.
def tekrar_kontrol(dizi):
    elemanlar = set()
    for eleman in dizi:
        if eleman in elemanlar:
            print(f"{eleman} dizide birden fazla kez bulunuyor.")
        else:
            elemanlar.add(eleman)

# Örnek kullanım
dizi = [1, 2, 3, 4, 5, 1, 3]
tekrar_kontrol(dizi)
