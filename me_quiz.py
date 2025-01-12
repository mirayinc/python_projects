

sorular =[
    {"prompt" : "Göz rengim ne?",
     "options": ["A.Mavi", "B.Kahverengi", "C.Ela", "D.Yeşil"],
     "answer": "D"
     },
    {"prompt" : "En sevdiğim renk ne?",
    "options":["A.Turuncu", "B.Mor", "C.Yeşil", "D.Siyah"],
    "answer": "C"
    },
    {"prompt": "First celebrity crushım kim?",
    "options": ["A.Charles Leclerc", "B.Theo James", "C.Donald Trump", "D.Tom Hardy"],
    "answer": "B"
    },
    {"prompt" :"Çocukken büyüyünce ne olmak istiyordum?",
    "options":["A.Tek boynuzlu atı olan uzay savaşçısı prenses şeftali","B.Doktor", "C.Avukat", "D.Vali"],
    "answer": "D"
    },
    {"prompt":"Friendste en sevdiğim karakter kimdi?",
    "options":["A.Chandler","B.Rachel","C.Phoebe", "D.Joey"],
    "answer": "C"
    },
    {"prompt" :"En sevdiğim çikolata?",
    "options":["A.Karam","B.Ferrero Rocher", "C.Oreolu Milka", "D.Dido"],
    "answer": "B"
    },
    {"prompt" :"Çok istediğim hayvan?",
    "options":["A.At","B.Kuş", "C.Köpek", "D.Kedi"],
    "answer": "A"
    },
    {"prompt" :"Hangi enstürmanı çalabildiğimi sanıyorum?",
    "options":["A.Keman","B.Piyano", "C.Gitar", "D.Bağlama"],
    "answer": "A"
    },
    {"prompt" :"Hangi tür film izlemekten hoşlanırım?",
    "options":["A.Korku","B.Macera", "C.Gerilim", "D.Romantik Komedi"],
    "answer": "D"
    },
    {"prompt" :"Hangi mevsim favorim?",
    "options":["A.İLkbahar","B.Yaz", "C.Sonbahar", "D.Kış"],
    "answer": "D"
    }
]

def do_you_even_know_my_name(sorular):
    score = 0
    for soru in sorular:
        print(soru["prompt"])
        for secenekler in soru["options"]:
            print(secenekler)
        answer = input("Cevabınızı girin(A,B,C veya D):  ")
        if answer == soru["answer"]:
            print("Doğru!\n")  
            score += 10
        else:
            print("Yanlış! Aşk olsun... \nDoğru cevap:", soru["answer"], "\n")
    if score >= 80:
        sonuc = "Beni Seviyorsunnn <3"
    elif score >= 50:
        sonuc="Beni tanıyorsunn"
    else:
        sonuc="Adımı biliyor musun bari??"
        
    return print("Skorun", score, sonuc)
            
do_you_even_know_my_name(sorular)