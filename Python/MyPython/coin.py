# function to read each inputted score and give grade back 10 times
import random

heads_count = 0
tails_count = 0

for i in range (1,5001):
    random_num = random.random() 
    random_rounded = round(random_num)
    if(random_rounded == 0):
        side = "head(s)"
        heads_count += 1
    else:
        side = "tail(s)"
        tails_count += 1

    print "Attempt #%d :Throwing a coin...It's a %s ...Got  %d head(s) so far and %d tails so far" %(i, side, heads_count, tails_count)

