wordfile = open("wordlist.txt", "r")
WordList = wordfile.read()
wordfile.close()
WordList = WordList.split(" ")

TempList = []

def FindBestWord(WordList):
    FinalList = WordList
    MostFrequentLetter = ''
    HighestFrequency = 0
    currentcount = 0

    for character in range(5):
        TempList = []
        # print('Starting character: ' + str(character))
        for i in range(97, 123):
            # print('Starting letter: '+chr(i))
            currentcount = 0
            for word in FinalList:
                # print('currently testing: '+word)
                letter = word[character]
                # print('character ' +str(character)+' of '+word+' is '+letter)
                if letter == chr(i):
                    currentcount += 1
                    # print('i have found '+str(currentcount)+' matches for the letter, '+letter)
                    if currentcount >= HighestFrequency:
                        MostFrequentLetter = chr(i)
                        HighestFrequency = currentcount
                        # print('the new highest letter is '+chr(i)+' with '+str(currentcount)+' instances')
        # print('the highest letter in character '+str(character)+' is '+MostFrequentLetter+' with '+str(HighestFrequency)+' instances')
        for word in FinalList:
            if word[character] == MostFrequentLetter:
                TempList.append(word)
        FinalList = TempList
        MostFrequentLetter = ''
        HighestFrequency = 0
        # print(FinalList)
    return (FinalList[0])


def Green(CorrectLetter, Character):
    # print('Using Green Logic\n')
    global WordList
    wordnumber = 0
    while wordnumber != len(WordList):
        word = WordList[wordnumber]
        if word[int(Character)] == CorrectLetter:
            TempList.append(word)
        wordnumber += 1
    WordList = TempList


def Yellow(AttemptedLetter, Character):
    # print('Using Yellow Logic\n')
    global WordList
    wordnumber = 0
    while wordnumber != len(WordList):
        word = WordList[wordnumber]
        if word[int(Character)] != AttemptedLetter and AttemptedLetter in word:
            TempList.append(word)
        wordnumber += 1
    WordList = TempList


def White(AttemptedLetter, Character):
    # print('Using White Logic\n')
    global WordList
    wordnumber = 0

    while wordnumber != len(WordList):
        word = WordList[wordnumber]
        if word[int(Character)] != AttemptedLetter:
            TempList.append(word)
        wordnumber += 1
    WordList = TempList

    # while wordnumber != len(WordList):
    # if AttemptedLetter not in WordList[wordnumber]:
    # TempList.append(WordList[wordnumber])
    # wordnumber += 1
    # WordList = TempList

while True:
    wordinput = input("Enter Word(cares): ")
    valueinput = input("Enter Values(YGYWW): ")
    for character in range(5):
        # print('working on character ' + str(character))
        if valueinput[character] == 'G':
            # print('inputing green info' + wordinput[character] + str(character))
            Green(wordinput[character], character)
        elif valueinput[character] == 'Y':
            # print('inputing yellow info ' + wordinput[character] + str(character))
            Yellow(wordinput[character], character)
        elif valueinput[character] == 'W':
            # print('inputing white info ' + wordinput[character] + str(character))
            White(wordinput[character], character)
        # print(WordList)
        #print(str(len(WordList)) + ' words remaining')
        # cont = input("continue?")

        TempList = []

    # print(WordList)
    print(str(len(WordList)) + ' words remaining')
    print('Best Word: ' + FindBestWord(WordList))
