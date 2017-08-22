# Code Your Own Quiz Project

# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.

#Code below was given at the end of madlibs_generator lesson:
#def play_game(ml_string, parts_of_speech):
#    replaced = []
#    ml_string = ml_string.split()
#    for word in ml_string:
#        replacement = word_in_pos(word, parts_of_speech)
#        if replacement != None:
#            user_input = raw_input("Type in a: " + replacement + " ")
#            word = word.replace(replacement, user_input)
#            replaced.append(word)
#        else:
#            replaced.append(word)
#    replaced = " ".join(replaced)
#    return replaced

#print play_game(test_string1, parts_of_speech1)

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

problem_dict ={'easy':
'''Hey, ___1___, don't make it ___2___
Take a sad ___3___ and make it ___4___
Remember to let ___5___ into your heart
Then you can start to make it ___4___
Hey, ___1___, don't be afraid
You were made to go out and get ___5___
The minute you let ___5___ under your skin
Then you begin to make it ___4___
''',

'medium':'''Need to input content''',

'hard': '' 'Need to input content'''}

#try making a commit again!


