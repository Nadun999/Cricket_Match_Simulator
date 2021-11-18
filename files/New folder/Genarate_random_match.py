import random


A = 'Mumbai_Indians'
B = 'Chennai_Superkings'
C = 'Delhi_Capitals'
D = 'RoyalChallengers_Bangalore'
E = 'Rajastan_Royals'
F = 'Kolkata_Knightriders'
G = 'Punjab_Kings'
H = 'Sunrisers_Hyderabad'

Group_A = [A, B, G, H]
Group_B = [C, D, E, F]

x = random.sample(Group_A, 2)
y = random.sample(Group_B, 2)
print(x, y)
