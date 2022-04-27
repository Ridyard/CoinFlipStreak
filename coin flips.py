# automate the boring stuff - coin flip streaks project / chapter 4
""" script to record how often a sequence of same results occur within
10,000 (or n) simulated coin flips"""

import random

coin = ['heads', 'tails']               # represents a coin
coinFlips = []                          # to record coin flip results
sequence = {'heads':0, 'tails':0}       # to record n flip-sequences
sampleSize = 10000                      # how many coin flips to carry out
streakMax = 6                           # represents the number of consecutive results, triggering a streak
count = 1                               # a running count of coin flip results


# simulate the random coin flips & store results in coinFlips[]
for i in range(sampleSize):
    coinFlips.append(random.choice(coin)) # add random coin flip results to coinFlips[]
#print(coinFlips, '\n')


# check for streak of results
"""we compare the CURRENT list item to the NEXT list item in the try/catch block below;
therefore we need to check if a streak has been hit upfront;
if there has been a streak, we reset the count value and continue on to the next list item;
(we skip the current item as it has already been accounted for in the previoius loop run-through) """
for i,v in enumerate(coinFlips):
    if count == streakMax:              # check if the streak has been hit
        sequence[v] += 1                # if streak hit, update the sequence dict
        count = 1                       # streak has been hit, so we can reset the count variable back to 1
        continue                        # skip this item as it has already been accounted in the previous loop step-through
    else:
        try:
            if coinFlips[i+1] == v:     # compare current value in list to the next value in the list
                count +=1
            else:
                count = 1               # reset if current & next item don't match
        except:
            print('///')                # loop will go out of bounds on final run (as we're comparing current item with the next list item), hence the try/catch will handle this 
print(sequence)


# returns the total number of streaks
numberOfStreaks = sum(sequence.values()) # add together the values in the sequence dict
print('\nchance of streak: %s%%' % (numberOfStreaks / 100)) 
print()







