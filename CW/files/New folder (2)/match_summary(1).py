from openpyxl import load_workbook
import random
import pandas as pd
from operator import itemgetter


def match_summary():
    # Toss

    if selection == toss:
        print(visiting_team[0].replace('_', ' '),
              'won the toss and chose to', choose)
    else:
        print(home_team[0].replace('_', ' '),
              'won the toss and chose to', choose)

    # first innings top performers

    print(team_to_bat[0].replace('_', ' '))
    print(df_score_card_first_ing_without_index.nlargest(4, 'Runs'))

    print('\n', team_to_bowl[0].replace('_', ' '))
    print(df_bowler_list_first_ing_without_index.nlargest(3, 'Wickets'))

    print('\nTotal', first_ing_total, '/', first_ing_wickets)

    # second innings top performers

    print(team_to_bowl[0].replace('_', ' '))
    print(df_score_card_second_ing_without_index.nlargest(4, 'Runs'))

    print('\n', team_to_bat[0].replace('_', ' '))
    print(df_bowler_list_second_ing_without_index.nlargest(3, 'Wickets'))

    print('\nTarget', first_ing_total+1)
    print('Total', second_ing_total, '/', second_ing_wickets)

    # Match result

    if (second_ing_total > first_ing_total):
        # print('second_ing_total',second_ing_total)
        print(team_to_bowl[0].replace('_', ' '), 'Won by',
              TOTAL_WICKETS-second_ing_wickets, 'wickets')
    elif (second_ing_total < first_ing_total):
        # print('first_ing_total',first_ing_total)
        print(team_to_bat[0].replace('_', ' '), 'Won by',
              (first_ing_total-second_ing_total), 'runs')
    else:
        print('Match drawn')
