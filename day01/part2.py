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
            else:
                # check what number it is
                # bunch of ifs
                if line[i:i+3] == "one":
                    digits.append("1")
                elif line[i:i+3] == "two":
                    digits.append("2")
                elif line[i:i+5] == "three":
                    digits.append("3")
                elif line[i:i+4] == "four":
                    digits.append("4")
                elif line[i:i+4] == "five":
                    digits.append("5")
                elif line[i:i+3] == "six":
                    digits.append("6")
                elif line[i:i+5] == "seven":
                    digits.append("7")
                elif line[i:i+5] == "eight":
                    digits.append("8")
                elif line[i:i+4] == "nine":
                    digits.append("9")
        if len(digits) == 1:
            digits.append(digits[0])
        sum += int(digits[0] + digits[-1])
    return sum

# TODO: change for the small example given
INPUT_S = '''\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''
EXPECTED = 281


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
