from collections import Counter

def tournamentWinner(competitions, results):
    # Write your code here.
	winner_team = []
	for i in range(len(results)):
		if results[i] == 0:
			winner = competitions[i][1]
			winner_team.append(winner)
		else:
			winner = competitions[i][0]
			winner_team.append(winner)

	win = Counter(winner_team)
	print(win)	
	print(max(zip(win.values(),win.keys()))[1])
    # return max(zip(win.values(),win.keys()))[1]
	return max(winner_team)


competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]

results = [0,0,1]

print(tournamentWinner(competitions,results))
