import random

total = 0
wickets = 0
balls = 1
TOTAL_WICKETS = 2
score_card = []

batsman_onstrike = [['name', 0, 0], True]
batsman_offstrike = [['name', 0, 0], False]


yet_to_bat = [['Sanath', 0, 0], ['Russel', 0, 0], ['Mahela', 0, 0]]
dismissed_batsmen = []


bowler_score = 0  # score counting variable for bowler
batter_score = 0  # score counting variable for batsman

# opening batsmen coming to the field
batsman_onstrike[0] = yet_to_bat.pop(0)
batsman_offstrike[0] = yet_to_bat.pop(0)


while balls < 60:
    if wickets == TOTAL_WICKETS:
        break
    else:
        # get random scores for bowler and batsman
        bowler_score = random.randint(1, 6)
        batter_score = random.randint(0, 6)

        if bowler_score == batter_score:
            current_batsman_onstrike_balls = batsman_onstrike[0][2]
            batsman_onstrike[0][2] = current_batsman_onstrike_balls + 1
            dismissed_batsmen.append(batsman_onstrike[0])
            # batsman_onstrike[0] = [['name' , 0] , True]
            if len(yet_to_bat) > 0:
                batsman_onstrike[0] = []
                batsman_onstrike[0] = yet_to_bat.pop(0)
                # out - add wicket to wickets
            wickets += 1
        else:
            current_batsman_onstrike_score = 0
            # adding batter_score to current_batsman
            current_batsman_onstrike_score = batsman_onstrike[0][1]
            batsman_onstrike[0][1] = current_batsman_onstrike_score + batter_score
            current_batsman_onstrike_balls = batsman_onstrike[0][2]
            batsman_onstrike[0][2] = current_batsman_onstrike_balls + 1
            if batter_score == 1 or batter_score == 3:
                current_batsman = batsman_onstrike[0]
                # swapping onstrike batsmen
                batsman_onstrike[0] = batsman_offstrike[0]
                batsman_offstrike[0] = current_batsman
            else:
                pass  # when batter_score is not swapping

            # add batter score to total
            total += batter_score
    balls += 1

score_card.append(dismissed_batsmen)
score_card.append([batsman_offstrike[0], '*'])


print(' total-', total, ' wickets -', wickets, ' overs -',
      int(balls/6), '.', (balls-1) % 6, ' balls', (balls-1))
last_dismissal = batsman_onstrike[0]
print('Last dismissal', last_dismissal)
batsman_onstrike[0] = []
print(score_card)
