import os.path
import math

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    i = 0
    times = []
    dists = []
    ways = [0, 0, 0, 0] # change to 4 0s for real solution

    for line in lines:
        if i == 0:
            # times
            times = [int(num) for num in " ".join(line.split()).split()[1:]]
            print(times)
        else:
            # distance
            dists = [int(num) for num in " ".join(line.split()).split()[1:]]
            print(dists)
        i += 1


    for x in range(0, len(times)):
        for held in range(0, times[x] + 1):
            # check all possibs
            distance = (times[x] - held) * held
            if distance > dists[x]:
                ways[x] += 1

    return math.prod(ways)

# TODO: change for the small example given
INPUT_S = '''\
Time:      7  15   30
Distance:  9  40  200
'''
EXPECTED = 288


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
