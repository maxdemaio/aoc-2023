import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    # array of arrays containing x, y positions (col, row)
    symbolPositions = []
    sum = 0

    # first pass get all the symbols
    # loop over line
    for y in range(0, len(lines)):
        # loop over each char in line
        for x in range(0, len(lines[y])):
            if lines[y][x] != "." and not lines[y][x].isdigit():
                symbolPositions.append([x, y])
    print(symbolPositions)

    # loop over each line
    for i in range(0, len(lines)):
        # loop over each char in line
        j = 0
        while j < len(lines[i]):
            myChar = lines[i][j]
            possibleNum = ""
            possibleNumAdj = False
            while myChar.isdigit():
                # check if any nearby
                for symPos in symbolPositions:
                    x = symPos[0]
                    y = symPos[1]
                    # 1 x/y away
                    if (x == j and abs(y - i) == 1) or (y == i and abs(x - j) == 1) or (abs(x - j) == 1 and abs(y - i) == 1):
                        possibleNumAdj = True
                        break
                possibleNum += myChar
                j += 1
                if j < len(lines[i]):
                    myChar = lines[i][j]
                else:
                    break  # Break out of the inner loop if j exceeds the length of the line
            if possibleNumAdj:
                sum += int(possibleNum)
            j += 1

    return sum


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
EXPECTED = 4361


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
