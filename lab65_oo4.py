class Team:
    name = "Normal Team"

team1 = Team()
print(team1.name)
team1.name = "R&D Team"
print(team1.name)


del team1.name
print(team1.name)

team1.member = 7

print(team1.name,team1.member)