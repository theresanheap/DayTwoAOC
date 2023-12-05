with open('DayTwoAOC/daytwo.txt', 'r') as f:
    lines = f.readlines()

    new_dict = {}

    for line in lines:
        key, values = map(str.strip, line.split(':'))
        key_without_game = key.replace("Game", "").strip()
        game_values = [item.strip() for item in values.replace(',', ';').split(';')]

        color_counts = {}
        for item in game_values:
            count, color = item.split()
            count = int(count)
            color_counts[color] = color_counts.get(color, 0) + count

        sorted_colors = sorted(color_counts.items(), key=lambda x: (-x[1], x[0]))

        sorted_values = [f"{count} {color}" for color, count in sorted_colors]

        new_dict[key_without_game] = sorted_values

print(new_dict)

# 12 red cubes, 13 green cubes, and 14 blue cube