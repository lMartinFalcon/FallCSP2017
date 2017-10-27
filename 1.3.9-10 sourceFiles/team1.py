import random
import time
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'NoIdea' # Only 10 chars displayed.
strategy_name = "Collude is Key, Let's be friends"
strategy_description = "There is a 1% chance that we won't not not not not not not not not not not not Collude"
def move():
    ''' Arguments accepted: None.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # Gets a random number between 1 and 100
    
    chance = random.randint(1, 100)
    if chance == 20:        # If the number is 20, then we will return c
        time.sleep(10)
        print 'ok'
        time.sleep(5)
        return 'c'
    else:                   # If the number is not 20, then will return b
        time.sleep(5)
        print 'ok'
        time.sleep(5)
        return 'b'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, depending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             