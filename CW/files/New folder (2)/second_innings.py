from openpyxl import load_workbook
import random
import pandas as pd
from operator import itemgetter


def second_innings():
    global second_ing_total
    global second_ing_wickets
    global df_score_card_second_ing_without_index
    global df_bowler_list_second_ing_without_index
    second_ing_total = 0
    second_ing_wickets = 0
    second_ing_balls = 1
    score_card_second_ing = []

    batsman_onstrike = [['name', 0, 0], True]
    batsman_offstrike = [['name', 0, 0], False]

    bowler_onstrike = []

    # batsman_name , runs , balls_faced , method of dismissal , bowler
    # importing batting team
    batting_url = team_to_bowl[1]
    batting_team = pd.read_excel(batting_url)
    # converting excel to python list
    yet_to_bat = batting_team.values.tolist()

    # bowlers_name , second_ing_balls , runs , wickets
    # importing bowling team
    bowling_url = team_to_bat[1]
    bowling_team = pd.read_excel(bowling_url)
    # converting excel to python list
    bowling_team_list = bowling_team.values.tolist()

    yet_to_bowl = []

    for i in reversed(range(len(bowling_team_list))):
        if len(yet_to_bowl) < 5:
            yet_to_bowl.append([bowling_team_list[i][0], 0, 0, 0, 0])

    dismissed_batsmen = []
    batsman_list = []

    # method of dismissal
    method_of_dismissal = ['Bowled', 'Caught', 'LBW']

    bowler_score = 0  # score counting variable for bowler
    batter_score = 0  # score counting variable for batsman

    # opening batsmen coming to the field
    batsman_onstrike[0] = yet_to_bat.pop(0)
    batsman_offstrike[0] = yet_to_bat.pop(0)

    # opening bowler
    bowler_onstrike = yet_to_bowl.pop(0)

    while (second_ing_balls < (TOTAL_BALLS+1)):
        if ((second_ing_wickets == TOTAL_WICKETS) or (second_ing_total > first_ing_total)):
            break
        else:
            if ((second_ing_balls-1) > 0 and (second_ing_balls-1) % 6 == 0) and (len(yet_to_bowl)) > 0:
                yet_to_bowl.append(bowler_onstrike)
                bowler_onstrike = yet_to_bowl.pop(0)

            # get random scores for bowler and batsman
            bowler_score = random.randint(1, 6)
            batter_score = random.randint(0, 6)

            if bowler_score == batter_score:
                # adding wickets to bowler
                current_bowler_onstrike_second_ing_wickets = 0
                current_bowler_onstrike_second_ing_wickets = bowler_onstrike[3]
                bowler_onstrike[3] = current_bowler_onstrike_second_ing_wickets + 1
                # adding second_ing_balls to batsman
                current_batsman_onstrike_balls = batsman_onstrike[0][2]
                batsman_onstrike[0][2] = current_batsman_onstrike_balls + 1

                # moving the dismissed_batsmen to dismissed_batsmen array
                dismissed_batsmen.append(batsman_onstrike[0])

                # adding method of dismissal to batsman
                current_batsman_method_of_dismissal = random.choices(
                    method_of_dismissal)
                batsman_onstrike[0][3] = current_batsman_method_of_dismissal[0]

                # adding dismissed bowler name to batsman
                current_batsman_bowler_dismissed = batsman_onstrike[0][4]
                batsman_onstrike[0][4] = current_batsman_bowler_dismissed + \
                    str(bowler_onstrike[0])

                # fall of wickets
                print('FOW', second_ing_total, ' --> ', second_ing_wickets+1,
                      ' on over -', int(second_ing_balls/6), '.', (second_ing_balls) % 6, batsman_onstrike[0][0])

                # bring new batsman to the crease (batsman_onstrike)
                if len(yet_to_bat) > 0:
                    batsman_onstrike[0] = []
                    batsman_onstrike[0] = yet_to_bat.pop(0)

                # out - add wicket to wickets
                second_ing_wickets += 1

            else:
                # adding batter_score to current_batsman
                current_batsman_onstrike_score = 0
                current_batsman_onstrike_score = batsman_onstrike[0][1]
                batsman_onstrike[0][1] = current_batsman_onstrike_score + batter_score

                # adding second_ing_balls to current_batsman
                current_batsman_onstrike_balls = batsman_onstrike[0][2]
                batsman_onstrike[0][2] = current_batsman_onstrike_balls + 1

                # adding batter_score to current_bowler
                current_bowler_onstrike_runs = 0
                current_bowler_onstrike_runs = bowler_onstrike[2]
                bowler_onstrike[2] = current_bowler_onstrike_runs + \
                    batter_score

                # swapping onstrike batsman when strike rotates
                if batter_score == 1 or batter_score == 3:
                    current_batsman = batsman_onstrike[0]
                    # swapping onstrike batsman
                    batsman_onstrike[0] = batsman_offstrike[0]
                    batsman_offstrike[0] = current_batsman
                else:
                    pass  # when batter_score is not swapping

                # add batter score to second_ing_total
                second_ing_total += batter_score

                # adding extras to the total
                # extras_second_ing = random.randint(1,10)                                                       #check this
                # second_ing_total += extras

        # adding second_ing_balls to bowler
        current_bowler_onstrike_balls = 0
        current_bowler_onstrike_balls = bowler_onstrike[1]
        bowler_onstrike[1] = current_bowler_onstrike_balls + 1
        second_ing_balls += 1

    # last dismissed batsman
    last_dismissal = dismissed_batsmen[-1]

    # add dismissed_batsmen to batsman_list
    batsman_list = dismissed_batsmen

    # add each batsman in yet_to_bat to batsman_list array for displaying purposes
    if len(yet_to_bat) > 0:
        for i in range(len(yet_to_bat)):
            batsman_list.append(yet_to_bat[i])

    # add on and off strike batsmen to batsman_list
    if second_ing_wickets != TOTAL_WICKETS:
        batsman_onstrike[0][3] = '* NOT OUT'
        batsman_list.append(batsman_onstrike[0])

    batsman_offstrike[0][3] = 'NOT OUT'
    batsman_list.append(batsman_offstrike[0])

    # add batsman_list to score_card_second_ing
    score_card_second_ing = batsman_list

    # sort score_card_second_ing to the original batting order
    sorted_list = sorted(score_card_second_ing, key=itemgetter(5))

    # add bowlers to bowler_list_second_ing
    bowler_list_second_ing = yet_to_bowl
    bowler_list_second_ing.append(bowler_onstrike)

    # convert df_score_card_second_ing to a data frame for displaying
    df_score_card_second_ing = pd.DataFrame(sorted_list)

    # converting bowler second_ing_balls to overs
    for bowler_overs_second_ing in bowler_list_second_ing:
        bowler_overs_second_ing[1] = str(
            int((bowler_overs_second_ing[1])/6)) + '.' + str((bowler_overs_second_ing[1]) % 6)

    # additing the economy for bowler
    for bowler_economy_second_ing in bowler_list_second_ing:
        bowler_economy_second_ing[4] = round(
            bowler_economy_second_ing[2]/float(bowler_economy_second_ing[1]), 2)

    # convert df_bowler_list_second_ing to a data frame for displaying
    df_bowler_list_second_ing = pd.DataFrame(bowler_list_second_ing)

    print('\nTotal-', second_ing_total, '\nwickets -', second_ing_wickets,
          '\novers -', int((second_ing_balls-1)/6), '.', (second_ing_balls-1) % 6, '\nballs', (second_ing_balls-1))
    # print('Extras',extras_second_ing)
    print('\nLast dismissal', last_dismissal)

    new_headers = ['Batting', 'Runs', 'Balls Faced',
                   'MOD', 'Bowler', 'Batting No']
    df_score_card_second_ing.columns = new_headers
    df_score_card_second_ing_without_index = df_score_card_second_ing.set_index(
        'Batting')
    print(df_score_card_second_ing_without_index)

    overs = str(int((second_ing_balls-1)/6)) + \
        '.' + str((second_ing_balls-1) % 6)
    second_ing_summary = [
        [second_ing_total, second_ing_wickets, overs, (second_ing_balls-1)]]

    df_second_ing_summary = pd.DataFrame(second_ing_summary, columns=[
        'Total', 'Wickets', 'Overs', 'Balls'])
    print(df_second_ing_summary.to_string(index=False))

    new_headers = ['Bowling', 'Overs', 'Runs', 'Wickets', 'Economy']
    df_bowler_list_second_ing.columns = new_headers
    df_bowler_list_second_ing_without_index = df_bowler_list_second_ing.set_index(
        'Bowling')
    print(df_bowler_list_second_ing_without_index)

    # --------## Write data to excel file by creating Excel Writer Object from Pandas -------------------------------------------

    book = load_workbook(
        r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\tournament\\matches\\' + filename_match + '.xlsx')
    writer = pd.ExcelWriter(
        r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\tournament\\matches\\' + filename_match + '.xlsx', engine='openpyxl')
    writer.book = book

    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

    df_score_card_second_ing.to_excel(
        writer, sheet_name='Validation', startrow=0, startcol=9, index=False)

    df_second_ing_summary.to_excel(
        writer, sheet_name='Validation', startrow=14, startcol=9, index=False)

    # second_ing_total.to_excel(writer,sheet_name='Validation',startrow=15 , startcol=9, index=False)
    # second_ing_wickets.to_excel(writer,sheet_name='Validation',startrow=16 , startcol=9, index=False)

    df_bowler_list_second_ing.to_excel(
        writer, sheet_name='Validation', startrow=19, startcol=9, index=False)

    writer.save()
    writer.close()
