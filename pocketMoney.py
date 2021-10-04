import random
secret_number = random.randint(0, 10)
guess_count = 1
guess_limit = 4
while guess_count<guess_limit:
	guess = input("Guess: ")
	guess_count += 1
	if int(guess) == secret_number:
		print("congrats, you guessed it")
		break
else:
	print("YOU FAILLED")