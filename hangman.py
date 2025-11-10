#!/bin/python3
import random

def check_word(word):
	if guessed_letter==word_to_guess:
		
list_of_words=["oren","red","yellow","bus"]
word_to_guess=random.choice(list_of_words)
#print(word_to_guess)
errors=0
guessed_letters=[]
while(errors<5):
	letter=input("enter a letter  ")
	if letter in guessed_letters:
		print(f"the letter {letter} was chosen before, choose another letter")	
	else:
		if letter in word_to_guess:
			print(f"the letter {letter} exists in {word_to_guess}")
		else:
			print("wrong")
			errors+=1
		guessed_letters.append(letter)
	print(guessed_letters)
