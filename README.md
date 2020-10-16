# synthetic hangman
## This is a challenge me and my friends got ourself. just for fun.

Tn base idea is to write a python script that can be used to play hangman as more synthetic as possible.

This is my implementation with four lines of code.

## Explaination

**BEFORE WE START!**

I'm not very familiar with python, as i have a limited experience and not a lot of real life examples of good python coding...

Any help/note/suggestion is more than accepted =)

### Base concepts an tricks

First of all, we need to think about the algorithm.

because of the hangman game style, we need to implement some kind of _"ask the user and repeat"_ operation.
this can be done with three methods:

- A for loop... which is the worst implementation possible in terms of line usage =(

- A while loop
    in this case, that's a valid option... the condition can be used for the user input and the cycle body may be used for the computation.
    but we will need some variables, and variable declaration has to be done ouside the while scope. that will take some juicy lines.

- Recursion
    this is the method i choose.
    In one line we can define the function and the variables we will be using. in one or two lines we can get the user input and do the computation, calling the function recursively with the updated variables.
    we will need one more line to call the function and print out the output.

#### tips and triks

##### inline if and inline for

we will make a massive use of inline if and inline for's.

```python
#This
v = ""
if condition:
    v = "something"
else:
    v = "something else"
#can be written as
v = "something" if condition else "something else"
```

Inline ifs are useful in calling functions with conditional parameters, like
```python
def a_func(parameter):
    pass #do something i dunno

print(a_func("correct" if fetchCondition() else "not_correct"))
```

Inline fors are useful too:

```python
#This
my_array = [1, 2, 3]
v = []
for i in my_array:
    v.append(i*2)
#now v == [2, 4, 6]

#can be written as
my_array = [1, 2, 3]
v = [i*2 for i in my_array]
``` 

inline for can be seen as a array mapping call: for each element of an array A, by performing some actions, we can build an array B so that for any element of B, it will be the "image" of the relative element of A.

##### void functions return something

In python void type does not exists.
A function that in a language like **C** should return void (see how a function call works in c, the return value get pushed to the stack, and if void is returned, nothing will be pushed), in python will return a special type called **None**
But the advantage is that **None** is something. so the conditions **print() is None -- print() is not None** will result respectively as **true** and **false** --because print() does return None--

##### short circuit
As we all know, computers are kinda smart. expecially when evaluating conditions.

_we can use that_

Commonly known as the _"shortcircuit rule"_, the interpreter will stop evaluating a logic expression if the result can be already determined.
For example, if an expression like **(cond a) and (cond b)** has to be evaluated, and **cond a** happens to be false, then we are sure that **false and <something>** will get us **false**.
Similar case for an or statement: **(cond a) or (cond b)**, if **cond a** happens to be truem then **true or <something>** will result in **true**.

So we can combine the shortcircuir thing and the None return type to do something in an if statement.
for example we can write multiple lines like
```python
v = ""
if (condition a) or (condition b):
    v = "something"
    print("some other thing")
else:
    v = "not something"
```

as a single line consisting of:

```python
v = "something" if (condition a) or (condition b) or print("some other thing") is not None else "not something"
```
##### printing during the function call.

suppose we have a variable called "word" that contains a word.
suppose we have then a list of character guessed by the user.

we need to print out the word (hiding the characters not found by the user) and then call the recursive function.
_--spoiler that's the method i used--_

first of all we need to write this in a compacted manner.
```python
#somewhere, somehow defied in the code this variables...
word = "<word>"
guess = "<list of letters guessed by the user>"

print("Current status: ")
for i in word:
    character_to_print = ""
    if i not in guess:                  #if the word's character is not in the guessed list
        character_to_print = "?"        #we will print a question mark
    else
        character_to_print = i          #else we will print the character
    print(character_to_print, end='')   #end='' in print make the function print the character then printing '' instead of the common newline.

```

FOA, the for body can be written as
```python
#somewhere, somehow defied in the code this variables...
word = "<word>"
guess = "<list of letters guessed by the user>"

print("Current status: ")
for i in word:
    print("?" if i not in guess else i, end='')   #end='' in print make the function print the character then printing '' instead of the common newline.

```
we can define an ingnored variable equal to a list that we can generate. remember that print does return something.

```python
#somewhere, somehow defied in the code this variables...
word = "<word>"
guess = "<list of letters guessed by the user>"

foo = [print("?" if i not in guess else i, end='') for i in word]
```

this code will print out the word, with unknown character as '?', and then will return a list of None elements, one for each character.

because of the use of the recursion, we can pass the resulting list directly in the function call, as an ignored parameter.

## The Algorithm.

we define a function with these parameters:
- word: the word to be guessed. initialized as ""
- guess: the list of characters the user has typed in. initialized as ""
- foo: something we will ignore
- tries: the remaining tries the user can use to find the word.
- guessed: a flag remainding the last iteration if the wor has been found. initialized as False.

First of all, we need to take the user input, but we need to do this only if the game has started (the word has been set), if the word has not been guessed the last iteration, and if the user has tries left.

```python
def hangman(word="", guess="", foo=[], tries=1, guessed=False):
    user_input = ""
    if not guessed and parola != "" and tries > 0
        user_input = input("Please select the word to be guessed ")
        print("Remaining tries: ", tries)
```

Then we have to do some conditioning:
if the word has not been set (== "") --so the game has not started yet--, we should ask the word and the number of triest to play with, then calling the next iteration.

if the user tries to guess an entire word, then we should check against the equality of the input and the word, returning "WIN" if correct, or re-calling the function with _tries - 1_ tries.

if the user has guessed the word last iteration, we should print out "WIN"

if the user has not any try left, we should print out "LOST".

if not any of the previous conditions, we should iterate:
so we call our functon with 
- word: the same word, 
- guess: the guess list plus the user input
- using the ignored input to print the guessed characters.
- tries: the same value if the character guessed is in the word but has not been guessed yet
- guessed: true if all the letters in the word are in the guess list. this can be archeived by mapping the word's characters as 0 if the letter is in the guess list, else 1; then summing the array checking for the equality with 0.

our script becomes:
```python
#see hangman_standard.py

def hangman(word="", guess="", foo=[], tries=1, guessed=False):
    user_input = ""
    if not guessed and word != "" and tries > 0:
        user_input = input("Please insert the character ")
        print("Remaining tries: ", tries)

    if word == "":
        return hangman( \
            input("Please insert THE word: "), \                #this will be evaluated first, asking for the user guessing word.
            "", \                                               #the guess list should be empty
            [], \                                               #ignored.
            int(input("\n"*100 + "Number of tries: ")), \       #we ask the user the number of allowed tries, but before printing out the string, we clear the screen printing 100 '\n'
            False \                                             #the word has not been guessed yet.
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
                word, \                                                                 #the current word
                guess + user_input, \                                                   #guess list updated with the newly typed character
                [], \                                                                   #ignored
                (tries - 1) if user_input not in word or user_input in (guess + user_input) else tries, \ #tries - 1 if the character is not in word, tries otherwise
                sum([(0 if i in guess + user_input else 1)for i in word]) == 0 \        #we sum the mapping of the word's characters as 0 if present in guesslist or 1 and check if the sum is zero (all characteres guessed)
            )

print(hangman()) #start the recursion
```

We should now start soing some shortening...

we can start using the print inline tecnique to print using the ignored variable...

```python
def hangman(word="", guess="", foo=[], tries=1, guessed=False):
    #unchanged...

    #print("Current status:")
    #for i in word:
    #    print("?" if i not in (guess + user_input) else i, end='')
    #print()

    return hangman( \
                word, \                                                                                     #the current word
                guess + user_input, \                                                                       #guess list updated with the newly typed character
                [print("Current status")] + [print("?" if i not in (guess + user_input) else i, end='') for i in word] + [print()], \
                (tries - 1) if user_input not in word or user_input in (guess + user_input) else tries, \   #tries - 1 if the character is not in word, tries otherwise
                sum([(0 if i in guess + user_input else 1)for i in word]) == 0 \                            #we sum the mapping of the word's characters as 0 if present in guesslist or 1 and check if the sum is zero (all characteres guessed)
            )

print(hangman()) #start the recursion
```

now we can compress the user inputing...

```python
def hangman(word="", guess="", foo=[], tries=1, guessed=False):
    user_input = input("Please insert the character ") if not guessed and word != "" and tries > 0 and print("Remaining tries: ", tries) is None else ""

    #if not guessed and word != "" and tries > 0:
    #    user_input = input("Please insert the character ")
    #    print("Remaining tries: ", tries)

    #unchanged

print(hangman()) #start the recursion
```

then the logic, we can compress it in the last return, by choosing what to return in a series of inline ifs

we can make it by saying:

```python
if word == "" or len(user_input) > 1 or guessed or tries <= 0:
    if word == "":
        #return new game thing...
    else:
        if guessed or word == user_input:
            return "WIN"
        else:
            if tries <= 0:
                return "LOST"
            else:
                hangman(word, guess, foo, tries-1, guessed)
else:
    #iterate
```

compressed looks like this:

```python
return (new_game_thing) if word == "" else ("WIN" if guessed or word == user_input else ("LOST" if tries <= 0 else hangman(word, guess, foo, tries-1, guessed))) if word == "" or len(user_input) > 1 or guessed or tries <= 0 else (iterate)
```

## THE FINAL SCRIPT

```python
#see hangman.min.py

def hangman(word="", guess="", foo=[], tries=1, guessed=False):
    user_input = input("Please insert the character ") if not guessed and word != "" and tries > 0 and print("Remaining tries: ", tries) is None else ""
    return hangman(input("Please insert THE word: "), "",  [],  int(input("\n"*100 + "Number of tries: ")),  False) if word == "" else ("WIN" if guessed or word == user_input else ("LOST" if tries <= 0 else hangman(word, guess, foo, tries-1, guessed))) if word == "" or len(user_input) > 1 or guessed or tries <= 0 else hangman(word, guess + user_input, [print("Current status")] + [print("?" if i not in (guess + user_input) else i, end='') for i in word] + [print()], (tries - 1) if user_input not in word or user_input in (guess + user_input) else tries, sum([(0 if i in guess + user_input else 1)for i in word]) == 0)

print(hangman()) #start the recursion
```

# 4 lines of code - 2 line of effective operations ;-)