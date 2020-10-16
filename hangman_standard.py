#!/bin/env python3

def hangman(word="", guess="", foo=[], tries=1, guessed=False):
    user_input = ""
    if not guessed and word != "" and tries > 0:
        user_input = input("Please insert the character ")
        print("Remaining tries: ", tries)

    if word == "":
        return hangman( \
            input("Please insert THE word: "), \
            "", \
            [], \
            int(input("\n"*100 + "Number of tries: ")), \
            False \
        )
    
    if len(user_input) > 1:
        if word == user_input:
            return "WIN"
        hangman(word, guess, foo, tries-1, guessed)
    
    if guessed:
        return "WIN"
    
    if tries <= 0:
        return "LOST"

    print("Current status:")
    for i in word:
        print("?" if i not in (guess + user_input) else i, end='')
    print()

    return hangman( \
                word, \
                guess + user_input, \
                [], \
                (tries - 1) if user_input not in word and user_input not in guess else tries, \
                sum([(0 if i in guess + user_input else 1)for i in word]) == 0 \
            )

print(hangman()) #start the recursion