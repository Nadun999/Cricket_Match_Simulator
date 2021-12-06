# ----------------------------------------------------------------------------------------------------Importing Modules--------------------------------------------------------------------------------------------------
from openpyxl import load_workbook
import random
import pandas as pd
from operator import itemgetter
# ------------------------------------------------------------------------------------------Store information about teams and players.-----------------------------------------------------------------------------------
Mumbai_India = ['Mumbai_India',
                r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\Mumbai_India\\Mumbai_India.xlsx']
Chennai_SouthAfrica = ['Chennai_SouthAfrica',
                       r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\Chennai_SouthAfrica\\Chennai_SouthAfrica.xlsx']
Delhi_NewZealand = ['Delhi_NewZealand',
                    r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\Delhi_NewZealand\\Delhi_NewZealand.xlsx']
RoyalChallengers_Bangladesh = ['RoyalChallengers_Bangladesh',
                               r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\RoyalChallengers_Bangladesh\\RoyalChallengers_Bangladesh.xlsx']
Rajastan_Australia = ['Rajastan_Australia',
                      r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\Rajastan_Australia\\Rajastan_Australia.xlsx']
Kolkata_England = ['Kolkata_England',
                   r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\Kolkata_England\\Kolkata_England.xlsx']
Punjab_Pakistan = ['Punjab_Pakistan',
                   r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\Punjab_Pakistan\\Punjab_Pakistan.xlsx']
Sunrisers_SriLanka = ['Sunrisers_SriLanka',
                      r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\Sunrisers_SriLanka\\Sunrisers_SriLanka.xlsx']

# ------------------------------------------------------------------------------------------------- Assigning teams to groups--------------------------------------------------------------------------------------------------------------------------------------------
Group_A = [Mumbai_India, Chennai_SouthAfrica,
           Delhi_NewZealand, RoyalChallengers_Bangladesh]
Group_B = [Rajastan_Australia, Kolkata_England,
           Punjab_Pakistan, Sunrisers_SriLanka]
# ----------------------------------------------------------------------------------------Global variables which are used in the functions--------------------------------------------------------------------------------------------------------------------------------

user_input = ''
global_exit = ''
TOTAL_WICKETS = 10
TOTAL_BALLS = 120
first_ing_total = 0
first_ing_wickets = 0
second_ing_total = 0
second_ing_wickets = 0
match_between = []
team_to_bat = []
team_to_bowl = []
visiting_team = []
home_team = []
filename_match = ''
selection = ''
toss = ''
choose = ''
df_score_card_first_ing_without_index = []
df_bowler_list_first_ing_without_index = []
df_score_card_second_ing_without_index = []
df_bowler_list_second_ing_without_index = []


print("\n\n----------------------------------------------------------------------------------Welcome to IIT Cricket Premier League 2021------------------------------------------------------------------------------------")


def GetTeam(teamName):
    print(GetTeam)
    df = pd.read_excel(
        r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\'+teamName+'\\'+teamName+'.xlsx')
    editable_options = df.iloc[:, :1]
    print(editable_options)


def EditTeam(teamName, row, col, edited_name):
    df = pd.read_excel(
        r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\'+teamName+'\\'+teamName+'.xlsx')
    df.at[row, col] = edited_name
    print(df.iloc[:, 0])
    df.to_excel(
        r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\'+teamName+'\\'+teamName+'.xlsx', index=False)


def editPlayer(teamName):
    GetTeam(teamName)
    editTeam = input(
        f"Do you want to make any changes on team {teamName}? \n1 - yes \n0 - no ")
    if editTeam == '0':
        global global_exit
        global_exit = 'y'
    while editTeam == '1':
        row = int(input(
            "Which player do you want to edit? \nSelect the corresponding row number :  "))
        col = input("Column name you want to edit? ").upper()
        val = input("What should be the change then? ")
        EditTeam(teamName, row, col, val)
        print("your changes have been saved successfully !!!")
        # \nOr press 'x' to exit...
        editTeam = input(
            f"Do you want to make any more changes on team {teamName} again?\n1 - yes \n0 - no ")


def team_profile_edit(getData):
    while (getData == '2') and (global_exit != 'y'):
        getGroup = input(
            "Which group do you want to see? \n1 - group A \n2 - group B \nOr press 'x' to exit...     ")
        if getGroup == 'x':
            break

        elif getGroup == '1':
            getTeam = input("Which team do you want to see? \n1 - Mumbai India \n2 - Chennai SouthAfrica \n3 - Delhi NewZealand \n4 - RoyalChallengers Bangladesh \n Select a number from 1 to 4 \nOr press 'x' to exit...       ")
            if getTeam == 'x':
                break
            if getTeam == '1':
                editPlayer('Mumbai_India')

            elif getTeam == '2':
                editPlayer('Chennai_SouthAfrica')

            elif getTeam == '3':
                editPlayer('Delhi_NewZealand')

            elif getTeam == '4':
                editPlayer('RoyalChallengers_Bangladesh')

        elif getGroup == '2':
            getTeam = input(
                "Which team do you want to see? \n1 - Rajastan Australia \n2 - Kolkata England \n3 - Punjab Pakistan \n4 - Sunrisers SriLanka \n Select a number from 1 to 4")

            if getTeam == '1':
                editPlayer('Rajastan_Australia')

            elif getTeam == '2':
                editPlayer('Kolkata_England')

            elif getTeam == '3':
                editPlayer('Punjab_Pakistan')

            elif getTeam == '4':
                editPlayer('Sunrisers_SriLanka')


def generate_random_match():
    match_between_A = random.sample(Group_A, 2)
    match_between_B = random.sample(Group_B, 2)

    chosen_match = [match_between_A, match_between_B]
    global match_between
    match_between = random.choice(chosen_match)
    print(match_between)


def points_table():
    points_table = pd.read_excel(
        r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\tournament\\points_table.xlsx')
    df_points_table = pd.DataFrame(points_table)
    df_points_table

    for team in match_between:

        if(team in Group_A):
            group = "Group A"
        else:
            group = "Group B"
        find_team_index = df_points_table.index[df_points_table[group] == team[0]].tolist(
        )
        if(group == "Group A"):
            current_match_count = df_points_table.at[find_team_index[0], 'Matches_A']
            df_points_table.at[find_team_index,
                               'Matches_A'] = current_match_count+1
        else:
            current_match_count = df_points_table.at[find_team_index[0], 'Matches_B']
            df_points_table.at[find_team_index,
                               'Matches_B'] = current_match_count+1
        print(find_team_index, group, current_match_count)

    print(df_points_table)

    # ----------------------------------------## Write data to excel file by creating Excel Writer Object from Pandas ----------------------

    writer = pd.ExcelWriter(
        r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\tournament\\points_table.xlsx', engine='xlsxwriter')
    workbook = writer.book
    worksheet = workbook.add_worksheet('Validation')
    writer.sheets['Validation'] = worksheet
    df_points_table.to_excel(writer, sheet_name='Validation',
                             startrow=0, startcol=0, index=False)

    writer.save()
    writer.close()


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


# def team3And4():
#     global df1, df_team3, df_team4, players_name, player, runs, score, wickets, wic_count
#     global top_batsman, top_bowlers, name_id, name, wicket, i

#     df1 = pd.read_excel(
#         r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\tournament\\top5.xlsx')
#     df_team3 = pd. read_excel(
#         r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\Chennai_SouthAfrica\\Chennai_SouthAfrica_B.xlsx')
#     df_team4 = pd.read_excel(
#         r'E:\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\Delhi_NewZealand\\Delhi_NewZealand_B.xlsx')

#     for players_name in range(11):
#         player = df_team3['PLAYER NAME'][players_name]
#         df1.at[players_name + 22, 'PLAYER NAME'] = player
#         df1.to_excel(
#             r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\tournament\\top5.xlsx', index=False)

#     for runs in range(11):
#         score = df_team3['Runs'][runs] + df1['TOTAL RUNS'][runs + 22]
#         df1.at[runs + 22, 'TOTAL RUNS'] = score
#         df1.to_excel(
#             'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\tournament\\top5.xlsx', index=False)

#     for wickets in range(11):
#         wic_count = df_team3['Wickets'][wickets] + df1['WICKETS'][wickets + 22]
#         df1.at[wickets + 22, 'WICKETS'] = wic_count
#         df1.to_excel(
#             'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\tournament\\top5.xlsx', index=False)

    # for players_name in range(11):
    #     player = df_team4['PLAYER NAME'][players_name]
    #     df1.at[players_name + 33, 'PLAYER NAME'] = player
    #     df1.to_excel(
    #         'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\tournament\\top5.xlsx', index=False)

    # for runs in range(11):
    #     score = df_team4['Runs'][runs] + df1['TOTAL RUNS'][runs + 33]
    #     df1.at[runs + 33, 'TOTAL RUNS'] = score
    #     df1.to_excel(
    #         r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\tournament\\top5.xlsx', index=False)

    # for wickets in range(11):
    #     wic_count = df_team4['Wickets'][wickets] + df1['WICKETS'][wickets + 33]
    #     df1.at[wickets + 33, 'WICKETS'] = wic_count
    #     df1.to_excel(
    #         'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\tournament\\top5.xlsx', index=False)

    # df1 = pd. read_excel(
    #     r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\tournament\\top5.xlsx')
    # top_batsman = df1['TOTAL RUNS'].nlargest(5)
    # top_bowlers = df1['WICKETS'].nlargest(5)

    # print("TOP 5 BATSMAN....")
    # for i in range(5):
    #     name_id = top_batsman.index[i]
    #     name = df1['PLAYER NAME'][name_id]
    #     runs = df1['TOTAL RUNS'][name_id]
    #     print(name, ' = ', runs)
    # print(' ')
    # print("TOP 5 WICKET TAKERS...")


while user_input != 'x':
    user_input = input(
        "\n\nPress the desired number for your action... \n\nPlay a new match - 1 \nView/edit team/player profile - 2 \npress 'x' to exit...  ")

    if user_input == '1':
        generate_random_match()
        points_table()
        toss()
        first_innings()
        second_innings()
        match_summary()
        # team3And4()
    elif user_input == '2':
        team_profile_edit(user_input)
        global_exit = ''
    elif user_input == 'x':
        break
    else:
        print('Input value incorrect \nTry again\n')

print("\n-------------------------------------------------------Thank you for playing!!!-------------------------------------------------------")
