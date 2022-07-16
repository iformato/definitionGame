import random
from random import randint
from bs4 import BeautifulSoup
import requests

pickWords = True

with open('file1.txt', 'r') as f:
    words = f.readlines()
wordsLength = len(words)-1

while True:
    myAction = input('-play game\n-add a word')
    if myAction == 'add a word':
        print('what word would you like to add?')
        with open('file1.txt', 'a') as f:
            f.write(input())
        break
    else:
        game = True
        while game == True:
            while pickWords == True:
                myNumber = random.randint(0, wordsLength)
                word = words[myNumber]
                with open('badwords') as f:
                    if word in f.read():
                        print('oops, bad word')
                        pass
                    else:
                        break
            lives = 3
            while lives > 0:
                sep = '\\'
                word = word.split(sep, 1)[0]
                url = f'https://www.merriam-webster.com/dictionary/{word}'
                myGet = requests.get(url)
                doc = BeautifulSoup(myGet.text,'html.parser')
                myDefinition = doc.find('span', class_='dtText')
                myDefinition=myDefinition.text
                word = doc.find('h1',class_='hword')
                word=word.text
                print(myDefinition)
                wordLength = len(word)
                print(f'the word is {wordLength} letters long')

                myGuess = input('what is this word?\n')
                if myGuess == word:
                    print('you got it!')
                    break
                else:
                    lives-=1
                    print('wrong')
                    if lives == 2:
                        print(f'the first letter is {word[0]}')
                    elif lives == 1:
                        print(f'the first letter is {word[0]} and the second letter is {word[1]}')
                    else:
                        print('you lose :(')
                        print(f'{word}')
            myAction = input('play again?\n\n--was this word offensive? reply yes to remove--\n')
            if 'play again' in myAction:
                continue
            elif myAction == 'yes':
                with open('badwords','a') as f:
                    f.write(word)
                    print('taken care of')
                break
            else:
                print('thank you for playing!')
            break

