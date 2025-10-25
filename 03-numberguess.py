import random

def main():
    x,y = userinputs()
    print(x)
    print(y)
    val = random.randint(int(x),int(y))
    timesguessed = guess(val)
    print("You guess it right. The answer is ", val, "and it took you", timesguessed, "tries.")
       
def userinputs():
    low = input("Enter the lower bound: ")
    high = input("Enter the upper bound: ")
    return low, high

def guess(val):
    guessed = 0
    while True:
        n = input("What is your guess?")
        if int(n) > val:
            print("Your guess is too high. Try again.")
            guessed = guessed + 1
            continue
        elif int(n) < val:
            print("Your guess is too low. Try again.")
            guessed = guessed + 1
            continue
        else:
            return guessed
    
        
main()
    


