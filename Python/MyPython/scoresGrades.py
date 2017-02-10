# function to read each inputted score and give grade back 10 times


print "Scores and Grades"
for i in range(0,10):
    data = raw_input("Input score: ")
    try: 
        score = int(data)
    except ValueError:
        print "Please input a valid integer"
    else: 
        if(score >= 90):
                grade = "A"
        elif(score >= 80):
                grade = "B"
        elif(score >= 70):
                grade = "C"
        elif(score >= 60):
                grade = "D"
        else:
                print "Invalid score"
        print "Score: %d; Your grade is %s" %(score, grade)

print "End of the program. Bye!"
