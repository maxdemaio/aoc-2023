import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    gears = []  # To store the positions of gears (not all are used unless exactly 2 adjc nums)
    gear_counts = {}  # To count adjacent part numbers for each gear
    gear_part_numbers = {}  # To store adjacent part numbers for each gear
    total_ratio = 0

    # Step 1: Identify the positions of gears
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '*':
                gears.append((j, i))
                gear_part_numbers[str(j) + str(i)] = []
                gear_counts[str(j) + str(i)] = 0

    # Step 2: Identify the used gears and add adjacent part numbers for each gear
    # loop over each line
    for i in range(0, len(lines)):
        # loop over each char in line
        j = 0
        while j < len(lines[i]):
            myChar = lines[i][j]
            possibleNum = ""
            possibleNumAdj = False
            gearsToAdd = set() # list of gears this num is adjacent to

            while myChar.isdigit():
                # check if any nearby
                for gear in gears:
                    x = gear[0]
                    y = gear[1]
                    # 1 x/y away
                    if (x == j and abs(y - i) == 1) or (y == i and abs(x - j) == 1) or (abs(x - j) == 1 and abs(y - i) == 1):
                        possibleNumAdj = True
                        # a number in the part is adj to a gear
                        # add that gear to the list of gears the num is adj to
                        gearsToAdd.add(str(x) + str(y))
                possibleNum += myChar
                j += 1
                if j < len(lines[i]):
                    myChar = lines[i][j]
                else:
                    break  # Break out of the inner loop if j exceeds the length of the line

             # Update the frequency maps
            for gear in gearsToAdd:
                gear_counts[gear] += 1
                gear_part_numbers[gear].append(int(possibleNum))
            j += 1

    # Step 4: Calculate gear ratios
    # Iterate through keys in the frequency_map
    for key, value in gear_counts.items():
        # Check if the value is 2
        if value == 2:
            # Check if the key exists in the data_dict
            if key in gear_part_numbers:
                # Access the list of numbers and calculate their product
                product = 1
                for num in gear_part_numbers[key]:
                    product *= num
                # Add the product to the global sum
                total_ratio += product
    return total_ratio

# TODO: change for the small example given
INPUT_S = '''\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''
EXPECTED = 467835


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
