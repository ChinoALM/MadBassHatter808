# # Basics of the game include:
#   -Game has 3 or more levels and each level contains 4 or more blanks to fill in.
#   -At the beginning of the game, immediately after running the program, user is prompted
#       to select a difficulty level from easy / medium / hard.
#   -Once user selects a level, game displays a fill-in-the blank and a prompt for the user
#       to fill in the first blank, and subsequently plays a full game of madlibs.

# This function greets the user and prompts the user to select a level difficulty.
def madhat_begin_game():
    print '\n'+ "Welcome to the Mad Hatter's Madlib Game!" +'\n'
    print "Fill in the blanks with lyrics from my favorite Beatles' songs!!" + '\n'
    print "Answers are case sensitive, so watch for proper Nouns and the beginning of sentences!" + '\n'
    input_check = True
    while input_check is True:
        level_input = raw_input("Type in easy, medium or hard to select a difficulty: ")
        if level_input == 'easy' or level_input == 'medium' or level_input == 'hard':
            input_check= False
        else:
            print '\n' + 'Invalid level selected. Please select easy, medium, or hard.' + '\n'
    return level_input

# This functions returns a problem string associated with the level difficulty the user selected.
def madhat_problem(level,problem_dict):
    choosen_problem = problem_dict[level]
    #print choosen_problem + '\n'
    return choosen_problem

# This functions returns a list of answers associated with the level difficulty the user selected.
def madhat_answers(level):
    if level == 'easy':
        answer_list = ['Jude', 'bad', 'song', 'better', 'her']
    if level == 'medium':
        answer_list =['Living', 'eyes', 'me', 'Strawberry', 'Fields']
    if level == 'hard':
        answer_list =['love', 'sleeping', 'guitar', 'gently', 'weeps', 'controlled']
    return answer_list

# Checks if a word in fill_in_blank is a substring of the word passed in.
def word_in_pos(word, fill_in_blank):
    for pos in fill_in_blank:
        if pos in word:
            return pos
    return None

# Prints string that corresponds to the level of difficulty the user selected and prompts user
# until they answer all the blanks correctly, or until the user has 3 incorrect guesses, returning
# the number of incorrect guesses, leaving them with 1 less attempt for each incorrect answer.
def game_instructions(string,answers,blanks,strike,string_index):
    for word in string:
        is_blank= word_in_pos(word,blanks)
        if is_blank!= None:
            while strike != 0:
                print '\n' + " ".join(string) + '\n'
                user_answer = raw_input("You have " + str(strike) + " attempts left. Please enter your guess: ")
                correct = word_in_pos(user_answer,answers)
                if correct != None:
                    print "\n"+ "Correct!" + "\n"
                    string[string_index] = user_answer
                    string_index = string_index+1
                    break
                else:
                    strike = strike -1
        else:
            string_index = string_index +1
    return strike
    return string_one

# Takes the number of incorrect guesses and tells the user if  they won or lost
def win_or_lose(strike_count):
    if strike_count == 0:
        print "\n" + "Wah. Wah. You lost! GAME OVER! Please try again." + "\n"
    else:
        print "\n" + "Congratulations, you won!" + "\n"


# Inputs for functions and calling upon them in a dictionary:
problem_dict ={'easy':
    '''
    Hey, ___1___, don't make it ___2___
    Take a sad ___3___ and make it ___4___
    Remember to let ___5___ into your heart
    Then you can start to make it ___4___
    Hey, ___1___, don't be afraid
    You were made to go out and get ___5___
    The minute you let ___5___ under your skin
    Then you begin to make it ___4___.
    ''',
    'medium':
    '''
    ___1___ is easy with ___2___ closed
    Misunderstanding all you see
    It's getting hard to be someone but it all works out
    It doesn't matter much to ___3___
    Let ___3___ take you down,
    cause I'm going to ___4___ Fields
    Nothing is real and nothing to get hung about
    ___4___ ___5___ forever.
    ''',
    'hard':
    '''
    I look at you all see the ___1___ there that's ___2___
    While my ___3___ ___4___ ___5___
    I look at the floor and I see it needs sweeping
    Still my ___3___ ___4___ ___5___
    I don't know why nobody told you
    How to unfold your ___1___
    I don't know how someone ___6___ you
    They bought and sold you.
    '''
    }

fill_in_blank =["___1___","___2___","___3___","___4___","___5___","___6___"]
strike = 3
string_index = 0

level= madhat_begin_game()
problem_string = madlib_problem(level,problem_dict)
answer_list = madhat_answers(level)
string_one = problem_string.split()

x = game_instructions(string_one,answer_list,fill_in_blank,strike,string_index)

win_or_lose(x)

#prevents the program from closing out automatically
x = raw_input("Hit return to exit:")