####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random
team_name = 'Team Five' # Only 10 chars displayed.
strategy_name = 'Random'
strategy_description = 'Random numbers dictate the outcome?'
print 'function is move([your history], your score)'
def move(their_history, their_score, my_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    choice1 = random.randint(0,10)
    choice2 = random.randint(0,10)
    choice3 = random.randint(0,10)
    counter = 0;
    decision = (choice1 + choice2 + choice3)/3
    
    conclusion = ''
    
    if (decision >= 7):
        print 'We Colude with you'
        conclusion = 'c'
    else:
        print 'get betrayed kiddo'
        conclusion = 'b'
    while(counter < 2):
        if (conclusion == 'c' and their_history[counter] == 'c'):
            print ('WE outta there bby')
            counter += 1
        elif (conclusion == 'b' and their_history[counter] == 'b'):
            print ("we both betrayed each other, rip 250 points")
            counter += 1
            their_score = their_score - 250
            my_score = my_score - 250
        elif (conclusion == 'b' and 'c'):
            print "I betrayed you, plus 100 points for me"
            counter += 1
            my_score += 100
        elif (their_history[counter] == 'b' and conclusion == 'c'):
            print "You betrayed me, rip 500 points"
            counter += 1
            my_score -= 500
            
        print ('my score' + (str)(my_score))
        print ('your score' + (str)(their_score))
move()