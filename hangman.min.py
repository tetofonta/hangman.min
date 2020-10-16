#!/bin/env python3

def hangman(word="", guess="", foo=[], tries=1, guessed=False):
    user_input = input("Please insert the character ") if not guessed and word != "" and tries > 0 and print("Remaining tries: ", tries) is None else ""
    return hangman(input("Please insert THE word: "), "",  [],  int(input("\n"*100 + "Number of tries: ")),  False) if word == "" else ("WIN" if guessed or word == user_input else ("LOST" if tries <= 0 else hangman(word, guess, foo, tries-1, guessed))) if word == "" or len(user_input) > 1 or guessed or tries <= 0 else hangman(word, guess + user_input, [print("Current status")] + [print("?" if i not in (guess + user_input) else i, end='') for i in word] + [print()], (tries - 1) if user_input not in word or user_input in (guess + user_input) else tries, sum([(0 if i in guess + user_input else 1)for i in word]) == 0)

print(hangman()) #start the recursion