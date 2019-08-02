import random
potential_words = ["modulus", "algorithm", "list", "variable", "condition"]
word = random.choice(potential_words)
print(word)

# Make it a list of letters for someone to guess

Number_of_spaces = ["_"]*len(word)# TIP: the number of letters should match the word
guesses = 10
maxfails = 6
fails = 0
print(Number_of_spaces)
print (guesses)
print ("guesses left.")
print (maxfails)
print ("maxfails allowed.")
print (fails)
print ("fails currently.")
while fails < maxfails:
	guess = input("Guess a letter: ")
	
	# check if the guess is valid: Is it one letter? Have they already guessed it?
guesses = guesses-1
	# check if the guess is correct: Is it in the word? If so, reveal the letters!
fails = fails+1
print("You have " + str(maxfails - fails) + " tries left!")
