def parse_game_string(game_str, red_limit, green_limit, blue_limit):
    try:
        parts = game_str.split(':')
        game_id = parts[0].split(' ')[-1]

        right_part = parts[1].strip()
        color_blocks = right_part.split(';')

        for color_block in color_blocks:
            color_count_pairs = [pair.strip().split() for pair in color_block.split(',')]

            for pair in color_count_pairs:
                count = int(pair[0])
                color = pair[1]

                if (color == 'red' and count > red_limit) or \
                   (color == 'green' and count > green_limit) or \
                   (color == 'blue' and count > blue_limit):
                    return 0 

        return int(game_id)
    except ValueError as e:
        print(f"Error parsing line: {game_str}. Error: {e}")
        return 0
    except Exception as e:
        print(f"Unexpected error parsing line: {game_str}. Error: {e}")
        return 0

def main(file_path, red_limit, green_limit, blue_limit):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            total_sum += parse_game_string(line, red_limit, green_limit, blue_limit)

    print("Total Sum of Game IDs:", total_sum)

file_path = 'Day02_part1.txt'
red_limit = 12
green_limit = 13
blue_limit = 14
main(file_path, red_limit, green_limit, blue_limit)
