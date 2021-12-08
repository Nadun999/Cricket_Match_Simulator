# ----------------------------------------------------------------------------------------------------Importing Modules-----------------------------------------------------------------------------------------------
import cricket
from openpyxl import load_workbook
import random
import pandas as pd
from operator import itemgetter
# ---------------------------------------------------------------------------------Global variables which are used when accessing the functions------------------------------------------------------------------------

user_input = ''
global_exit = ''
winning_team = []
losing_team = []
# match_between = []

print("\n\n-------------------------------------------------------------------------------Welcome to IIT Cricket Premier League 2021----------------------------------------------------------------------------------")

try:
    while user_input != 'x':
        user_input = input(
            "\n\nPress the desired number for your action... \n\nPlay a new match - 1 \nView/edit team/player profile - 2 \nView Player Standings - 3 \nView Tournament Standings - 4 \nPress 'x' to exit...  ")

        if user_input == '1':
            cricket.generate_random_match()
            cricket.points_table()
            cricket.toss()
            cricket.first_innings()
            cricket.second_innings()
            cricket.match_summary()
        elif user_input == '2':
            cricket.team_profile_edit(user_input)
            global_exit = ''
        elif user_input == '3':
            cricket.display_player_standings()
        elif user_input == '4':
            cricket.display_points_table()
        elif user_input == 'x':
            break
        else:
            print('Input value incorrect \nTry again!!!\n')
except Exception:
    print('\n------------------------------------------------------------------------------------------TOURNAMENT OVER----------------------------------------------------------------------------------\n')


print("\n\n-------------------------------------------------------------------------------------- --Thank you for playing!!!------------------------------------------------------------------------------------------")
