import random

kelimeler = [
    {"fransızca": "de", "türkçe": "…'in, …'den"},
    {"fransızca": "la", "türkçe": "the (belirtme artikeli, dişil)"},
    {"fransızca": "et", "türkçe": "ve"},
    {"fransızca": "le", "türkçe": "the (belirtme artikeli, eril)"},
    {"fransızca": "à", "türkçe": "…'a, …'e"},
    {"fransızca": "être", "türkçe": "olmak"},
    {"fransızca": "en", "türkçe": "…'de, …'da, içinde"},
    {"fransızca": "avoir", "türkçe": "sahip olmak"},
    {"fransızca": "que", "türkçe": "ki"},
    {"fransızca": "pour", "türkçe": "için"},
    {"fransızca": "dans", "türkçe": "içinde"},
    {"fransızca": "ce", "türkçe": "bu (eril)"},
    {"fransızca": "il", "türkçe": "o (erkek)"},
    {"fransızca": "qui", "türkçe": "kim"},
    {"fransızca": "ne", "türkçe": "…me/ma (olumsuzluk)"},
    {"fransızca": "sur", "türkçe": "üstünde"},
    {"fransızca": "se", "türkçe": "kendini, kendisine"},
    {"fransızca": "pas", "türkçe": "değil"},
    {"fransızca": "plus", "türkçe": "daha fazla"},
    {"fransızca": "pouvoir", "türkçe": "yapabilmek"},
    {"fransızca": "par", "türkçe": "tarafından, ile"},
    {"fransızca": "je", "türkçe": "ben"},
    {"fransızca": "avec", "türkçe": "ile"},
    {"fransızca": "tout", "türkçe": "her şey, tüm"},
    {"fransızca": "faire", "türkçe": "yapmak"},
    {"fransızca": "son", "türkçe": "onun (eril)"},
    {"fransızca": "mettre", "türkçe": "koymak"},
    {"fransızca": "autre", "türkçe": "diğer"},
    {"fransızca": "nous", "türkçe": "biz"},
    {"fransızca": "mais", "türkçe": "ama"},
    {"fransızca": "comme", "türkçe": "gibi"},
    {"fransızca": "ou", "türkçe": "veya, ya da"},
    {"fransızca": "si", "türkçe": "eğer"},
    {"fransızca": "leur", "türkçe": "onların"},
    {"fransızca": "y", "türkçe": "orada, oraya"},
    {"fransızca": "dire", "türkçe": "demek, söylemek"},
    {"fransızca": "elle", "türkçe": "o (kadın)"},
    {"fransızca": "devoir", "türkçe": "zorunda olmak"},
    {"fransızca": "avant", "türkçe": "önce"},
    {"fransızca": "deux", "türkçe": "iki"},
    {"fransızca": "même", "türkçe": "aynı, bile"},
    {"fransızca": "prendre", "türkçe": "almak"},
    {"fransızca": "aussi", "türkçe": "ayrıca, da"},
    {"fransızca": "celui", "türkçe": "şu (eril)"},
    {"fransızca": "donner", "türkçe": "vermek"},
    {"fransızca": "bien", "türkçe": "iyi"},
    {"fransızca": "où", "türkçe": "nerede"},
    {"fransızca": "fois", "türkçe": "defa, kez"},
    {"fransızca": "vous", "türkçe": "siz"},
    {"fransızca": "nouveau", "türkçe": "yeni (eril)"},
    {"fransızca": "aller", "türkçe": "gitmek"},
    {"fransızca": "entre", "türkçe": "arasında"},
    {"fransızca": "premier", "türkçe": "birinci (eril)"},
    {"fransızca": "vouloir", "türkçe": "istemek"},
    {"fransızca": "déjà", "türkçe": "zaten, çoktan"},
    {"fransızca": "grand", "türkçe": "büyük (eril)"},
    {"fransızca": "mon", "türkçe": "benim (eril)"},
    {"fransızca": "me", "türkçe": "beni, bana"},
    {"fransızca": "moins", "türkçe": "daha az"},
    {"fransızca": "aucun", "türkçe": "hiçbir (eril)"},
    {"fransızca": "lui", "türkçe": "ona (eril)"},
    {"fransızca": "temps", "türkçe": "zaman"},
    {"fransızca": "savoir", "türkçe": "bilmek"},
    {"fransızca": "falloir", "türkçe": "gerekli olmak"},
    {"fransızca": "voir", "türkçe": "görmek"},
    {"fransızca": "quelque", "türkçe": "biraz, birkaç"},
    {"fransızca": "sans", "türkçe": "…siz, olmadan"},
    {"fransızca": "raison", "türkçe": "sebep"},
    {"fransızca": "notre", "türkçe": "bizim"},
    {"fransızca": "dont", "türkçe": "…dığı (ilgi zamiri)"},
    {"fransızca": "non", "türkçe": "hayır"},
    {"fransızca": "an", "türkçe": "yıl"},
    {"fransızca": "monde", "türkçe": "dünya"},
    {"fransızca": "jour", "türkçe": "gün"},
    {"fransızca": "monsieur", "türkçe": "bay"},
    {"fransızca": "venir", "türkçe": "gelmek"},
    {"fransızca": "pendant", "türkçe": "sırasında"},
    {"fransızca": "très", "türkçe": "çok"},
    {"fransızca": "juste", "türkçe": "sadece, adil"},
    {"fransızca": "encore", "türkçe": "henüz, daha"},
    {"fransızca": "trouver", "türkçe": "bulmak"},
    {"fransızca": "rendre", "türkçe": "geri vermek/döndürmek"},
    {"fransızca": "homme", "türkçe": "adam"},
    {"fransızca": "femme", "türkçe": "kadın"},
    {"fransızca": "suite", "türkçe": "devam, takip"},
    {"fransızca": "voilà", "türkçe": "işte"},
    {"fransızca": "vie", "türkçe": "hayat"},
    {"fransızca": "depuis", "türkçe": "…den beri"},
    {"fransızca": "peu", "türkçe": "az"},
    {"fransızca": "sous", "türkçe": "altında"},
    {"fransızca": "chaque", "türkçe": "her"},
    {"fransızca": "place", "türkçe": "yer"},
    {"fransızca": "dernier", "türkçe": "son (eril)"},
    {"fransızca": "comprendre", "türkçe": "anlamak"},
    {"fransızca": "quel", "türkçe": "hangi (eril)"},
    {"fransızca": "après", "türkçe": "sonra"},
    {"fransızca": "heure", "türkçe": "saat"},
    {"fransızca": "beaucoup", "türkçe": "çok (miktar)"},
    {"fransızca": "aujourd'hui", "türkçe": "bugün"},
    {"fransızca": "maintenant", "türkçe": "şimdi"}
]


# Quiz fonksiyonu
def quiz_user(kelimeler):
    while True:  # Tekrar oynama seçeneği için döngü
        random.shuffle(kelimeler)  # Kelimeleri karıştırmak için
        score = 0  # Doğru sayacı
        wrong_answers = []  # Yanlış cevaplar için liste

        print("\n--- Fransızca-Türkçe Testi Başlıyor! ---\n")
        print("Not: Testi bitirmek isterseniz 'çık' yazabilirsiniz.\n")

        for kelime in kelimeler:
            print(f"'{kelime['fransızca']}' kelimesinin Türkçe çevirisi nedir?")
            user_answer = input("Senin cevabın: ").strip().lower()  # Kullanıcıdan cevap al ve normalize et

            # Kullanıcı çıkmak isterse quizi bitir
            if user_answer == "çık":
                print("\nTest sonlandırıldı.")
                print(f"O ana kadar topladığın puan: {score}/{len(kelimeler)}\n")
                return  # Ana quiz döngüsünden çık

            correct_answer = kelime['türkçe'].lower()  # Doğru cevabı normalize et

            if user_answer == correct_answer:
                print("✅ DOĞRU!\n")
                score += 1
            else:
                print(f"❌ YANLIŞ! Doğru cevap: {kelime['türkçe']}.\n")
                wrong_answers.append(kelime)  # Yanlış cevapları listeye ekle

        # Test sonuçları
        print(f"Testi tamamladın. Puanın: {score}/{len(kelimeler)}\n")

        # Yanlış cevapları göster
        if wrong_answers:
            print("--- Yanlış Yaptığın Sorular ---")
            for kelime in wrong_answers:
                print(f"{kelime['fransızca']} ➡ {kelime['türkçe']}")
            print()

        # Kullanıcıya tekrar oynamak isteyip istemediğini sor
        play_again = input("Tekrar oynamak ister misin? (evet/hayır): ").strip().lower()
        if play_again != "evet":
            print("Teşekkürler! Görüşmek üzere.")
            break

# Quiz'i çalıştır
quiz_user(kelimeler)