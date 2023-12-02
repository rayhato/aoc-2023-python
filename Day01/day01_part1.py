def process_line(line):
    first_digit = None
    second_digit = None

    for char in line:
        if char.isdigit():
            first_digit = char
            break

    if first_digit is not None:
        reversed_line = line[::-1]
        for char in reversed_line:
            if char.isdigit():
                second_digit = char
                break

    if first_digit is not None and second_digit is not None:
        two_digit_number = int(first_digit + second_digit)
        print(f"Line: {line.strip()}, Two-digit Number: {two_digit_number}")

        return two_digit_number
    else:
        return 0


def main():
    file_path = 'day01_part1.txt'
    total_sum = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Process each line and accumulate the sum
                two_digit_number = process_line(line)
                total_sum += two_digit_number

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

    print(f"Total Sum: {total_sum}")


if __name__ == "__main__":
    main()

