from openpyxl import load_workbook
import random
import pandas as pd
from operator import itemgetter

Group_A = [Mumbai_India, Chennai_SouthAfrica,
           Delhi_NewZealand, RoyalChallengers_Bangladesh]
Group_B = [Rajastan_Australia, Kolkata_England,
           Punjab_Pakistan, Sunrisers_SriLanka]


def generate_random_match():
    match_between_A = random.sample(Group_A, 2)
    match_between_B = random.sample(Group_B, 2)

    chosen_match = [match_between_A, match_between_B]
    global match_between
    match_between = random.choice(chosen_match)
    print(match_between)
