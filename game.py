import random

def game(word):
    tries = 6
    attempt = 1
    print("This game uses five letter words...")
    print("☐ = letter not included")
    print("☒ = letter included, but not in correct position")
    print("◼ = letter in correct position")
    print("--- guess the word ---")
    anslist = []
    while attempt <= tries:
        guess = input()
        if guess == word:
            anslist.append("◼◼◼◼◼")
            for i in anslist:
                print(i)
            return attempt
        #print the attempt here
        ansStr = ""
        for i in range(len(word)):
            if guess[i] == word[i]:
                ansStr = ansStr + "◼"
            elif guess[i] in word:
                ansStr = ansStr + "☒"
            else:
                ansStr = ansStr + "☐"
        attempt = attempt + 1
        anslist.append(ansStr)
        for i in anslist:
            print(i)
    return attempt - 1


def loadContent():
    my_file = open("sgb-words.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    return content_list

def main():
    wordlist = loadContent()

    # below this would be in a game loop
    while 1:
        wordidx = random.randint(0, len(wordlist) - 1)
        word = wordlist[wordidx]
        attempt = game(word)
        print("attempt:",attempt,"/",6)
        print("word was:", word)



main()