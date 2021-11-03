# importing random for random number generator
import random

# Creating Instructions

def instruction():
    print(' Welcome to Lo Shu Magic Square')
    print(' Here is how to play:')
    print(' You Will Enter a Series of numbers')
    print(' Or you can choose sets of numbers to be generated')
    print(' After a grid with 3 rows and 3 columns will be generated')
    print(' If each row, each column, and each diagonal all add up to the same number.')
    print(' You have a Lo Shu Magic Square')
    print(' If not, you will not have a Lo Shu Magic Square')
def game():  # ask user for which game they would like to play 
    choice = input('Type "random" for Generated Numbers or "input" for inputed Number:')
    if choice == "random":
        generator()
    if choice == "input":
        main()
    


def generator():
    # Creating variables for generator and writing loop
    while True:
        try:
            rowone_numone = random.randint(1,9) # variables for getting random numbers
            rowone_numtwo = random.randint(1,9)
            rowone_numthree = random.randint(1,9)
            break
        except ValueError:                          # if random numbers is not interger ask them to type again
            print('Only Numbers 1-10 Try again')
            
    print('You Have Successfully Enter Your Row 1 Number')   # prints that the correct numbers have been entered
    
    rowone = rowone_numone + rowone_numtwo + rowone_numthree # creates row one for 3 enter numbers 

    while True:
        try:
            rowtwo_numone = random.randint(1,9)          # variables for getting random numbers
            rowtwo_numtwo = random.randint(1,9)
            rowtwo_numthree = random.randint(1,9)
            break
        except ValueError:                            # if random numbers is not interger ask them to type again
            print('Only Numbers 1-10 Try again')
            
    print('You Have Successfully Enter Your Row 2 Number') # prints that the correct numbers have been entered
    
    rowtwo = rowtwo_numone + rowtwo_numtwo + rowtwo_numthree # creates row one for 3 enter numbers 
    
    while True:
        try:
            rowthree_numone = random.randint(1,9)       # variables for getting random numbers
            rowthree_numtwo = random.randint(1,9)
            rowthree_numthree = random.randint(1,9)
            break
        except ValueError:                              # if random numbers is not interger ask them to type again
            print('Only Numbers 1-10 Try Again')
            
    print('You Have Successfully Enter Your Row 3 Number')  # prints that the correct numbers have been entered
    
    rowthree = rowthree_numone + rowthree_numtwo + rowthree_numthree # creates row one for 3 enter numbers 

    column_one = rowone_numone + rowtwo_numone + rowthree_numone # creates column for rows 
    column_two = rowone_numtwo + rowtwo_numtwo + rowthree_numtwo
    column_three = rowone_numthree + rowtwo_numthree + rowthree_numthree

    diag_one = rowone_numone +rowtwo_numtwo + rowthree_numthree # creates diagonal row 
    diag_two = rowone_numthree + rowtwo_numtwo + rowthree_numone

    total = [rowone, rowtwo, rowthree, column_one, column_two, column_three, diag_one, diag_two] # makes a list of indv numbers and seperates them 
    results = total.count(total[0]) == len(total)  # gets the list and test if every total is true
    score = 0 # sets score to zero
    
    if all (total) == results:                        # shows that if all numbers are equal then excute 
        print('You have a Lo Shu Magic Square')
        print(rowone_numone, rowone_numtwo, rowone_numthree)
        print(rowtwo_numone, rowtwo_numtwo, rowtwo_numthree)
        print(rowthree_numone, rowthree_numtwo, rowthree_numthree)
        print('Score:')
        score =  score + 1
        
        
    else:                                              # if all numbers are not equal excute this command 
        print(' You Do Not have a Lo Shu Magic Square')
        print(rowone_numone, rowone_numtwo, rowone_numthree)
        print(rowtwo_numone, rowtwo_numtwo, rowtwo_numthree)
        print(rowthree_numone, rowthree_numtwo, rowthree_numthree)

    restart = input('To Play Random Generator again type "random" to play inputed numbers type "input" ')        # input for restarting or changing game 
    if restart == "random":
        generator()
    if restart == "input":
        main()
    elif restart == "no":
        exit()


def main(): 
# Creating variables for numbers and writing loop
    while True:                                                     
        try:
            rowone_numone = int(input(' Enter Your First Number For Row 1:')) # varaibles for user input
            rowone_numtwo = int(input(' Enter Your Second Number For Row 1:'))
            rowone_numthree = int(input('Enter Your Third Number For Row 1:'))
            break
        except ValueError:                                 # error code for int not entered 
            print('Only Numbers 1-10 Try again')
            
    print('You Have Successfully Enter Your Row 1 Number') 
    
    rowone = rowone_numone + rowone_numtwo + rowone_numthree # creating varaible for row 1 

    while True:
        try:
            rowtwo_numone = int(input(' Enter Your First Number For Row 2:')) # varaibles again for user input 
            rowtwo_numtwo = int(input(' Enter Your Second Number For Row 2:'))
            rowtwo_numthree = int(input('Enter Your Third Number For Row 2:'))
            break
        except ValueError:                           # error code for int not entered 
            print('Only Numbers 1-10 Try again')
            
    print('You Have Successfully Enter Your Row 2 Number') # printing that you entered numbers successfully
    
    rowtwo = rowtwo_numone + rowtwo_numtwo + rowtwo_numthree  # creating varaible for row 2 
     
    while True:
        try:
            rowthree_numone = int(input(' Enter Your First Number For Row 3:')) # variables again for user input 
            rowthree_numtwo = int(input(' Enter Your Second Number For Row 3:'))
            rowthree_numthree = int(input('Enter Your Third Number For Row 3:'))
            break
        except ValueError:                       # error code for int not entered       
            print('Only Numbers 1-10 Try Again')
            
    print('You Have Successfully Enter Your Row 3 Number') # printing that you entered numbers successfully
    
    rowthree = rowthree_numone + rowthree_numtwo + rowthree_numthree # variables again for creating row 

    column_one = rowone_numone + rowtwo_numone + rowthree_numone # creating variable for column 
    column_two = rowone_numtwo + rowtwo_numtwo + rowthree_numtwo
    column_three = rowone_numthree + rowtwo_numthree + rowthree_numthree

    diag_one = rowone_numone +rowtwo_numtwo + rowthree_numthree # creating variable for diagonal 
    diag_two = rowone_numthree + rowtwo_numtwo + rowthree_numone

    total = [rowone, rowtwo, rowthree, column_one, column_two, column_three, diag_one, diag_two] # creating total for list 
    results = total.count(total[0]) == len(total) # getting reuslts from list 
     
    score = 0 # creating score 
    
    if all (total) == results:  # if list is correct display correct 
        print(' You have a Lo Shu Magic Square')
        print(rowone_numone, rowone_numtwo, rowone_numthree)
        print(rowtwo_numone, rowtwo_numtwo, rowtwo_numthree)
        print(rowthree_numone, rowthree_numtwo, rowthree_numthree)
        
        
        
    else:
        print(' You Do Not have a Lo Shu Magic Square')  # if list is wrong show incorrect 
        print(rowone_numone, rowone_numtwo, rowone_numthree)
        print(rowtwo_numone, rowtwo_numtwo, rowtwo_numthree)
        print(rowthree_numone, rowthree_numtwo, rowthree_numthree)

    if score == 0: # adding score 
            scorefinal = score + 1
            print('You score is:', scorefinal)


    restart = input('To Play Random Generator again type "random" to play inputed numbers type "input" or type "no"') # restarting game 
    if restart == "random":
        generator()
    elif restart == "input":
        main()
    elif restart == "no":
        exit()

    


instruction()
game()
generator()
main()



