import math
import os
import re

def task1():
    game_config = {
        'red' : 12,
        'green' : 13,
        'blue' : 14,
    }
    valid_game_ids = []

    # load input data
    with open(os.path.join(os.path.dirname(__file__), 'input'), 'r') as file:
        for line in file.readlines():
            game_id = line.split(':')[0].replace("Game ", "").strip()
            # print(game_id)
            games = line.split(':')[1].strip()
            game_results = {
                'red': [],
                'green': [],
                'blue': [],
            }
            for count, colour in re.findall(r'(\d+) (\w+)', games):
                # print("------" + game_id + "------")
                # print(count, colour)
                game_results[colour].append(int(count))
            # print(game_results)
            # if any of the individual game results are greater than the game_config, then the game is invalid
            if any(result > game_config[colour] for colour, results in game_results.items() for result in results):
                print(f"Game {game_id} is invalid")
            else:
                valid_game_ids.append(int(game_id))
    return sum(valid_game_ids)


def task2():
    prod_of_max = []

    # load input data
    with open(os.path.join(os.path.dirname(__file__), 'input'), 'r') as file:
        for line in file.readlines():
            game_id = line.split(':')[0].replace("Game ", "").strip()
            # print(game_id)
            games = line.split(':')[1].strip()
            game_results = {
                'red': [],
                'green': [],
                'blue': [],
            }
            for count, colour in re.findall(r'(\d+) (\w+)', games):
                game_results[colour].append(int(count))
            # get the max value for each colour
            max_values = [max(results) for results in game_results.values()]
            prod_of_max.append(math.prod(max_values))
            # print(math.prod(max_values))
    return sum(prod_of_max)


print(task1())
print(task2())