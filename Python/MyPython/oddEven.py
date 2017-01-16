# function to count from 1 to 2000. Generate the number and specify if it is odd or even
def odd_Even():
    for count in range(1,2000):
        if (count % 2 == 0):
            print "Even", count 
        else:
            print "Odd", count 

odd_Even()

