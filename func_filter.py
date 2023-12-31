numbers = [1,2,3,4,5]

# filter con listas
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)

# filter con dict
matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Uruguay',
        'home_team_score': 3,
        'away_team_score': 1,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Mexico',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'
    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Chile',
        'away_team': 'Argentina',
        'home_team_score': 1,
        'away_team_score': 3,
        'home_team_result': 'Lose'
    }
]

# print(matches)
print(len(matches))

new_list = list(filter(lambda x: x["home_team_result"] == 'Win', matches))
print(new_list)
print(len(new_list))