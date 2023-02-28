from openpyxl import load_workbook
import random
import pandas as pd
from operator import itemgetter


def EditTeam(teamName, row, col, edited_name):
    df = pd.read_excel(
        r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\'+teamName+'\\'+teamName+'.xlsx')
    df.at[row, col] = edited_name
    print(df.iloc[:, 0])
    df.to_excel(
        r'E:\\IIT\\1st Year\\1st Trimester\\CM1601 [PRO]  Programming Fundamentals\\Course Work\\team_data\\'+teamName+'\\'+teamName+'.xlsx', index=False)
