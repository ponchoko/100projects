import random

def main():
    while True:
        guess = int(input("Select your move - 1 for Rock, 2 for Paper, 3 for Scissors): "))
        comp = random.randint(1,3)
        if guess == 1:
            if comp == 3:
                print("you lose")
                continue
            elif comp == 2:
                print("you win")
                continue
            else:
                print("its a tie")
                continue            
        elif guess == 2:
            if comp == 1:
                print("you lose")
                continue
            elif comp == 1:
                print("you win")
                continue
            else:
                print("its a tie") 
                continue           
        elif guess == 3:
            if comp == 1:
                print("you lose")
                continue
            elif comp == 2:
                print("you win")
                continue
            else:
                print("its a tie")
                continue
    
main()




            

