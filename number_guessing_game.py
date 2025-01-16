import random
top_of_range = input("Bir sayı girin: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <=0:
        print("Lütfen 0'dan büyük bir sayı girin")
        quit()
else:
    print("Bir sayı girmeliydiniz.")
    quit()        
        
#random.randrange(-1,11)
#(start,stop) 11 koyarsan 11'i değil max 10u alır. 
# start koymazsan sadece stop üretecek.
#ama random_number = random.randint(-1,11) #11 dahil

random_number = random.randit(0,top_of_range)
guesses = 0
while True:
    guesses+=1
    user_guess = input("Bir tahmin yap: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Lütfen sayı girin.")
        continue
    
    if user_guess == random_number:
        print("Doğru Bildin!!")
        break
    
    elif user_guess > random_number:
        print("Tekrar denemelisin...")
        print("Daha düşük bir sayı söylemelisin.")
    else:
        print("Tekrar denemelisin...")
        print("Daha büyük bir sayı söylemelisin.")
        
print("Sayıyı", guesses,"denemede buldun.")
