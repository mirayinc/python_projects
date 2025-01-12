
#hangman game

import random

kelimeler = ["kimya","matematik","biyoji", "fizik", "edebiyat", "müzik"]

secilen_kelime = random.choice(kelimeler)
#kelimeler listesinden random bir tanesini seçecek
kelime = [ "_" for _ in secilen_kelime]
#seçilen kelimenin her harfi için _ oluşturacak

#print(kelime_ne)
#buraya kadar olan kısmı doğru yaptık mı anlamak için

giriş = 8

while giriş > 0 and "_" in kelime:
    print("\n" + " ".join(kelime))
    tahmin = input("Bir harf tahmin et: ").lower()
    #burada lower yazmıştım-hata alır. lower yazılınca referans verilir
    #lower fonksiyonuna çağrı yapmak için lower() olmalı
    if tahmin in secilen_kelime:
        for index, harf in enumerate(secilen_kelime):
            if harf == tahmin:
                kelime[index] = tahmin #harf varsa gösterilir
    else:
        print("Bu harf kelimenin içinde yok")
        giriş -= 1
        
if "_" not in kelime:
    print("Kelimeyi bildin!!")
    print(" ".join(kelime))
    print("BAŞARDIN!!!")
else:
    print("Tahmin hatalı. Bulman gereken kelime: " + secilen_kelime)
