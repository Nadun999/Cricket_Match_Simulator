# ----------------------------------------------------------------------------------------------------Importing Modules--------------------------------------------------------------------------------------------------
import modulesss
from openpyxl import load_workbook
import random
import pandas as pd
from operator import itemgetter
# ---------------------------------------------------------------------------------Global variables which are used when accessing the functions---------------------------------------------------------------------------

user_input = ''
global_exit = ''


print("\n\n----------------------------------------------------------------------------------Welcome to IIT Cricket Premier League 2021-------------------------------------------------------------------------------")

while user_input != 'x':
    user_input = input(
        "\n\nPress the desired number for your action... \n\nPlay a new match - 1 \nView/edit team/player profile - 2 \nView PLayer Standings - 3 \npress 'x' to exit...  ")

    if user_input == '1':
        modulesss.generate_random_match()
        modulesss.points_table()
        modulesss.toss()
        modulesss.first_innings()
        modulesss.second_innings()
        modulesss.match_summary()
    elif user_input == '2':
        modulesss.team_profile_edit(user_input)
        global_exit = ''
    elif user_input == '3':
        modulesss.display_player_standings()
    elif user_input == 'x':
        break
    else:
        print('Input value incorrect \nTry again!!!\n')

print("\n\n--------------------------------------------------------------------------------------------Thank you for playing!!!----------------------------------------------------------------------------------------")
