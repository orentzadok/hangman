#!/bin/python3
import random
from itertools import count


def check_word(word):
    if word==word_to_guess:
        print("you won")
        end=True
        return end

def check_index_in_string(word_to_guess,letter,index,count):
    if count==1:
        index=word_to_guess.find(letter, index)
    else:
        index = word_to_guess.find(letter, index+1)
    return index

def check_more_then_once(letter,word_to_guess):
    count=word_to_guess.count(letter)
    return (count)

def under_score(word,list):
    print(len(word))
    for i in range(len(word)):
        list.insert(i,"_")
    return list

def update_list(list,index,letter):
    list.insert(index, letter)
    list.pop(index + 1)
    return list

def hangman():
    hangman_paint=["""
        +---+
        |   |
    ================""",
        """
    +---+
    |   |
        |
        |
        |
    ==============""",
        """
        +---+
        |   |
        0   |
            |
            |
    ==========""",
    """
        +---+
        |   |
        0   |
        |   |
            |
    ==========""",
    """
        +---+
        |   |
        0   |
        |   |
       /|\\  |
    ==========""",
    """
     +---+
        |   |
        0   |
       /|\\  |
       /|\\  |
    =========="""

     ]
    return hangman_paint
end=False
list_of_words=["oreen","reed","yellow","buus","helllo","ggggg"]
word_to_guess=random.choice(list_of_words)
errors=0
used_letters=[]
solution=""
list=[]
list=under_score(word_to_guess,list)
while(errors<6 and not end):
        letter=input("enter a letter  ")
        if letter in used_letters:
                print(f"the letter {letter} was chosen before, choose another letter")
        else:
                if letter in word_to_guess:
                    print(f"the letter {letter} exists")
                    count=check_more_then_once(letter, word_to_guess)
                    i=1
                    index=0
                    if count==1:
                        index = check_index_in_string(word_to_guess, letter, index,count)
                        update_list(list, index, letter)
                    else:
                        for i in range(count):

                            index=check_index_in_string(word_to_guess,letter,index,count)
                            update_list(list,index,letter)
                    solution=''.join(list)
                    print(solution)
                else:
                        print("wrong")
                        errors=errors+1
                        hang=hangman()
                        print(hang[errors-1])
                used_letters.append(letter)

        print(used_letters)
        end=check_word(solution)
