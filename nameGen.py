# This is for Sean
# You're welcome

from random import randint

adjLines = [line.rstrip('\n') for line in open('28K adjectives.txt')]
nounLines = [line.rstrip('\n') for line in open('91K nouns.txt')]


def genLinePull():
    randA = randint(0, 28000)
    randB = randint(0, 91000)

    theAdjArray = list(adjLines[randA])
    theNounArray = list(nounLines[randB])

    theAdjArray[0] = theAdjArray[0].lower()
    theNounArray[0] = theNounArray[0].lower()

    if theNounArray[-1] == 's':
        if theNounArray[-2] == 's':
            '''Do nothing'''
        else:
            theNounArray.pop()

    theAdj = ''.join(theAdjArray)
    theNoun = ''.join(theNounArray)

    print('༼ つ ◕_◕ ༽つ Don is a/an ' + adjLines[randA] + ' ' + theNoun + '\n')




#Print initial menu 
print('')
print('////////////////////////////////')
print('/// Welcome to The Generator ///') 
print('////////////////////////////////')
print('')

choice = '0'
while choice != "q":

    choice = input('Enter for a funny name, q to quit: ')
    choice = choice.lower()
    print()

    if choice == 'a':
    	genLinePull()
    elif choice == '':
        genLinePull()
    elif choice == 'q':
    	print('Thanks for playing, Seanald')
    else:
    	print('Unrecognized input, stop trying to break my programs Sean')




