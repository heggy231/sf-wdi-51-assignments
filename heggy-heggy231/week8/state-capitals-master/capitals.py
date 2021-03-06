# [X] Welcome user to the game!

# [X] array to print "capital Columbus state Ohio" for all
#     do I need to user f?  no just use for in loop
#   for key in student:
#   print( f"{key} = {student[key]}" )
#   https://git.generalassemb.ly/sf-wdi-51/intro-to-python-1#dictionaries---iterating-items
# correct for state Wyoming number that state got correct0
# convert number to string: str(state["correct"]))


# [X] get the array to show up shuffled! 
# [X] get python to ask for name of capitol "please "
# [X] store the user's input
# [X] check user's input is correct or not and give feedback
# [ ] Initialize new keys in the dictionaries that store the number of times a user gets a capital correct and the number of times the answer is wrong.



# tips: Potentially Useful Methods
# print
# input
# for loop
# sorted
# random.shuffle()
# str <== str(12)
# "Sammy has {} balloons.".format(5)
#   => Sammy has 5 balloons.

# get random library!
import random

# testing array
# states = [
# {
#     "name": "Alabama",
#     "capital": "Montgomery"
# }, {
#     "name": "Pennsylvania",
#     "capital": "Harrisburg"
# }, {
#     "name": "Wyoming",
#     "capital": "Cheyenne"
# }]

# a list of state dictionaries
states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}, {
    "name": "Arkansas",
    "capital": "Little Rock"
}, {
    "name": "California",
    "capital": "Sacramento"
}, {
    "name": "Colorado",
    "capital": "Denver"
}, {
    "name": "Connecticut",
    "capital": "Hartford"
}, {
    "name": "Delaware",
    "capital": "Dover"
}, {
    "name": "Florida",
    "capital": "Tallahassee"
}, {
    "name": "Georgia",
    "capital": "Atlanta"
}, {
    "name": "Hawaii",
    "capital": "Honolulu"
}, {
    "name": "Idaho",
    "capital": "Boise"
}, {
    "name": "Illinois",
    "capital": "Springfield"
}, {
    "name": "Indiana",
    "capital": "Indianapolis"
}, {
    "name": "Iowa",
    "capital": "Des Moines"
}, {
    "name": "Kansas",
    "capital": "Topeka"
}, {
    "name": "Kentucky",
    "capital": "Frankfort"
}, {
    "name": "Louisiana",
    "capital": "Baton Rouge"
}, {
    "name": "Maine",
    "capital": "Augusta"
}, {
    "name": "Maryland",
    "capital": "Annapolis"
}, {
    "name": "Massachusetts",
    "capital": "Boston"
}, {
    "name": "Michigan",
    "capital": "Lansing"
}, {
    "name": "Minnesota",
    "capital": "St. Paul"
}, {
    "name": "Mississippi",
    "capital": "Jackson"
}, {
    "name": "Missouri",
    "capital": "Jefferson City"
}, {
    "name": "Montana",
    "capital": "Helena"
}, {
    "name": "Nebraska",
    "capital": "Lincoln"
}, {
    "name": "Nevada",
    "capital": "Carson City"
}, {
    "name": "New Hampshire",
    "capital": "Concord"
}, {
    "name": "New Jersey",
    "capital": "Trenton"
}, {
    "name": "New Mexico",
    "capital": "Santa Fe"
}, {
    "name": "New York",
    "capital": "Albany"
}, {
    "name": "North Carolina",
    "capital": "Raleigh"
}, {
    "name": "North Dakota",
    "capital": "Bismarck"
}, {
    "name": "Ohio",
    "capital": "Columbus"
}, {
    "name": "Oklahoma",
    "capital": "Oklahoma City"
}, {
    "name": "Oregon",
    "capital": "Salem"
}, {
    "name": "Pennsylvania",
    "capital": "Harrisburg"
}, {
    "name": "Rhode Island",
    "capital": "Providence"
}, {
    "name": "South Carolina",
    "capital": "Columbia"
}, {
    "name": "South Dakota",
    "capital": "Pierre"
}, {
    "name": "Tennessee",
    "capital": "Nashville"
}, {
    "name": "Texas",
    "capital": "Austin"
}, {
    "name": "Utah",
    "capital": "Salt Lake City"
}, {
    "name": "Vermont",
    "capital": "Montpelier"
}, {
    "name": "Virginia",
    "capital": "Richmond"
}, {
    "name": "Washington",
    "capital": "Olympia"
}, {
    "name": "West Virginia",
    "capital": "Charleston"
}, {
    "name": "Wisconsin",
    "capital": "Madison"
}, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}]

# print(states)
print("Welcome to name your capital game!!!")
# input("Tell me the capital of: " + states[3]["name"])
# for state in states: 

# initialize store the number of times a user gets a capital correct and the number of times the answer is wrong, must put outside of my function so it keep the previous game count for correct, wrong
total_correct = 0
total_wrong = 0

for state in states:
	state["correct"] = 0
	state["wrong"] = 0

def state_game():
	global total_correct
	global total_wrong
	# use random lib method shuffle to shuffle states 
	# shuffle has to be inside of function so it gets shuffled eachtime
	random.shuffle(states)

	for state in states: 
		capital_guess = input("Tell me the capital of: " + state["name"] + "state capital is " + state["capital"])
		print("your answer: " + capital_guess)
		
		if capital_guess == state["capital"]:
			print("yes! you are correct!")
			state["correct"] = state["correct"] + 1
			total_correct = total_correct + 1
			print("Game Total Correct " + str(total_correct))
		else:
			print("Sorry wrong capital. Try a new state!")
			state["wrong"] = state["wrong"] + 1
			total_wrong = total_wrong + 1
			print("Game Total wrong " + str(total_wrong))
			
		print("Your score for" + state["name"] + " is:" )
		print("Correct: " + str(state["correct"]))
		print("Wrong: " + str(state["wrong"]))
		
		print("You're correct {} time and wrong {} time".format(state["correct"], state["wrong"]))
		print()
# end of for in loop #############################
# 
	play_game_again = input("Want to play again? (yes/no)")
	if play_game_again == "yes" or play_game_again == "y":
		return state_game()
	else:
		print("Please come back and play with us again!!")
		return

state_game()

# if capital_guess == state["capital"]:
# for state in states:
#   print("capital " + state["capital"] + " state " + state["name"])

# assign each state { "correct": 0, "wrong":0}


# print(states[0]["correct"])
# expect to see each state's name with number of each state got correct which is set to 0 at first
  # print("correct for state " + state["name"] + " " + " number that state got correct" + str(state["correct"]))

# for state in states:
#   print("capital " + state["capital"] + " state " + state["name"] + " number that state got correct " + str(state["correct"]) + " number that user got wrong for that state " + str(state["wrong"]))


