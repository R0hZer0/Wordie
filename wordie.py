#!/usr/bin/python3

from itertools import permutations
import enchant
import sys


def helper():
    print("=====================================")
    print("\nUsage : ./wordie.py word")
    print("\n=> Provide letters as a single Word\n")
    print("=====================================")
    sys.exit(0)

# Checking if word exists in dictionary or not
def checkWord(perm):
    wordToSearch = ""
    for letter in perm:
        wordToSearch += letter
    toCheck = d.check(wordToSearch)
    if (toCheck == True):
        finalWords.append(wordToSearch)
    else:
        exit

words = []
finalWords = []
d = enchant.Dict("en_US")
finalList = []

try:
    # Handling input
    temp = sys.argv[1]
    if(len(temp) < 5 or len(temp) > 7):
        helper()
    
    words = list(temp)
    perms = permutations(words)
    
    # Applying permutations on all letters and checking them against pyenchant's dictionary
    for i in list(perms):
        for j in range(3,len(words)+1):   # 3 is used as min length of word is 3 in Words of Wonders
            checkWord(i[0:j])

    # Unique elements inside final list
    for i in finalWords:
        if i not in finalList:
            finalList.append(i)
            finalList.append(", ")
    
    finalList.pop()
    for i in finalList:
        print(i,end='')
    print()

except IndexError as e:
    helper()
