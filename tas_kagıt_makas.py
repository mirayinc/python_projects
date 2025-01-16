import random

user_wins = 0
comp_wins = 0
secenekler = ["taş","kağıt", "makas"]

while True:
    user_input = input("Seç TAŞ-KAĞIT-MAKAS? veya p ile pes et: ").lower()
    if user_input == "p":
        break
    if user_input not in secenekler:
        print("Seçim yapmalısın..")
        continue
    random_number = random.randint(0,2)
    # taş 0, kağıt 1 ve makas 2
    comp_sec = secenekler[random_number]
    print("Bilgisayar", comp_sec, "seçti.")
    
    if user_input == comp_sec:
        print("Aynı seçimi seçtiniz. \nKazanan yok.")
        continue
    
    elif user_input == "taş" and comp_sec == "makas":
        print("Sen Kazandın!")
        user_wins += 1
        continue
    
    elif user_input == "makas" and comp_sec == "kağıt":
        print("Sen Kazandın!")
        user_wins += 1
        continue
    
    elif user_input == "kağıt" and comp_sec == "taş":
        print("Sen Kazandın!")
        user_wins += 1
        continue
    else:
        print("Kaybettin..")
        comp_wins +=1
        
    
     
print("Sen", user_wins, "kere ve Bilgisayar", comp_wins, "kere kazandı.")
print("Görüşürüz!!")