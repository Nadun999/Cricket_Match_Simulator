from openpyxl import load_workbook
import random
import pandas as pd
from operator import itemgetter


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
