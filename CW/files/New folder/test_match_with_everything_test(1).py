import random


total = 0
wickets = 0
balls = 1
TOTAL_WICKETS = 10
score_card = []

batsman_onstrike = [['name', 0, 0], True]
batsman_offstrike = [['name', 0, 0], False]

bowler_onstrike = []


# batsman_name , runs , balls_faced , method of dismissal , bowler
yet_to_bat = [['Sanath', 0, 0, '', ''], [
    'Russel', 0, 0, '', ''], ['Mahela', 0, 0, '', ''], ['Charith', 0, 0, '', ''], ['Pathum', 0, 0, '', ''], ['Bhanuka', 0, 0, '', ''], ['Dasun', 0, 0, '', ''], ['Chandimal', 0, 0, '', ''], ['Mathews', 0, 0, '', ''], ['Dimuth', 0, 0, '', ''], ['Thirimanne', 0, 0, '', '']]
dismissed_batsmen = []


# bowlers_name , balls , runs , wickets
yet_to_bowl = [['Vass', 0, 0, 0], ['Murali', 0, 0, 0],
               ['Wanindu', 0, 0, 0], ['Chameera', 0, 0, 0], ['Chamika', 0, 0, 0]]

# method of dismissal
method_of_dismissal = ['Bowled', 'Caught', 'LBW']


bowler_score = 0  # score counting variable for bowler
batter_score = 0  # score counting variable for batsman


# opening batsmen coming to the field
batsman_onstrike[0] = yet_to_bat.pop(0)
batsman_offstrike[0] = yet_to_bat.pop(0)

# opening bowler
bowler_onstrike = yet_to_bowl.pop(0)


while balls < 60:
    if wickets == TOTAL_WICKETS:
        break
    else:
        if ((balls-1) > 0 and (balls-1) % 6 == 0) and (len(yet_to_bowl)) > 0:
            yet_to_bowl.append(bowler_onstrike)
            # bowler_onstrike[0] = []
            bowler_onstrike = yet_to_bowl.pop(0)

        # get random scores for bowler and batsman
        bowler_score = random.randint(1, 6)
        batter_score = random.randint(0, 6)

        if bowler_score == batter_score:
            # adding wickets to bowler
            current_bowler_onstrike_wickets = 0
            current_bowler_onstrike_wickets = bowler_onstrike[3]
            bowler_onstrike[3] = current_bowler_onstrike_wickets + 1
            # adding balls to batsman
            current_batsman_onstrike_balls = batsman_onstrike[0][2]
            batsman_onstrike[0][2] = current_batsman_onstrike_balls + 1
            dismissed_batsmen.append(batsman_onstrike[0])
            # adding method of dismissal to batsman
            current_batsman_method_of_dismissal = random.choices(
                method_of_dismissal)
            batsman_onstrike[0][3] = current_batsman_method_of_dismissal[0]

            # adding dismissed bowler name to batsman
            current_batsman_bowler_dismissed = batsman_onstrike[0][4]
            batsman_onstrike[0][4] = current_batsman_bowler_dismissed + \
                str(bowler_onstrike[0])

            if len(yet_to_bat) > 0:
                batsman_onstrike[0] = []
                batsman_onstrike[0] = yet_to_bat.pop(0)
                # out - add wicket to wickets
            wickets += 1

            # fall of wickets
            print('FOW', total, ' --> ', wickets, ' on over -',
                  int(balls/6), '.', (balls) % 6)

        else:
            # adding batter_score to current_batsman
            current_batsman_onstrike_score = 0
            current_batsman_onstrike_score = batsman_onstrike[0][1]
            batsman_onstrike[0][1] = current_batsman_onstrike_score + batter_score
            # adding balls to current_batsman
            current_batsman_onstrike_balls = batsman_onstrike[0][2]
            batsman_onstrike[0][2] = current_batsman_onstrike_balls + 1

            # adding batter_score to current_bowler
            current_bowler_onstrike_runs = 0
            current_bowler_onstrike_runs = bowler_onstrike[2]
            bowler_onstrike[2] = current_bowler_onstrike_runs + batter_score

            if batter_score == 1 or batter_score == 3:
                current_batsman = batsman_onstrike[0]
                # swapping onstrike batsmen
                batsman_onstrike[0] = batsman_offstrike[0]
                batsman_offstrike[0] = current_batsman
            else:
                pass  # when batter_score is not swapping

            # add batter score to total
            total += batter_score

    # adding balls to bowler
    current_bowler_onstrike_balls = 0
    current_bowler_onstrike_balls = bowler_onstrike[1]
    bowler_onstrike[1] = current_bowler_onstrike_balls + 1
    balls += 1


score_card.append(dismissed_batsmen)
score_card.append([batsman_offstrike[0], '*'])

print(' total-', total, ' wickets -', wickets, ' overs -',
      int(balls/6), '.', (balls-1) % 6, ' balls', (balls-1))  # """check overs and balls !!!!!!! """
last_dismissal = batsman_onstrike[0]
print('Last dismissal', last_dismissal)
batsman_onstrike[0] = []
print(score_card)

print(yet_to_bowl, bowler_onstrike)
