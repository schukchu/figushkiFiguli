import random
from os import system

luckyNum = random.randint(1, 10)
lostFins = 0
yourNum = 1
hasWon = False

fins = ['empty finger', 'Left pinky', 'Left Ring finger', 'Left Middle finger', 'Left Index finger', 'Left Thumb',
        'Right pinky', 'Right Ring finger', 'Right Middle finger', 'Right Index finger', 'Right Thumb']
lost = ['nothing to see here', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

print('You\'ve fallen into an unfavorable position - you\'ve been caught by the Mad Jester')
print('Your objective is to get away from him as much fingers as you can keep.'
      'Good luck!')
while True :
    print('Jester: Pick any number you favor from 1 to 10')
    yourNum = int(input())
    if (yourNum == luckyNum):
        print("Congrats on your win! /n/" 
              "Visit me anytime you feel bored!")
        break
    elif (fins[yourNum - 1] == lost[lostFins]):
        print("Sorry mate, you've already lost that one")
    else:
        lost[lostFins] = fins[yourNum - 1]
        lostFins = lostFins + 1
        print(lost[lostFins - 1])
        print("Oops, your guess was incorrect!" 
              "You've lost your " + fins[yourNum - 1])

