from openpyxl import load_workbook
import random
import pandas as pd
from operator import itemgetter


def first_innings():
    global filename_match
    global first_ing_total
    global first_ing_wickets
    global df_score_card_first_ing_without_index
    global df_bowler_list_first_ing_without_index
    first_ing_total = 0
    first_ing_wickets = 0
    first_ing_balls = 1
    score_card_first_ing = []

    batsman_onstrike = [['name', 0, 0], True]
    batsman_offstrike = [['name', 0, 0], False]

    bowler_onstrike = []

    # batsman_name , runs , balls_faced , method of dismissal , bowler
    # importing batting team
    batting_url = team_to_bat[1]
    batting_team = pd.read_excel(batting_url)
    # converting excel to python list
    yet_to_bat = batting_team.values.tolist()

    # bowlers_name , first_ing_balls , runs , wickets , economy
    # importing bowling team
    bowling_url = team_to_bowl[1]
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

    while (first_ing_balls < (TOTAL_BALLS+1)):
        if first_ing_wickets == TOTAL_WICKETS:
            break
        else:
            if ((first_ing_balls-1) > 0 and (first_ing_balls-1) % 6 == 0) and (len(yet_to_bowl)) > 0:
                yet_to_bowl.append(bowler_onstrike)
                bowler_onstrike = yet_to_bowl.pop(0)

            # get random scores for bowler and batsman
            bowler_score = random.randint(1, 6)
            batter_score = random.randint(0, 6)

            if bowler_score == batter_score:
                # adding wickets to bowler
                current_bowler_onstrike_first_ing_wickets = 0
                current_bowler_onstrike_first_ing_wickets = bowler_onstrike[3]
                bowler_onstrike[3] = current_bowler_onstrike_first_ing_wickets + 1
                # adding first_ing_balls to batsman
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
                print('FOW at', first_ing_total, ' --> ', first_ing_wickets+1,
                      ' on over -', int(first_ing_balls/6), '.', (first_ing_balls) % 6, batsman_onstrike[0][0])

                # bring new batsman to the crease (batsman_onstrike)
                if len(yet_to_bat) > 0:
                    batsman_onstrike[0] = []
                    batsman_onstrike[0] = yet_to_bat.pop(0)

                # out - add wicket to wickets
                first_ing_wickets += 1

            else:
                # adding batter_score to current_batsman
                current_batsman_onstrike_score = 0
                current_batsman_onstrike_score = batsman_onstrike[0][1]
                batsman_onstrike[0][1] = current_batsman_onstrike_score + batter_score

                # adding first_ing_balls to current_batsman
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

                # add batter score to first_ing_total
                first_ing_total += batter_score

                # adding extras to the total
                # extras_first_ing = random.randint(1,10)                                                       #check this
                # first_ing_total += extras

        # adding first_ing_balls to bowler
        current_bowler_onstrike_balls = 0
        current_bowler_onstrike_balls = bowler_onstrike[1]
        bowler_onstrike[1] = current_bowler_onstrike_balls + 1

        # adding first_ing_balls to first_ing ball count
        first_ing_balls += 1

    # last dismissed batsman
    last_dismissal = dismissed_batsmen[-1]

    # add dismissed_batsmen to batsman_list
    batsman_list = dismissed_batsmen

    # add each batsman in yet_to_bat to batsman_list array for displaying purposes
    if len(yet_to_bat) > 0:
        for i in range(len(yet_to_bat)):
            batsman_list.append(yet_to_bat[i])

    # add on and off strike batsmen to batsman_list
    if first_ing_wickets != TOTAL_WICKETS:
        batsman_onstrike[0][3] = '* NOT OUT'
        batsman_list.append(batsman_onstrike[0])

    batsman_offstrike[0][3] = 'NOT OUT'
    batsman_list.append(batsman_offstrike[0])

    # add batsman_list to score_card_first_ing
    score_card_first_ing = batsman_list

    # add bowlers to bowler_list_first_ing
    bowler_list_first_ing = yet_to_bowl
    bowler_list_first_ing.append(bowler_onstrike)

    # sort score_card_first_ing to the original batting order
    sorted_list = sorted(score_card_first_ing, key=itemgetter(5))

    # convert score_card_first_ing to a data frame for displaying
    df_score_card_first_ing = pd.DataFrame(sorted_list)

    # converting bowler first_ing_balls to overs
    for bowler_overs_first_ing in bowler_list_first_ing:
        bowler_overs_first_ing[1] = str(
            int((bowler_overs_first_ing[1])/6)) + '.' + str((bowler_overs_first_ing[1]) % 6)

    # additing the economy for bowler
    for bowler_economy_first_ing in bowler_list_first_ing:
        bowler_economy_first_ing[4] = round(
            bowler_economy_first_ing[2]/float(bowler_economy_first_ing[1]), 2)

    # convert df_bowler_list_first_ing to a data frame for displaying
    df_bowler_list_first_ing = pd.DataFrame(bowler_list_first_ing)

    print('\nTotal-', first_ing_total, '\nwickets -', first_ing_wickets,
          '\novers -', int((first_ing_balls-1)/6), '.', (first_ing_balls-1) % 6, '\nballs', (first_ing_balls-1))
    # print('Extras - ',extras_first_ing)
    print('\nLast dismissal', last_dismissal)

    new_headers = ['Batting', 'Runs', 'Balls Faced',
                   'MOD', 'Bowler', 'Batting No']
    df_score_card_first_ing.columns = new_headers
    df_score_card_first_ing_without_index = df_score_card_first_ing.set_index(
        'Batting')
    print(df_score_card_first_ing_without_index)

    overs = str(int((first_ing_balls-1)/6)) + \
        '.' + str((first_ing_balls-1) % 6)
    first_ing_summary = [
        [first_ing_total, first_ing_wickets, overs, (first_ing_balls-1)]]

    df_first_ing_summary = pd.DataFrame(first_ing_summary, columns=[
                                        'Total', 'Wickets', 'Overs', 'Balls'])
    print(df_first_ing_summary.to_string(index=False))

    new_headers = ['Bowling', 'Overs', 'Runs', 'Wickets', 'Economy']
    df_bowler_list_first_ing.columns = new_headers
    df_bowler_list_first_ing_without_index = df_bowler_list_first_ing.set_index(
        'Bowling')
    print(df_bowler_list_first_ing_without_index)

    # -------------## Write data to excel file by creating Excel Writer Object from Pandas -------------------------------------------

    filename_match = str(visiting_team[0]) + '_vs_' + str(home_team[0])
    match_file_path = r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\tournament\\matches\\' + filename_match + '.xlsx'

    writer = pd.ExcelWriter(match_file_path, engine='xlsxwriter')
    workbook = writer.book
    worksheet = workbook.add_worksheet('Validation')
    writer.sheets['Validation'] = worksheet

    df_score_card_first_ing.to_excel(
        writer, sheet_name='Validation', startrow=0, startcol=0, index=False)

    df_first_ing_summary.to_excel(
        writer, sheet_name='Validation', startrow=14, startcol=0, index=False)
    # first_ing_total.to_excel(writer,sheet_name='Validation',startrow=15 , startcol=0, index=False)
    # first_ing_wickets.to_excel(writer,sheet_name='Validation',startrow=16 , startcol=0, index=False)

    df_bowler_list_first_ing.to_excel(
        writer, sheet_name='Validation', startrow=19, startcol=0, index=False)

    writer.save()
    writer.close()
