# players
list_of_players = [{'player': 1, 'money': 0}, {'player': 2, 'money': 0}, {'player': 3, 'money': 0}]

# wheel
wheel = ['BANKRUPT', 'Lose a Turn', 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]


function setupPhrase()
	secret_phrase = join(get 3 random words from word_list)
 	return secret_phrase


function game(list_of_players)
	
	# rounds 1 and 2

	for round in range (1, 3)
	
		secret_phrase = setupPhrase()
		secret_phrase_display = '_ _ _ _ _' from secret_phrase

		while round is not over 
		
			for player in list_of_players

				print(player number 'is the active player')

				while turn not over

					turn(player, secret_phrase, secret_phrase_display) #returns 0, 1, or 2

					if 0: #  round is over
						round_is_over = true
						break;
					elif 1: # turn is over
						turn_is_over = true
						continue
					else: # 2 turn is not over
						continue

				else: 
					continue # only executed if the inner loop did NOT break

				break; # only executed if the inner loop DID break


	# round 3				
	winner = player with max money

	secret_phrase = setupPhrase()
	secret_phrase_display = '_ _ _ _ _' from secret_phrase

	for letter in ['R', 'S', 'T', 'L', 'N', 'E']:
		revealLetter(letter, secret_phrase, secret_phrase_display)

	print('enter 3 more consonants')
	c1 = getValidConsonant() 
	c2 = getValidConsonant() 
	c3 = getValidConsonant()
	print('enter a vowel')
	v = getValidVowel()

	guesses = [c1, c2, c3, v]
	for letter in guesses:
		revealLetter(letter, secret_phrase, secret_phrase_display)

	print("you have 20 seconds to guess the phrase")
	start = time.start()
	result = guessThePhrase(secret_phrase)
	end = time.time()

	if result == 0 
		if (end - start) < 20
			print("you win ")
			winner['money'] += 5000
		else
			print('You guessed correctly but you ran out of time')
	else
		print(f'your answer was wrong, the correct asnwer was {secret_phrase}')


	print("Final results")
	for player in player_list:
   		print(f"Player {player['player']}, ${player['money']}")


# returns 0 if round is over (word is guessed)
# returns 1 if turn is over
# returns 2 if turn is not over
function turn(player, secret_phrase, secret_phrase_display)
	
	if only vowels left:
		
		if player[money] < 250: 
			return guessThePhrase(secret_phrase)

		return buyVowel(player, secret_phrase, secret_phrase_display) # returns 0, 1, or 2

	input ('guess the phrase' or 'spin the wheel')

		if 'turn the wheel'

			turn wheel (random.choice(wheel))

			if number

				consonant = getValidConsonant() # input("enter consonant")

				if consonant in secret_phrase
					player[money] += number
					reveal letter in display

					if word is fully guessed # round over
						return 0

					else

						input('Buy a vowel?')

						if yes
							return buyVowel(player, secret_phrase, secret_phrase_display) # returns 0, 1, or 2
						else 
							return 2 # turn not over

				else # consonant NOT in secret_phrase
					return 1 # turn is over
			
			elif bankrupt
				player[money] = 0
				return 1 # turn is over

			else 
				return 1 # turn is over

		else # guess the word
			return guessThePhrase(secret_phrase)
		


# returns 0 if round is over (word is guessed)
# returns 1 if turn is over
# returns 2 if turn is not over
function buyVowel(player, secret_phrase, secret_phrase_display)
	
	while 1:

		if (player[money] > 250):

			player[money] -= 250
			vowel = getValidVowel()
			
			if vowel in secret_phrase:
				reveal letter in display

				input('buy a vowel' or 'spin the wheel' or 'guess the phrase')
				if 'buy a vowel':
					continue
				elif 'spin the wheel'
					return 2
				else 
					return guessThePhrase(secret_phrase)

			else
				print("wrong")
				return 1

		else:
			print("no money")
			return 2




# returns 0 if round is over (word is guessed)
# returns 1 if turn is over
# returns 2 if turn is not over
function guessThePhrase(secret_phrase)

	if input('guess the phrase') == secret_phrase
		return 0
	else 
		return 1

	# return !(input('guess the phrase') == secret_phrase) ??



function getValidVowel()
	
	while 1:
		vowel = input('enter a vowel')
		if vowel in ['a', 'e', 'i', 'o', 'u']
			return vowel
		else 
			print('not a vowel')


function getValidConsonant() 

	while 1:
		consonant = input('enter a consonant')
		if consonant not in ['a', 'e', 'i', 'o', 'u']
			return consonant
		else 
			print('not a consonant')


# open letters in diplay

function revealLetter(letter, secret_phrase, secret_phrase_display)

	for i in range(len(secret_phrase)):
    	if secret_phrase[i] == letter:
    		secret_phrase_display[i] = letter
