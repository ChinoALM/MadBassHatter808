# Code Your Own Quiz Project
# Basics of the game include:
#   -Game has 3 or more levels and each level contains 4 or more blanks to fill in.
#   -At the beginning of the game, immediately after running the program, user is prompted
#       to select a difficulty level from easy / medium / hard.
#   -Once a level is selected, game displays a fill-in-the blank and a prompt to fill in the first blank.

# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.



#----Word in Position----
# Below is code for the function word_in_pos (meaning word in parts_of_speech),
# which takes in a string word and a list parts_of_speech as inputs. If there
# is a word in parts_of_speech that is a substring of the variable word, then
# return that word in parts_of_speech, else return None.

#def word_in_pos(word, parts_of_speech):
#    for pos in parts_of_speech:
#        if pos in word:
#           return pos
#    return None

def game_intro():

    print '/n'+ "Welcome to the Mad Bass Hatter's Madlib"
#   print more at the beginning of the game to direct your player how the game is played

easy = '''
    Hey, ___1___, don't make it ___2___
    Take a sad ___3___ and make it ___4___
    Remember to let ___5___ into your heart
    Then you can start to make it ___4___
    Hey, ___1___, don't be afraid
    You were made to go out and get ___5___
    The minute you let ___5___ under your skin
    Then you begin to make it ___4___.'''

medium = '''
    ___1___ is easy with ___2___ closed
    Misunderstanding all you see
    It's getting hard to be someone but it all works out
    It doesn't matter much to ___3___
    Let ___3___ take you down,
    cause I'm going to ___4___ Fields
    Nothing is real and nothing to get hung about
    ___4___ ___5___ forever.'''

hard = '''
    I look at you all see the ___1___ there that's ___2___
    While my ___3___ ___4___ ___5___
    I look at the floor and I see it needs sweeping
    Still my ___3___ ___4___ ___5___
    I don't know why nobody told you
    How to unfold your ___1___
    I don't know how someone ___6___ you
    They bought and sold you'''

answer_list = [["Jude", "bad", "song", "better", "her"], # for easy
               ["Living", "eyes", "me", "Strawberry", "Fields"], # for medium
               ["love", "sleeping", "guitar", "gently", "weeps", "controlled"]] # for hard

#Prompt user to select level difficulty. Valid level must be choosen to continue.
def select_level():
    level = raw_input("Enter your difficulty level (easy/medium/hard): ")
    if level == "easy":
        print "Easy level selected"
        return 0
    elif level == "medium":
        print "Medium level selected"
        return 1
    elif level == "hard":
        print "Hard level selected"
        return 2
    else:
        print "Invalid level selected. Please enter easy, medium, or hard."
        return select_level () # prompts user to select valid level



#Code below was given at the end of madlibs_generator lesson:
def play_game(ml_string, parts_of_speech):
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input("Type in a: " + replacement + " ")
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

print play_game(test_string1, parts_of_speech1)

