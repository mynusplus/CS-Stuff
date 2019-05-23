####
# Prisoners Dilemma Code by Ted Lindholm, with parts from the general prisoners dilemma code by Arthur Goldman
####

import sys
from loadfromdir import get_list_of_filenames
import os
import random
from pathlib import Path


from prisoners_dilemma import load_modules, play_tournament, play_single_dilemma

#print("going from the top in pd")

team_name = '?'
strategy_name = 'Optimization'
strategy_description = 'Tests strategies against individual players and selects the best one'

# Copies module locations from running the function
modules = sys.argv
updated_modules = []




# Finds the tournament location by looking at updated modules
for module_index in range(len(modules)):
    if modules[module_index] == '-d':
        assert (module_index + 1) < len(modules), "Got the dir flag with no argument"
        module_directory = modules[module_index + 1]
        assert os.path.isdir(module_directory), "There is no directory named {}".format(module_directory)
        if not (module_directory[-1] == '/'):
            module_directory += '/'
        add_to_modules = get_list_of_filenames(module_directory)
        for module in add_to_modules:
            updated_modules.append(module)
    elif modules[module_index - 1] == '-d':
        continue
    else:
        add_to_modules = modules[module_index]
        updated_modules.append(add_to_modules)

# print(updated_modules)
for mod in updated_modules:
    if os.path.basename(mod) == "pd.py":
        PRISONERS_DILEMMA_LOCATION = os.path.dirname(os.path.dirname(mod))
updated_modules[:] = []

TOURNAMENT_LOCATION = os.path.join(PRISONERS_DILEMMA_LOCATION, "tournament")
MODULE_LOCATION = os.path.join(TOURNAMENT_LOCATION, "pd.py")
MODULE_2_LOCATION = os.path.join(TOURNAMENT_LOCATION, "pd_2.py")
MODULE_3_LOCATION = os.path.join(TOURNAMENT_LOCATION, "pd_3.py")
INFO_LOCATION = os.path.join(PRISONERS_DILEMMA_LOCATION, "info.py")
INFO_LOCATION_2 = os.path.join(PRISONERS_DILEMMA_LOCATION, "info_2.py")

# What round number am I in? My teammates?
round_num_with_me = -1
round_num_with_2 = -1
round_num_with_3 = -1

# If you want to add more strategies, update it here, define a strategy_clone version of it, do the thing so it says
# "Running strategy_clone". below that, write the code so it is removed, and write the what_to_do part in the move
# function itself

# Maybe running a fake tournament will fix issues?
def test_run():
    updated_modules = []

    info = open(INFO_LOCATION, 'w+')
    info.close()

    for module_index in range(len(modules)):
        if modules[module_index] == '-d':
            assert (module_index + 1) < len(modules), "Got the dir flag with no argument"
            module_directory = modules[module_index + 1]
            assert os.path.isdir(module_directory), "There is no directory named {}".format(module_directory)
            if not (module_directory[-1] == '/'):
                module_directory += '/'
            add_to_modules = get_list_of_filenames(module_directory)
            for module in add_to_modules:
                updated_modules.append(module)
        elif modules[module_index - 1] == '-d':
            continue
        else:
            add_to_modules = modules[module_index]
            updated_modules.append(add_to_modules)

    #print("here are the module names in pd: " + str(updated_modules))
    teams = load_modules(updated_modules)

    play_tournament(teams)

    updated_modules = []

if os.path.exists(INFO_LOCATION):
    os.remove(INFO_LOCATION)
else:
    test_run()

STRATEGIES = ['BETRAY', 'GRUDGE', 'EARLY_HISTORY', 'COPYCAT', 'CCB', 'ONCE', 'EDUCATED_GUESS', 'WIZAL_DOG', 'ONCE_2', 'ANTIHISTORY']
not_used_strategies = ['COLLUDE']

scores_for_strategy = {}
for strategy in STRATEGIES:
    scores_for_strategy.update({strategy: []})

their_scores_for_strategy = {}
for strategy in STRATEGIES:
    their_scores_for_strategy.update({strategy: []})


def make_file_in_prisoners_dilemma(name):
    assert type(name) is str, "make_file_in_tournament with nonstring"
    complete_name = os.path.join(PRISONERS_DILEMMA_LOCATION, name)
    # complete_name = PRISONERS_DILEMMA_LOCATION + SLASH + name
    return complete_name


def find_rounds():
    global round_num_with_me
    global round_num_with_2
    global round_num_with_3

    for module_index in range(len(modules)):
        if modules[module_index] == '-d':
            assert (module_index + 1) < len(modules), "Got the dir flag with no argument"
            module_directory = modules[module_index + 1]
            assert os.path.isdir(module_directory), "There is no directory named {}".format(module_directory)
            if not (module_directory[-1] == '/'):
                module_directory += '/'
            add_to_modules = get_list_of_filenames(module_directory)
            for module in add_to_modules:
                updated_modules.append(module)
        elif modules[module_index - 1] == '-d':
            continue
        else:
            add_to_modules = modules[module_index]
            updated_modules.append(add_to_modules)

    round_num_with_me = updated_modules.index(MODULE_LOCATION)
    if MODULE_2_LOCATION in updated_modules:
        round_num_with_2 = updated_modules.index(MODULE_2_LOCATION)
    if MODULE_3_LOCATION in updated_modules:
        round_num_with_3 = updated_modules.index(MODULE_3_LOCATION)
    # print("My location: " + str(round_num_with_me))
    # print("2 location: " + str(round_num_with_2))
    # print("3 location: " + str(round_num_with_3))

    updated_modules[:] = []


find_rounds()


def play_strategy(strategy):
    #print("running play_strategy in pd")

    info = open(INFO_LOCATION, 'w+')
    info.close()

    for module_index in range(len(modules)):
        if modules[module_index] == '-d':
            assert (module_index + 1) < len(modules), "Got the dir flag with no argument"
            module_directory = modules[module_index + 1]
            assert os.path.isdir(module_directory), "There is no directory named {}".format(module_directory)
            if not (module_directory[-1] == '/'):
                module_directory += '/'
            add_to_modules = get_list_of_filenames(module_directory)
            for module in add_to_modules:
                updated_modules.append(module)
        elif modules[module_index - 1] == '-d':
            continue
        else:
            add_to_modules = modules[module_index]
            updated_modules.append(add_to_modules)

    if MODULE_LOCATION in updated_modules:
        updated_modules.remove(MODULE_LOCATION)
    else:
        assert False, "module not in updated_modules, MODULE_LOCATION may be incorrect"

    def collude_clone():
        """always colludes"""
        location = make_file_in_prisoners_dilemma('collude.py')
        f = open(location, 'w+')
        f.write('team_name = \'?\'\n')
        f.write('strategy_name = \'?\'\n')
        f.write('strategy_description = \'?\'\n')
        f.write('def move(my_history, their_history, my_score, their_score):\n')
        f.write(' '*4 + 'return \'c\'\n')
        f.close()
        updated_modules.append(location)

    def betray_clone():
        """always betrays"""
        location = make_file_in_prisoners_dilemma('betray.py')
        f = open(location, 'w+')
        f.write('team_name = \'?\'\n')
        f.write('strategy_name = \'?\'\n')
        f.write('strategy_description = \'?\'\n')
        f.write('def move(my_history, their_history, my_score, their_score):\n')
        f.write(' ' * 4 + 'return \'b\'\n')
        f.close()
        updated_modules.append(location)

    def grudge_clone():
        """colludes, but holds a grudge"""
        location = make_file_in_prisoners_dilemma('grudge.py')
        f = open(location, 'w+')
        f.write('team_name = \'?\'\n')
        f.write('strategy_name = \'?\'\n')
        f.write('strategy_description = \'?\'\n')
        f.write('def move(my_history, their_history, my_score, their_score):\n')
        f.write(' ' * 4 + 'if \'b\' in their_history:''\n')
        f.write(' ' * 8 + 'return \'b\'''\n')
        f.write(' ' * 4 + 'else:''\n')
        f.write(' ' * 8 + 'return \'c\'''\n')
        f.close()
        updated_modules.append(location)

    def early_history_clone():
        """"uses early history, from example4.py"""
        location = make_file_in_prisoners_dilemma('early_history.py')
        f = open(location, 'w+')
        f.write('team_name = \'?\'\n')
        f.write('strategy_name = \'?\'\n')
        f.write('strategy_description = \'?\'\n')
        f.write('def move(my_history, their_history, my_score, their_score):\n')
        f.write(' ' * 4 + 'if len(my_history)==0:''\n')
        f.write(' ' * 8 + 'return \'c\'''\n')
        f.write(' ' * 4 + 'else:''\n')
        f.write(' ' * 8 + 'recent_round_them = their_history[-1]''\n')
        f.write(' ' * 8 + 'recent_round_me = my_history[-1]''\n')
        f.write(' ' * 8 + 'for round in range(len(my_history)-1):''\n')
        f.write(' ' * 12 + 'prior_round_them = their_history[round]''\n')
        f.write(' ' * 12 + 'prior_round_me = my_history[round]''\n')
        f.write(' ' * 12 + 'if (prior_round_me == recent_round_me) and (prior_round_them == recent_round_them):''\n')
        f.write(' ' * 16 + 'return their_history[round]''\n')
        f.write(' ' * 8 + 'if my_history[-1]==\'c\' and their_history[-1]==\'b\':''\n')
        f.write(' ' * 12 + 'return \'b\'''\n')
        f.write(' ' * 8 + 'else:''\n')
        f.write(' ' * 12 + 'return \'c\'''\n')
        f.close()
        updated_modules.append(location)

    def once_clone():
        """betrays 12 and 13"""
        location = make_file_in_prisoners_dilemma('once.py')
        f = open(location, 'w+')
        f.write('team_name = \'?\'\n')
        f.write('strategy_name = \'?\'\n')
        f.write('strategy_description = \'?\'\n')
        f.write('def move(my_history, their_history, my_score, their_score):\n')
        f.write(' ' * 4 + 'if len(my_history) == 12 or 13:''\n')
        f.write(' ' * 8 + 'return \'b\'''\n')
        f.write(' ' * 4 + 'else: ''\n')
        f.write(' ' * 8 + 'return \'c\'''\n')
        f.close()
        updated_modules.append(location)

    def antihistory_clone():
        """counters early history"""
        location = make_file_in_prisoners_dilemma('antihistory.py')
        f = open(location, 'w+')
        f.write('team_name = \'?\'\n')
        f.write('strategy_name = \'?\'\n')
        f.write('strategy_description = \'?\'\n')
        f.write('def move(my_history, their_history, my_score, their_score):\n')
        f.write(' ' * 4 + 'if len(my_history) == 0 or 2:''\n')
        f.write(' ' * 8 + 'return \'c\'''\n')
        f.write(' ' * 4 + 'else: ''\n')
        f.write(' ' * 8 + 'return \'b\'''\n')
        f.close()
        updated_modules.append(location)

    def once_2_clone():
        """counters WizalDOG"""
        location = make_file_in_prisoners_dilemma('once.py')
        f = open(location, 'w+')
        f.write('team_name = \'?\'\n')
        f.write('strategy_name = \'?\'\n')
        f.write('strategy_description = \'?\'\n')
        f.write('def move(my_history, their_history, my_score, their_score):\n')
        f.write(' ' * 4 + 'if len(my_history) <= 13:''\n')
        f.write(' ' * 8 + 'return \'b\'''\n')
        f.write(' ' * 4 + 'else: ''\n')
        f.write(' ' * 8 + 'return \'c\'''\n')
        f.close()
        updated_modules.append(location)

    def copycat_clone():
        """copies previous round results"""
        location = make_file_in_prisoners_dilemma('copycat.py')
        f = open(location, 'w+')
        f.write('team_name = \'?\'\n')
        f.write('strategy_name = \'?\'\n')
        f.write('strategy_description = \'?\'\n')
        f.write('def move(my_history, their_history, my_score, their_score):\n')
        f.write(' ' * 4 + 'if len(my_history) == 0:''\n')
        f.write(' ' * 8 + 'return \'c\'''\n')
        f.write(' ' * 4 + 'else:''\n')
        f.write(' ' * 8 + 'return their_history[-1]''\n')
        f.close()
        updated_modules.append(location)

    def ccb_clone():
        """goes ccb over and over"""
        location = make_file_in_prisoners_dilemma('ccb.py')
        f = open(location, 'w+')
        f.write('team_name = \'?\'\n')
        f.write('strategy_name = \'?\'\n')
        f.write('strategy_description = \'?\'\n')
        f.write('def move(my_history, their_history, my_score, their_score):\n')
        f.write(' ' * 4 + 'if (len(my_history)+1)%3 == 0:''\n')
        f.write(' ' * 8 + 'return \'b\'''\n')
        f.write(' ' * 4 + 'else: ''\n')
        f.write(' ' * 8 + 'return \'c\'''\n')
        f.close()
        updated_modules.append(location)

    def educated_guess_clone():
        """"counters educated guess"""
        location = make_file_in_prisoners_dilemma('educated_guess.py')
        f = open(location, 'w+')
        f.write('team_name = \'?\'\n')
        f.write('strategy_name = \'?\'\n')
        f.write('strategy_description = \'?\'\n')
        f.write('def move(my_history, their_history, my_score, their_score):\n')
        f.write(' ' * 4 + 'betrays = len(list(filter(lambda x: x == \'b\', my_history))) - len(list(filter(lambda x: x == \'b\', their_history)))''\n')
        f.write(' ' * 4 + 'colludes = len(list(filter(lambda x: x == \'c\', my_history))) - len(list(filter(lambda x: x == \'c\', their_history)))''\n')
        f.write(' ' * 4 + 'if betrays < colludes:''\n')
        f.write(' ' * 8 + 'c = \'b\'''\n')
        f.write(' ' * 4 + 'else:''\n')
        f.write(' ' * 8 + 'c = \'c\'''\n')
        f.write(' ' * 4 + 'return c''\n')
        f.close()
        updated_modules.append(location)

    def wizal_dog_clone():
        """"counters WizalBOB and ROB"""
        location = make_file_in_prisoners_dilemma('wizal_dog.py')
        f = open(location, 'w+')
        f.write('team_name = \'?\'\n')
        f.write('strategy_name = \'?\'\n')
        f.write('strategy_description = \'?\'\n')
        f.write('def move(my_history, their_history, my_score, their_score):\n')
        f.write(' ' * 4 + 'if len(my_history) < 15:''\n')
        f.write(' ' * 8 + 'return \'c\'''\n')
        f.write(' ' * 4 + 'elif str(their_history[0] + their_history[1] + their_history[2] + their_history[3]) == \'bccb\':''\n')
        f.write(' ' * 8 + 'return \'b\'''\n')
        f.write(' ' * 4 + 'else:''\n')
        f.write(' ' * 8 + 'return \'b\'''\n')
        f.close()
        updated_modules.append(location)

    assert strategy in STRATEGIES, "Not a valid strategy in play_strategy"
    if strategy == 'COLLUDE':
        collude_clone()
        # print("Running collude_clone")
    elif strategy == 'BETRAY':
        betray_clone()
        # print("Running betray_clone")
    elif strategy == 'GRUDGE':
        grudge_clone()
        # print("Running grudge_clone")
    elif strategy == 'EARLY_HISTORY':
        early_history_clone()
    elif strategy == 'ONCE':
        once_clone()
    elif strategy == 'COPYCAT':
        copycat_clone()
    elif strategy == 'CCB':
        ccb_clone()
    elif strategy == "EDUCATED_GUESS":
        educated_guess_clone()
    elif strategy == "WIZAL_DOG":
        wizal_dog_clone()
    elif strategy == "ONCE_2":
        once_2_clone()
    elif strategy == "ANTIHISTORY":
        antihistory_clone()
    else:
        assert False, "No code for that strategy"

    #print("In pd: " + str(updated_modules))
    teams = load_modules(updated_modules)

    all_scores = play_tournament(teams)[0]
    # print("all scores" + str(all_scores))
    h = all_scores[::-1]
    my_score = h[0]
    scores_for_strategy[strategy] = my_score
    # print("Scores for " + strategy + ": " + str(scores_for_strategy[strategy]))

    their_scores = all_scores[0:len(all_scores) - 1]
    their_scores_against_me = []
    for score in their_scores:
        lst = score[::-1]
        their_scores_against_me.append(lst[0])
    their_scores_for_strategy[strategy] = their_scores_against_me
    # print("Opponent scores for "+ strategy + ": "+ str(their_scores_against_me))

    for item in ["collude.py","betray.py", "grudge.py", "early_history.py", "once.py", "copycat.py", "ccb.py", "educated_guess.py", "wizal_dog.py", "once_2.py", "antihistory.py"]:
        if os.path.exists(os.path.join(PRISONERS_DILEMMA_LOCATION, item)):
            os.remove(os.path.join(PRISONERS_DILEMMA_LOCATION, item))

    updated_modules[:] = []

    os.remove(INFO_LOCATION)


def optimize_strategy():
    for item in STRATEGIES:
        for thing in STRATEGIES:
            assert len(scores_for_strategy[item]) == len(scores_for_strategy[thing]), \
                'Some strategies have more data than others for me'

    # Sorts scores by code played against
    scores_for_round = {}
    for round in range(len(scores_for_strategy["BETRAY"])):
        for strategy in STRATEGIES:
            if round in scores_for_round:
                scores_for_round[round].append(scores_for_strategy[strategy][round])
            else:
                scores_for_round.update({round: [scores_for_strategy[strategy][round]]})
    # print(scores_for_round)

    # Finds best strategy for each round
    strategies_for_round = scores_for_round
    for round in scores_for_round:
        best = -600
        for item in scores_for_round[round]:
            if item > best:
                best = item
        strategies_for_round[round] = STRATEGIES[scores_for_round[round].index(best)]
    # print(strategies_for_round)

    return strategies_for_round


# Simulates the tournaments for all strategies, failsafe to prevent infinite recursion
if not os.path.exists(INFO_LOCATION):
    TESTING_FAILED = False
    for strategy in STRATEGIES:
        play_strategy(strategy)
else:
    TESTING_FAILED = True

# Determines optimal strategy for each round, stores in variable optimal strategies
n = optimize_strategy()
optimal_strategies = []
for item in n:
    optimal_strategies.append(n[item])

# Makes optimal strategies against allies betray
if TESTING_FAILED == False:
    if not round_num_with_2 == -1:
        optimal_strategies[round_num_with_2] = "BETRAY"
    if not round_num_with_3 == -1:
        optimal_strategies[round_num_with_3] = "BETRAY"


if TESTING_FAILED == False:
    pass
    # print("Optimal strategies: "+ str(optimal_strategies) + " in pd")
else:
    # print("No optimal strategies, TESTING_FAILED == True in pd")
    for module_index in range(len(modules)):
        if modules[module_index] == '-d':
            assert (module_index + 1) < len(modules), "Got the dir flag with no argument"
            module_directory = modules[module_index + 1]
            assert os.path.isdir(module_directory), "There is no directory named {}".format(module_directory)
            if not (module_directory[-1] == '/'):
                module_directory += '/'
            add_to_modules = get_list_of_filenames(module_directory)
            for module in add_to_modules:
                updated_modules.append(module)
        elif modules[module_index - 1] == '-d':
            continue
        else:
            add_to_modules = modules[module_index]
            updated_modules.append(add_to_modules)




    #For if testing failed
    total_num_of_rounds = len(updated_modules)
    strategies = []
    for i in range(total_num_of_rounds):
        if updated_modules[i] == MODULE_2_LOCATION and not MODULE_2_LOCATION == -1:
            strategies.append("BETRAY")
        elif updated_modules[i] == MODULE_3_LOCATION and not MODULE_3_LOCATION == -1:
            strategies.append("BETRAY")
        elif updated_modules[i] == MODULE_LOCATION:
            pass
        else:
            strategies.append("GRUDGE")

# Starting at round 0...
ROUND_NUM = -1

def move(my_history, their_history, my_score, their_score):

    global ROUND_NUM

    if TESTING_FAILED == True:
        #print("move in pd uses TESTING_FAILED")
        if len(my_history) == 0:
            #print("in pd: " + str(optimal_strategies))
            ROUND_NUM = ROUND_NUM + 1



        what_to_do = strategies[ROUND_NUM]
        #what_to_do = 'GRUDGE'

        if what_to_do == 'GRUDGE':
            if 'b' in their_history:
                return 'b'
            else:
                return 'c'
        if what_to_do == "BETRAY":
            return 'b'

    else:
        if len(my_history) == 0:
            # print("in pd: " + str(optimal_strategies))
            ROUND_NUM = ROUND_NUM + 1
            # print("Using " + str(optimal_strategies[ROUND_NUM]) + " in " + str(ROUND_NUM) + ". I am " + str(round_num_with_me) + ", partner is "+ str(round_num_with_2))

        what_to_do = optimal_strategies[ROUND_NUM]

        if what_to_do == "COLLUDE":
            return 'c'
        elif what_to_do == "BETRAY":
            return 'b'
        elif what_to_do == "GRUDGE":
            if 'b' in their_history:
                return 'b'
            else:
                return 'c'
        elif what_to_do == "EARLY_HISTORY":

            if len(my_history) == 0:  # It's the first round: collude
                return 'c'
            else:

                recent_round_them = their_history[-1]
                recent_round_me = my_history[-1]

                for round in range(len(my_history) - 1):
                    prior_round_them = their_history[round]
                    prior_round_me = my_history[round]

                    if (prior_round_me == recent_round_me) and \
                            (prior_round_them == recent_round_them):
                        return their_history[round]

                if my_history[-1] == 'c' and their_history[-1] == 'b':
                    return 'b'
                else:
                    return 'c'
        elif what_to_do == "ONCE":
            if len(my_history) == 12 or 13:
                return 'b'
            else:
                return 'c'
        elif what_to_do == "ONCE_2":
            if len(my_history) <= 13:
                return 'b'
            else:
                return 'c'
        elif what_to_do == "COPYCAT":
            if len(my_history) == 0:
                return 'c'
            else:
                return their_history[-1]
        elif what_to_do == "CCB":
            if (len(my_history)+1) % 3 == 0:
                return 'b'
            else:
                return 'c'
        elif what_to_do == "EDUCATED_GUESS":
            betrays = len(list(filter(lambda x: x == 'b', my_history))) - len(list(filter(lambda x: x == 'b', their_history)))
            colludes = len(list(filter(lambda x: x == 'c', my_history))) - len(list(filter(lambda x: x == 'c', their_history)))

            if betrays < colludes:
                c = 'b'
            else:
                c = 'c'

            return c
        elif what_to_do == "WIZAL_DOG":
            if len(my_history) < 15:
                return 'c'
            elif str(their_history[0] + their_history[1] +
                       their_history[2] + their_history[3]) == 'bccb':
                return 'b'
            else:
                return 'b'
        elif what_to_do == "ANTIHISTORY":
            if len(my_history) == 0 or 2:
                return 'c'
            else:
                return 'b'
        else:
            return 'b'
