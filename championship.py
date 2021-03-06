import random

teams = ['eg', 'sk', 'vega', 'rox', 'elements', 'albus', 'al', 'gg']
wins = 1 #количество побед в каждом раунде

playoff = {}
round_number = len(teams)//2
print("start teams: ", teams)


def check_team_number(teams):
	if len(teams)%2 and len(teams)!=1:
		quit("odd team number")


def init_pairs(teams):
	check_team_number(teams)
	pairs = []
	while teams:
		pairs.append([teams.pop(random.randrange(0, len(teams))),
					  teams.pop(random.randrange(0, len(teams)))])
	return pairs


def create_pairs(teams):
	check_team_number(teams)
	return [list(pairs) for pairs in zip(teams[::2], teams[1::2])]


def match(pair):
	match = {}
	result = random.randint(0, wins*2-1)
	if result < wins:
		first_team_result = wins
		second_team_result = result
	else:
		first_team_result = result - wins
		second_team_result = wins
	match.update({first_team_result:pair[0],
				  second_team_result:pair[1]})
	return match


def round(pairs):
	matches = []
	new_teams = []
	while pairs:
		matches.append(match(pairs.pop()))
	for i in matches:
		new_teams.append(i.get(wins))
	playoff.update({'1/'+str(len(matches)):matches})
	return new_teams

	
pairs = init_pairs(teams)
for i in range(round_number-1):
	teams = round(pairs)
	pairs = create_pairs(teams)

print()	
print("playoff:")
for round in playoff:
	print(round, ":")
	for match in playoff.get(round):
		print(match)

print()
print("winner is ", teams[0])

while True:
	team = input()
	if not team:
		quit()
	for round in playoff:
		for match in playoff.get(round):
			if (team in match.values()):
				print(round, match)
