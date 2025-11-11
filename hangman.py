#!/bin/python3
import random

def check_word(word):
	if guessed_letters==word_to_guess:
		print("you won")
		

list_of_words=["oren","red","yellow","bus"]
word_to_guess=random.choice(list_of_words)
#print(word_to_guess)
errors=0
guessed_word=""
while(errors<5):
	letter=input("enter a letter  ")
	if letter in guessed_letters:
		print(f"the letter {letter} was chosen before, choose another letter")	
	else:
		if letter in word_to_guess:
			print(f"the letter {letter} exists ")
		else:
			print("wrong")
			errors+=1
		guessed_letters.append(letter)
	print(guessed_letters)
	check_word(guessed_letters)
