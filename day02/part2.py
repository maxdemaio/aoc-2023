import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    powers = []

    # iterate over each game
    for line in lines:
        gameAndParts = line.split(": ")
        gameId = gameAndParts[0].split()[1]
        parts = gameAndParts[1]

        maxRed = 0
        maxGreen = 0
        maxBlue = 0
        # iterate over each turn in the game
        sets = parts.split(";")
        for i in range(0, len(sets)):
            print("gameId", gameId, "setId", i, "set", sets[i])
            # array of nums/colors
            handfuls = sets[i].split(",")
            for j in range(0, len(handfuls)):
                num, color = handfuls[j].strip().split(" ")
                if color == "red":
                    maxRed = max(maxRed, int(num))
                if color == "green":
                    maxGreen = max(maxGreen, int(num))
                if color == "blue":
                    maxBlue = max(maxBlue, int(num))
        powers.append(maxRed * maxGreen * maxBlue)
    sum = 0
    for power in powers:
        sum += power
    return sum

# TODO: change for the small example given
INPUT_S = '''\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''
EXPECTED = 2286


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
