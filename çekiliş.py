import random

def cekilis():
    katılımcılar =[]
    while True:
        isim = input("Katılımcı isimlerini girin çıkmak için 'q' basın.")
        if isim.lower() == "q":
            break
        katılımcılar.append(isim)
        if not katılımcılar: #burada katılımcı listesi boşsa false olur, not false true demek. true olursa kod bloğu çalışır.
            print("Katıılımcı adı girmeniz gerekiyor.")
            return
    kazanan = random.choice(katılımcılar)
    print(f"Kazanan katılımcı {kazanan}")
    
if __name__ == "__main__":
    cekilis()
