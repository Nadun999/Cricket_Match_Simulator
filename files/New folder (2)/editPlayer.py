from openpyxl import load_workbook
import random
import pandas as pd
from operator import itemgetter


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
