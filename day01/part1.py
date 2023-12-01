import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    sum = 0

    for line in lines:
        digits = []
        for i in range(0, len(line)):
            if line[i].isdigit():
                digits.append(line[i])
        if len(digits) == 1:
            digits.append(digits[0])
        sum += int(digits[0] + digits[-1])
    return sum

# TODO: change for the small example given
INPUT_S = '''\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''
EXPECTED = 142


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    test()
