import random
import time

team1_name = "Arsenal"
team1_rank = 1
team2_name = "Chelsea"
team2_rank = 10

team1_chance = 20 - team1_rank
team2_chance = 20 - team2_rank

team1_chance += random.randint(0, 20)
team2_chance += random.randint(0, 20)

print("The pickalator is now choosing a winner..\n")
time.sleep(2)

print("... almost there..\n")
time.sleep(2)

if team1_chance >= team2_chance:
    confidence = (team1_chance - team2_chance) / 31 * 100
    print(f'The pickalator has chosen: {team1_name} with {int(confidence)}% confidence')
else:
    confidence = (team2_chance - team1_chance) / 31 * 100
    print(f'The pickalator has chosen: {team2_name} with {int(confidence)}% confidence')

print(f'team1_chance: {team1_chance}')
print(f'team2_chance: {team2_chance}')