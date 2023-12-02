def parse_game_string(game_str):
    try:
        parts = game_str.split(':')

        right_part = parts[1].strip()
        color_blocks = right_part.split(';')

        max_red = 0
        max_green = 0
        max_blue = 0

        for color_block in color_blocks:
            color_count_pairs = [pair.strip().split() for pair in color_block.split(',')]

            for pair in color_count_pairs:
                count = int(pair[0])
                color = pair[1]

                if color == 'red':
                    max_red = max(max_red, count)
                elif color == 'green':
                    max_green = max(max_green, count)
                elif color == 'blue':
                    max_blue = max(max_blue, count)

        return max_red * max_green * max_blue
    except ValueError as e:
        print(f"Error parsing line: {game_str}. Error: {e}")
        return 0
    except Exception as e:
        print(f"Unexpected error parsing line: {game_str}. Error: {e}")
        return 0

def main(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            total_sum += parse_game_string(line)

    print("Total Sum of Max Counts Products:", total_sum)

file_path = 'Day02_part1.txt'
main(file_path)

