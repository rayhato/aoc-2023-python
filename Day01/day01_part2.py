def convert_to_digits(line):
    word_to_number = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    block_size = 5
    index = 0
    converted_line = ""

    while index < len(line):
        block = line[index:index + block_size]

        longest_match = None
        for i in range(len(block), 0, -1):
            potential_match = block[:i]
            if potential_match in word_to_number and (not longest_match or block.find(potential_match) == i - len(potential_match)):
                longest_match = potential_match

        if longest_match:
            converted_line += word_to_number[longest_match][0] + block[1:]
            index += len(longest_match) - 1  
        else:
            converted_line += line[index]
            index += 1

    return converted_line

def process_line(line):
    converted_line = convert_to_digits(line)

    first_digit = None
    second_digit = None

    for char in converted_line:
        if char.isdigit():
            first_digit = char
            break

    if first_digit is not None:
        reversed_line = converted_line[::-1]
        for char in reversed_line:
            if char.isdigit():
                second_digit = char
                break

    if first_digit is not None and second_digit is not None:
        two_digit_number = int(first_digit + second_digit)
        print(f"Original Line: {line.strip()}, Converted Line: {converted_line.strip()}, Two-digit Number: {two_digit_number}")

        return two_digit_number
    else:
        return 0


def main():
    file_path = 'day01_part2.txt'
    total_sum = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                two_digit_number = process_line(line)
                total_sum += two_digit_number

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

    print(f"Total Sum: {total_sum}")


if __name__ == "__main__":
    main()
