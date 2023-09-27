import random
from lib.paladin import Paladin
from lib.mage import Mage

if __name__ == "__main__":
    print(f"aaaa")

teams = ["red", "blue"]
paladins = []

blue_mage = Mage("Blue Mage", 1, "blue")
red_mage = Mage("Red Mage", 2, "red")

blue_team = []
red_team = []

for i in range(20):
    rand = random.randint(0, 1)
    team = teams[rand]

    if team == "red":
        red_team.append(Paladin(f"Paladin {i}", i, teams[rand]))
    else:
        blue_team.append(Paladin(f"Paladin {i}", i, teams[rand]))

blue_count = len(blue_team)
red_count = len(red_team)

print(f"Blue Team: {blue_count}")
print(f"Red Team: {red_count}")

if blue_count > red_count:
    blue_mage.new_level(2)
    blue_mage.get_skills(["Fireball", "Iceball", "Lightning"])
else:
    red_mage.new_level(2)
    red_mage.get_skills(["Fireball", "Iceball", "Lightning"])


# random paladin from one of the teams
rand = random.randint(0, 1)
team = teams[rand]
paladin = blue_team[random.randint(0, blue_count - 1)] if team == "blue" else red_team[random.randint(0, red_count - 1)]
mage = blue_mage if team == "blue" else red_mage
paladin.go_to_mage(mage)

print(f"Mage: {mage.personId}")
print(f"Paladin: {paladin.personId}")
