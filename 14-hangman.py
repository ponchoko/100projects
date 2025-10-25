def main():
    word = "chick" #only place to replace word
    current = "_____"
    while current != word:
        guess = input("Guess a letter. ")
        if guess in word:
            print("Correct guess!") 
        else:
            print("Incorrect guess.")

        for i in range(len(word)):
            if guess == word[i]:
                current = current[:i] + guess + current[i+1:]
        if current == word:
            print("You got it. The word was " + word)
            exit
        else:
            print("Current state: " + current)


main()
