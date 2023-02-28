from openpyxl import load_workbook
import random
import pandas as pd
from operator import itemgetter


def toss():
    coin = ["heads", "tails"]
    options = ['bat', 'bowl']
    global team_to_bat
    global team_to_bowl
    global visiting_team
    global home_team
    global selection
    global toss
    global choose

    visiting_team = random.choice(match_between)

    if visiting_team in match_between:
        match_between.remove(visiting_team)

    home_team = match_between[0]

    # This simulates the coin being tossed
    toss = random.choice(coin)
    # This simulates the visiting team choose head or tails
    selection = random.choice(coin)
    # This simulates the visiting team choose bat or bowl
    choose = random.choice(options)

    print('Home Team - ', home_team[0])
    print('Visiting Team - ', visiting_team[0])

    if selection == toss:
        print(visiting_team[0], 'won the toss and chose to', choose)
        if choose == options[0]:
            team_to_bat = visiting_team
            team_to_bowl = home_team
        else:
            team_to_bat = home_team
            team_to_bowl = visiting_team

    else:
        print(home_team[0], 'won the toss and chose to', choose)
        if choose == options[0]:
            team_to_bat = home_team
            team_to_bowl = visiting_team
        else:
            team_to_bat = visiting_team
            team_to_bowl = home_team

    print('team_to_bat', team_to_bat[0])
    print('team_to_bowl', team_to_bowl[0])
