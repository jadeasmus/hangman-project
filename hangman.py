import random

game_word = ''
player_word = ''
attempt_count = 9
end = False

with open('animals.txt') as txt_words:
    words = txt_words.read().split('\n')
    # print(words)
    game_word = random.choice(words)
    game_word = game_word.lower()
    player_word = '_'*len(game_word)


# checks player's guess
def guess_check(letter):
    if letter in game_word:
        print("Correct!")
    else:
        print("Incorrect.")


# updates player's progress
def update_word():
    global player_word
    game_copy = game_word[:]
    player_copy = player_word[:]
    for c in game_copy:
        if guess == c:
            ind = game_copy.find(guess)
            game_list = list(game_copy)
            player_list = list(player_copy)
            player_list[ind] = game_list[ind]
            player_copy = "".join(player_list)
            player_word = player_copy

    print(player_word)
    print("You have " + str(attempt_count) + ' tries left.')


# gives hint by checking mother file
def hint():
    pass


# ends the round when attempt limit is reached
def end_game():
    global end
    if attempt_count == 0:
        end = True
        print("Attempt limit reached. The game word was: " + game_word)
    elif player_word == game_word:
        end = True
        print("You got the word! The game word was: " + game_word)
    else:
        end = False


# driver
print("Welcome to Hangman!!")
print("I have chosen a word. It has " + str(len(game_word)) + " letters. The category is animals.")
print("You have " + str(attempt_count) + " tries.")

for t in range(9):
    if end:
        break
    guess = input("Please enter your guess: ")
    attempt_count -= 1
    guess_check(guess)
    update_word()
    # hint()
    end_game()



