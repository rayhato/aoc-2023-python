def get_full_number(x, y, schematic, searched):
    # Find first digit and last digit of part number
    y_min, y_max = y, y
    while y_min - 1 >= 0 and schematic[x][y_min - 1].isdigit():
        y_min -= 1
    while y_max < len(schematic[x]) and schematic[x][y_max].isdigit():
        y_max += 1

    # It is needed to filter out doubles as a part number might be visited twice.
    # Hence the need to return a 0 and filter it out later.
    # Yes, I know ... could be optimized to stop looking earlier and not use a 0, stop nagging mom(!).
    number = '0'
    if [x, y_min, y_max] not in searched:
        number = ''.join(schematic[x][y_min:y_max])
        searched.append([x, y_min, y_max])

    return int(number)


# Find all adjacent numbers for a part.
def adjacent_numbers(i, j, schematic, searched):
    numbers = []
    for x in range(-1, 1 + 1):
        for y in range(-1, 1 + 1):
            if schematic[i + x][j + y].isdigit():
                number = get_full_number(i + x, j + y, schematic, searched)
                if number != 0:
                    numbers.append(number)

    return numbers

def solve(data, gears=False):
    schematic = [[c for c in line] for line in data.split('\n')]

    # Find all parts by part symbol together with their adjacent numbers.
    searched, parts = [], []
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if not schematic[i][j].isdigit() and schematic[i][j] != '.':
                parts.append([schematic[i][j], adjacent_numbers(i, j, schematic, searched)])

    if gears:
        # For gears, first calculate the gear ratios (product) and then sum those.
        return sum([part[1][0] * part[1][1] for part in parts if part[0] == '*' and len(part[1]) == 2])
    else:
        # Make the sum of all numbers of the parts
        return sum([sum(part[1]) for part in parts])

# Replace with your actual file paths
test_file_path = 'Day03_sample.txt'
puzzle_file_path = 'Day03_input.txt'

with open(test_file_path, 'r') as file:
    test_input = file.read()

with open(puzzle_file_path, 'r') as file:
    puzzle_input = file.read()

print("Part 1")
p1_test_result = solve(test_input)
print(f"Test solution: {p1_test_result}")
p1_result = solve(puzzle_input)
print(f"Puzzle solution: {p1_result} \n")

print("Part 2")
p2_test_result = solve(test_input, True)
print(f"Test solution: {p2_test_result}")
p2_result = solve(puzzle_input, True)
print(f"Puzzle solution: {p2_result}")
