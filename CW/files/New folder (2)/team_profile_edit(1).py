from openpyxl import load_workbook
import random
import pandas as pd
from operator import itemgetter


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
