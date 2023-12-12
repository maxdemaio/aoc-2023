import os.path
import copy

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def create_new_dict():
    return {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0,
            "T": 0, "J": 0, "Q": 0, "K": 0, "A": 0}


def solve(s: str) -> int:
    lines = s.splitlines()
    totalWinnings = 0

    freqMaps = [create_new_dict() for _ in range(5)]
    hands = []
    bids = []
    rankings = []

    for i in range(0, len(lines)):
        cards, bid = lines[i].split()
        hands.append(cards)
        bids.append(int(bid))

        print("cards", cards, "bid", bid)
        
        for j in range(0, len(cards)):
            freqMaps[i][cards[j]] += 1

    # freq maps have been populated, we need to rank them
    for map in freqMaps:
       print(max(map.values()))


    return totalWinnings

# TODO: change for the small example given
INPUT_S = '''\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''
EXPECTED = 6440


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    test()
