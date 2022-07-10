import random
from colorama import Fore
import colorama

def play_game():
    lines = []
    with open("/Users/mulla-2243/Documents/untitled folder/wordle/words.txt") as f:
        lines = f.readlines()
    word = "sorry" #random.choice(lines).strip()
    guess = ""
    lifes = 5
    word_list = list(word)
    print("Guess the word : ")
    while guess != word and lifes:
        guess = input()
        if guess+"\n" not in lines:
            print("Not a valid word")
            continue
        lifes = lifes - 1
        for i in range(5):
            g = guess[i]
            w = word[i]
            clr = Fore.LIGHTBLACK_EX
            w_cnt = word.count(g)
            g_cnt = guess.count(g)
            if g == w:
                clr = Fore.GREEN
            elif g in word:
                if guess[i:5].count(g) <= word.count(g) and guess.count():
                    clr = Fore.YELLOW
            print(clr + f"{guess[i]}", end=" ")
        else:
            colorama.Style.RESET_ALL
            print("")
    
    else:
        colorama.Style.RESET_ALL
        colorama.Fore.RESET
        if guess == word:
            print("Congrats!!")
        else:
            print(f"Better luck next time. Word is {word}")

def play_game_2():
    lines = []
    with open("/Users/mulla-2243/Documents/untitled folder/wordle/words.txt") as f:
        lines = f.readlines()
    word = random.choice(lines).strip()
    # word = "sorry"
    print(lines[5758-1])
    guess = ""
    lifes = 6
    print("Guess the word : ")
    while lifes:
        color_list = [Fore.RED]*5
        guess = input()
        if guess+"\n" not in lines:
            print("Not a valid word")
            continue
        lifes = lifes - 1
        guess_copy = guess
        word_copy = word
        for i in range(5):
            if guess_copy[i] == word_copy[i]:
                # word_copy = word_copy.replace(guess_copy[i],"0",1)
                # guess_copy = guess_copy.replace(guess_copy[i], "0", 1)
                guess_copy = string_replacer(guess_copy, i)
                word_copy = string_replacer(word_copy, i)
                print(f"{word_copy}   {guess_copy}")
                color_list[i] = Fore.GREEN
        for i in range(5):
            if guess_copy[i] != "0" and guess_copy[i] in word_copy:
                # word_copy = word_copy.replace(guess_copy[i], "0",1)
                # guess_copy = guess_copy.replace(guess_copy[i],"0", 1)
                word_copy = string_replacer(word_copy, word_copy.index(guess_copy[i]))
                guess_copy = string_replacer(guess_copy, i)
                print(f"{word_copy}   {guess_copy}")
                color_list[i] = Fore.YELLOW
        for i in range(5):
            print(color_list[i], f"{guess[i]}", end="")
        else:
            print()
        if guess == word:
            print("Congrats!!!")
            break
    else:
        print("Better Luck Next Time. Word is", end="")
        print(Fore.GREEN, word)

def string_replacer(string,index):
    l = list(string)
    l[index] = "0"
    str1 = ""
    return str1.join(l)
    
play_game_2()

