import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    totalCards = 0

    cardCounts = [1 for l in range(1, 198)]
    cardNum = 1
    for line in lines:
        matches = 0
        cardAndParts = line.split(": ")
        parts = cardAndParts[1].split(" | ")
        winningNums = parts[0].split()
        myNums = parts[1].split()

        print(winningNums)
        print(myNums)
        winningNumMap = {}
        for winningNum in winningNums:
            winningNumMap[winningNum] = 0
        for num in myNums:
            if num in winningNumMap:
                matches += 1
        # generate more scratch cards

        copies = cardCounts[cardNum - 1]
        for i in range(cardNum, (cardNum - 1) + matches + 1):
            cardCounts[i] += 1 * copies
        cardNum += 1
    print(cardCounts)
    print(sum)
    return sum(cardCounts)

# TODO: change for the small example given
INPUT_S = '''\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''
EXPECTED = 30


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
