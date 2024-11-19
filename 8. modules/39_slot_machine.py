import random

symbols = ['🍒','🍇', '🍉', '7️⃣ ']

def play():

    while True: 
        for _ in range(5):
            results=(random.choices(symbols, k=3))

            print("|".join(results))

            if all(i =='7️⃣ ' for i in results):
                print ("Jackpot! 💰")

            else:  
                print ('Thanks for playing!')

        play_again=input('Do you want to play again? (Y/N)')
        if play_again != 'Y':
            print ("Goodbye! Thanks for playing!")
            break


play()