wordfile = open("wordlist.txt", "r")
WordList = wordfile.read()
wordfile.close()
WordList = WordList.split(" ")

TempList = []

GreenYellowLetters = []
GreenLetters = []

def BestLetterRemoverWord(SmallWordList):
    wordfile = open("wordlist.txt", "r")
    FullWordList = wordfile.read()
    wordfile.close()
    FullWordList = FullWordList.split(" ")
    InitialLetterList = "".join(SmallWordList)
    FinalLetterList = ""
    print(GreenLetters)
    for i in InitialLetterList:
        if i not in GreenLetters:
            FinalLetterList = FinalLetterList + i


    FinalLetterList = FinalLetterList + 'a' + 'e'
    TempList = FinalLetterList
    FinalLetterList = ""
    for letter in TempList:
        if letter not in FinalLetterList:
            FinalLetterList = FinalLetterList+letter

    print("letters:"+FinalLetterList)

    PlaceHolderWordList = FullWordList
    for word in PlaceHolderWordList:
        correctcount = 0
        for letter in FinalLetterList:
            if letter in word and letter != 'a' and letter != 'e':
                correctcount += 1
        if correctcount < 3:
            FullWordList.remove(word)
            print("removed "+word)

    print(FullWordList)

    if len(FullWordList) == 0:
        return(FindBestWord(SmallWordList))
        print('returning small list')
    else:
        print('returning big list')
        return(FindBestWord(FullWordList))

def FindBestWord(WordList):
    FinalList = WordList
    MostFrequentLetter = ''
    HighestFrequency = 0

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
                    if currentcount > HighestFrequency:
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
    #print('Using Green Logic\n')
    global WordList
    global GreenYellowLetters
    GreenYellowLetters.append(CorrectLetter)
    if CorrectLetter not in GreenLetters:
        GreenLetters.append(CorrectLetter)
    wordnumber = 0
    while wordnumber != len(WordList):
        word = WordList[wordnumber]
        if word[int(Character)] == CorrectLetter:
            TempList.append(word)
        wordnumber += 1
    WordList = TempList


def Yellow(AttemptedLetter, Character):
    #print('Using Yellow Logic\n')
    global WordList
    global GreenYellowLetters
    GreenYellowLetters.append(AttemptedLetter)
    wordnumber = 0
    while wordnumber != len(WordList):
        word = WordList[wordnumber]
        if word[int(Character)] != AttemptedLetter and AttemptedLetter in word:
            TempList.append(word)
        wordnumber += 1
    WordList = TempList


def White(AttemptedLetter, Character):
    #print('Using White Logic\n')
    global WordList
    global GreenYellowLetters
    wordnumber = 0

    if AttemptedLetter not in GreenYellowLetters:
        #print("white full run")
        while wordnumber != len(WordList):
            if AttemptedLetter not in WordList[wordnumber]:
                TempList.append(WordList[wordnumber])
            wordnumber += 1
    else:
        #print("white column run")
        while wordnumber != len(WordList):
            word = WordList[wordnumber]
            if word[int(Character)] != AttemptedLetter:
                TempList.append(word)
            wordnumber += 1
    WordList = TempList
    #print("white done")
AltWordUsed = False
for WordLoop in range(6):
    wordinput = input("Enter Word(cares): ")
    if wordinput == 'debug':
        print(WordList)
        wordinput = input("Enter Word(cares): ")
    valueinput = input("Enter Values(YGYWW): ")
    for character in range(5):
        # print('working on character ' + str(character))
        if valueinput[character] == 'G':
            #print('inputing green info' + wordinput[character] + str(character))
            Green(wordinput[character], character)
        elif valueinput[character] == 'Y':
            # print('inputing yellow info ' + wordinput[character] + str(character))
            Yellow(wordinput[character], character)
        elif valueinput[character] == 'W':
            #print('inputing white info ' + wordinput[character] + str(character))
            White(wordinput[character], character)
        #print(WordList)
        #print(str(len(WordList)) + ' words remaining')
        # cont = input("continue?")

        TempList = []

    # print(WordList)
    print(str(len(WordList)) + ' words remaining')
    print('on word '+str(WordLoop))
    if WordLoop <=4 and len(GreenLetters) >= 3 and len(WordList) > 2 and AltWordUsed == False:
        AltWordUsed = True
        print('Best Word(Alt): ' + BestLetterRemoverWord(WordList))
    else:
        print('Best Word(Prim): ' + FindBestWord(WordList))
