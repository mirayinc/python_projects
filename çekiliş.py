import random

def cekilis_yap():
    katilimcilar = []
    while True:
        isim = input("Katılımcı ismini gir (bitirmek için 'q' tuşuna bas): ")
        if isim.lower() == 'q':
            break
        katilimcilar.append(isim)

    if not katilimcilar:
        print("Hiç katılımcı yok, çekiliş yapılamaz!")
        return

    kazanan = random.choice(katilimcilar)
    print(f"🎉 Kazanan: {kazanan} 🎉")

if __name__ == "__main__":
    cekilis_yap()
