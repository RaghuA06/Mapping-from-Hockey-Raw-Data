# Raghu Alluri
# March 2020
"""
1. The function should now return a dictionary with team names as keys and the
points as the values.
2. Team names may be repeated in the file, and should be combined into one 
values list.
"""

from typing import TextIO, Dict, List


def get_game_dict(game_data: TextIO) -> Dict[str, List[int]]:
    """Return a dictionary containing the team name and a list of points
    earned in each game for each team in the open file game_data. 
    
    >>> input_file = open('sample_games.txt')
    >>> get_game_dict(input_file)
    {'Toronto Maple Leafs': [2, 2, 1, 0, 0, 2], 'Grande Prairie Storm': [], \
'Montreal Canadiens': [1, 2, 1, 0, 2]}
    >>> input_file.close()
    """
    hockey = {}
    raw_data = []
    for line in game_data:
        raw_data.append(line.strip())

    teams = []
    scores_list = []
    for i in range(len(raw_data)):
        if raw_data[i].isnumeric() == False and raw_data[i] not in teams:
            teams.append(raw_data[i])
            lst = []
            j = i + 1
            while j <= len(raw_data) - 1 and raw_data[j].isnumeric() == True:
                lst.append(int(raw_data[j]))
                j = j + 1
            scores_list.append(lst)
        elif raw_data[i].isnumeric() == False and raw_data[i] in teams:
            team_index = teams.index(raw_data[i])
            j = i + 1
            while j <= len(raw_data) - 1 and raw_data[j].isnumeric() == True:
                scores_list[team_index].append(int(raw_data[j]))
                j = j + 1
            

    for i in range(len(teams)):
        hockey[teams[i]] = scores_list[i]

    return hockey
            















    
 
