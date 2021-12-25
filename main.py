import json
import random
import re

def setupPhrase(phrases):
    secret_phrase =  random.choice(phrases)
    return secret_phrase


# load data from json, clean non alpha charachters
def cleanData():
    # load phrases from phrases.json to 'phrases_not_clean' list as tuples
    with open('phrases.json') as f:
        data = json.load(f)
        phrases_not_clean = list(data.items())

    clean_list_pass_1 = []
    clean_list_pass_2 = []

    for tuple in phrases_not_clean:

        clean_list_item = (re.sub("[^a-zA-Z &]+", "", tuple[0]).lower(), re.sub("-", " ", tuple[1]))
        clean_list_pass_1.append(clean_list_item)

    for tuple in clean_list_pass_1:

        clean_list_item = (re.sub("&", "and", tuple[0]).lower(), tuple[1].title())
        clean_list_pass_2.append(clean_list_item)

    return clean_list_pass_2

def start():

    print("===================================")
    print("----Welcome to Wheel of Fortune----")
    player1 = input("Enter 1st player's name: ")
    player2 = input("Enter 2nd player's name: ")
    player3 = input("Enter 3rd player's name: ")

    # setup players
    list_of_players = [{'player': player1, 'money': 0, 'total bank': 0}, 
                       {'player': player2, 'money': 0, 'total bank': 0},
                       {'player': player3, 'money': 0, 'total bank': 0}]

    
    phrases = cleanData()

    # wheel
    wheel = ['BANKRUPT', 'Lose a Turn', 100, 150, 200, 250, 300, 350, 400, 400, 450, 500, 500, 500, 550, 600, 650, 650, 700, 700, 750, 800, 850, 900]

    game(list_of_players, wheel, phrases)

def game(list_of_players, wheel, phrases):

    # rounds 1 and 2
    for round in range (1, 3):

        round_is_over = False
        guessed_letters = []
        # set a new secret word
        secret_phrase = setupPhrase(phrases)
        print(secret_phrase)

        display = list(secret_phrase[0])
        
        for i in range(len(display)):
            if secret_phrase[0][i] != ' ':
                display[i] = '_'



        while not round_is_over:

            for player in list_of_players:
                
                turn_is_over = False
                while not turn_is_over:
                
                    turn(player, secret_phrase, display, guessed_letters, wheel) #returns 0, 1, or 2

                    if 0: #  round is over
                        round_is_over = True
                        break;
                    elif 1: # turn is over
                        turn_is_over = True
                        continue
                    else: # 2 turn is not over
                        continue

                else: 
                    continue # only executed if the inner loop did NOT break

                break; # only executed if the inner loop DID break


# 	# round 3				
# 	winner = player with max money # max bank after 2 rounds (if tie choose random)

# 	secret_phrase = setupPhrase()
# 	secret_phrase_display = '_ _ _ _ _' from secret_phrase

# 	for letter in ['R', 'S', 'T', 'L', 'N', 'E']:
# 		revealLetter(letter, secret_phrase, secret_phrase_display)

# 	print('enter 3 more consonants')
# 	c1 = getValidConsonant() 
# 	c2 = getValidConsonant() 
# 	c3 = getValidConsonant()
# 	print('enter a vowel')
# 	v = getValidVowel()

# 	guesses = [c1, c2, c3, v]
# 	for letter in guesses:
# 		revealLetter(letter, secret_phrase, secret_phrase_display)

# 	print("you have 20 seconds to guess the phrase")
# 	start = time.start()
# 	result = guessThePhrase(secret_phrase)
# 	end = time.time()

# 	if result == 0 
# 		if (end - start) < 20
# 			print("you win ")
# 			winner['money'] += 5000
# 		else
# 			print('You guessed correctly but you ran out of time')
# 	else
# 		print(f'your answer was wrong, the correct asnwer was {secret_phrase}')


# 	print("Final results")
# 	for player in player_list:
#    		print(f"Player {player['player']}, ${player['money']}, ${player['total']")


# retruns true if display is hiding only vowels
def onlyVowelsLeft(secret_phrase, display):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(display)):
        if secret_phrase[i] not in vowels and display[i] == '_':
            return False
    return True

# returns player choice (spin or guess)
def playerChoice():
        while 1:
            choice = input("Do you want to spin the wheel or guess the word? s/g: ").lower()
            if choice == 's' or choice == 'g':
                return choice
            else:
                print("Invalid Input.")

# returns true if player wants to buy a vowel
def buyAVowel():
    while 1:
        choice = input("Do you want to buy a vowel? y/n: ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid Input.")


# returns 0 if round is over (word is guessed)
# returns 1 if turn is over
# returns 2 if turn is not over
def turn(player, secret_phrase, display, guessed_letters, wheel):
    
    printDisplay(player, secret_phrase, display, guessed_letters)
    
    if onlyVowelsLeft(secret_phrase, display):
        
        print("Only vowels left.")

        if player['money'] < 250: 
            print("You don't have enough money to buy a vowel. Try t o guess the phrase.")
            return guessThePhrase(secret_phrase)

        return buyVowel(player, secret_phrase, display, guessed_letters) # returns 0, 1, or 2

    else:

        # get player choice (s for spin the wheel, g for guess the phrase)
        choice = playerChoice() 
        
        # spin the wheel
        if choice == 's':
            
            wheel_value = random.choice(wheel)

            if isinstance(wheel_value, int):

                print(f"The wheel landed on ${wheel_value}")

                consonant = getValidConsonant(guessed_letters) 
                
                count = 0 # number of occurnaces
                for i in range(len(secret_phrase[0])):
                    if secret_phrase[0][i] == consonant:
                        count += 1

                if consonant in secret_phrase[0]:
                    player['money'] += count * wheel_value # (* count)
                    revealLetter(consonant, secret_phrase, display)
                    printDisplay(player, secret_phrase, display, guessed_letters)

                    if '_' not in display: # round over
                        return 0
                    else:
                        if buyAVowel():
                            return buyVowel(player, secret_phrase, display, guessed_letters) # returns 0, 1, or 2
                        else:
                            return 2 # turn not over
                else: # consonant NOT in secret_phrase
                    print(f"{consonant} is not in the phrase.")
                    return 1 # turn is over
            
            elif wheel_value == 'BANKRUPT':
                print("BANKRUPT")
                player['money'] = 0
                return 1 # turn is over

            else:
                print("Lose a Turn")
                return 1 # turn is over

        else: # guess the word
            return guessThePhrase(secret_phrase)
               
		


# # returns 0 if round is over (word is guessed)
# # returns 1 if turn is over
# # returns 2 if turn is not over
def buyVowel(player, secret_phrase, display,  guessed_letters):
    
    while 1:

        if (player['money'] > 250):

            player['money'] -= 250
            vowel = getValidVowel(guessed_letters)
            
            if vowel in secret_phrase[0]:
                revealLetter(vowel, secret_phrase, display)
                printDisplay(player, secret_phrase, display)
                # player can choose to buy another vowel or guess the word or spin the wheel
                if buyAVowel():
                    continue
                else:
                    choice = playerChoice() # return 's' or 'g'
                    if choice == 's':
                        return 2
                    else:
                        return guessThePhrase(secret_phrase)
            else:
                print(f"{vowel} is not in the phrase.")
                return 1

        else:
            print("You do not have enough money to buy a vowel")
            return 2




# returns 0 if round is over (word is guessed)
# returns 1 if turn is over
# returns 2 if turn is not over
# 
def guessThePhrase(secret_phrase):

    if input("Guess the phrase: ") == secret_phrase[0]:
        print("You guess was correct !!!")
        print("Round over.")
        return 0
    else:
        print("Wrong guess.")
        return 1



def getValidVowel(guessed_letters):
	
    while 1:
        vowel = input('Enter a vowel: ').lower()
        if vowel in ['a', 'e', 'i', 'o', 'u'] and vowel not in guessed_letters:
            guessed_letters.append(vowel)
            return vowel
        else:
            print(f"{vowel} is not a vowel. Please try again.")


def getValidConsonant(guessed_letters):
    list_of_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l','m', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    while 1:
        consonant = input('Enter a consonant: ').lower()
        if consonant in list_of_consonants and consonant not in guessed_letters:
            guessed_letters.append(consonant)
            return consonant
        else:
            print(f"{consonant} is not a consonant. Please try again.")


# # open letters in diplay

def revealLetter(letter, secret_phrase, display):
    for i in range(len(secret_phrase[0])):
        if secret_phrase[0][i] == letter:
            display[i] = letter


def printDisplay(player, secret_phrase, display, guessed_letters):
    print("===================================")
    print(f"Player: {player['player']}: $ {player['money']}")
    print(f"{' '.join(display)}")
    print(f"\n{secret_phrase[1]}")
    print(f"Previous guesses {', '.join(guessed_letters)}")
    print("===================================")
    print(f"cheat: {secret_phrase[0]}")









start()