import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    colorMaxes = {"red": 12, "green": 13, "blue": 14}
    lines = s.splitlines()
    validGames = []
    for line in lines:
        gameAndParts = line.split(": ")
        gameId = gameAndParts[0].split()[1]
        parts = gameAndParts[1]
        validGame = True 

        # each random turn
        sets = parts.split(";")

        for i in range(0, len(sets)):
            print("gameId", gameId, "setId", i, "set", sets[i])
            # array of nums/colors
            handfuls = sets[i].split(",")
            for j in range(0, len(handfuls)):
                num, color = handfuls[j].strip().split(" ")
                if int(num) > colorMaxes[color]:
                    validGame = False
        if validGame:
            validGames.append(gameId)
    print(validGames)
    sum = 0
    for vGame in validGames:
        sum += int(vGame)
    return sum

# TODO: change for the small example given
INPUT_S = '''\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''
EXPECTED = 8


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
