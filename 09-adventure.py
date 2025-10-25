def main():
    result1 = stage1()
    if result1 == 1:
        stage2()
    elif result1 == 2:
        print("You encountered a monster! You Lose!")
        exit()
    
    result2 = stage2()
    if result2 == 1:
        print("You found a treasure! You Win)")
        exit()
    if result2 == 2:
        print("You encountered a monster! You Lose!")
        exit()
    
def stage1():
    return int(input("Choose your path \n 1. Enter the dark cave \n 2. Follow the path through the forest."))

def stage2():
    return int(input("Choose your path \n 1.Open the chest \n 2. Follow the path through the forest."))
    
main()