import sys
from loadfromdir import get_list_of_filenames
import os

# Finds the tournament location by looking at updated modules
updated_modules = []
modules = sys.argv
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

for mod in updated_modules:
    if os.path.basename(mod) == "pd_2.py":
        PRISONERS_DILEMMA_LOCATION = os.path.dirname(os.path.dirname(mod))


TOURNAMENT_LOCATION = os.path.join(PRISONERS_DILEMMA_LOCATION, "tournament")
MODULE_LOCATION = os.path.join(TOURNAMENT_LOCATION, "pd.py")
MODULE_2_LOCATION = os.path.join(TOURNAMENT_LOCATION, "pd_2.py")
MODULE_3_LOCATION = os.path.join(TOURNAMENT_LOCATION, "pd_3.py")
INFO_LOCATION = os.path.join(PRISONERS_DILEMMA_LOCATION, "info.py")
INFO_LOCATION_2 = os.path.join(PRISONERS_DILEMMA_LOCATION, "info_2.py")

team_name = '?'
strategy_name = '3'
strategy_description = 'Make others lose points, but help teammate.'

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

#print("updated modules: " + str(updated_modules))
total_num_of_rounds = len(updated_modules)
strategies = []
for i in range(total_num_of_rounds):
    if updated_modules[i] == MODULE_LOCATION:
        strategies.append("COLLUDE")
    elif updated_modules[i] == MODULE_3_LOCATION:
        pass
    else:
        strategies.append("BETRAY")

#print("pd_3 strategies: " + str(strategies))

#Starting at round 0...
ROUND_NUM_3 = -1

def move(my_history, their_history, my_score, their_score):
    global ROUND_NUM_3

    if len(my_history) == 0:
        ROUND_NUM_3 = ROUND_NUM_3 + 1

    try:
        what_to_do = strategies[ROUND_NUM_3]
    except:
        what_to_do = "BETRAY"
    #print("what to do: "+ str(what_to_do)+ " ROUND_NUM: " + str(ROUND_NUM))

    if what_to_do == "COLLUDE":
        return 'c'
    elif what_to_do == "BETRAY":
        return 'b'
    else:
        return 'b'
