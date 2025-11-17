#!/bin/python3
import random
def check_word(word):
	if word==word_to_guess:
		print("you won")
		end=True	
		return end

def check_index_in_string(word_to_guess,letter):
	index=word_to_guess.index(letter)
	print(index)
	return index

end=False
list_of_words=["oren","red","yellow","bus"]
word_to_guess=random.choice(list_of_words)
#print(word_to_guess)
errors=0
used_letters=[]
solution=""
while(errors<5 and not end):
	letter=input("enter a letter  ")
	if letter in used_letters:
		print(f"the letter {letter} was chosen before, choose another letter")	
	else:
		if letter in word_to_guess:
			print(f"the letter {letter} exists")
			index=check_index_in_string(word_to_guess,letter)
			print(solution[:index])
			solution=solution[:index]+letter+solution[(index+1):]
			print(solution)
		else:
			print("wrong")
			errors+=1
		used_letters.append(letter)
			
#		check_guess(word_to_guess,used_letters,solution)
	print(used_letters)
	end=check_word(solution)
