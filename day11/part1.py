import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def mihoy():
    return False

def solve(s: str) -> int:
    lines = s.splitlines()

    rows = [mihoy() for _ in range(len(lines))]
    cols = [mihoy() for _ in range(len(lines[0]))]
    coords = [] # array of x/y positions of galaxies
    shortest_paths = []

    # check which rows need to be expanded
    for i in range(0, len(lines)):
        needs_to_expand = True
        for j in range(0, len(lines[i])):
            if lines[i][j] == "#":
                needs_to_expand = False
        if needs_to_expand:
            rows[i] = True
    
    # transpose this shit, dawg
    transposed_lines = [''.join(row) for row in zip(*lines)]

    # check the columns which need to be expanded ez clap
    for i in range(0, len(transposed_lines)):
        needs_to_expand = True
        for j in range(0, len(transposed_lines[i])):
            if transposed_lines[i][j] == "#":
                needs_to_expand = False
        if needs_to_expand:
            cols[i] = True

    # expand the mf galaxy for the rows
    i = 0
    while i < len(lines) - 1:
        if rows[i] == True:
            # add some fkin space
            if i == 0:
                lines.insert(0, "." * len(lines[i]))
                rows.insert(i, True)
                i = i + 2
            else:
                lines.insert(i, "." * len(lines[i]))
                rows.insert(i, True)
                i = i + 2
        i += 1

    # transpose the expanded galaxy from the rows again bitchass
    transposed_lines = [''.join(row) for row in zip(*lines)]

    # expand the mf galaxy for the columns
    i = 0
    while i < len(transposed_lines) - 1:
        if cols[i] == True:
            # add some fkin space
            if i == 0:
                transposed_lines.insert(0, "." * len(transposed_lines[i]))
                cols.insert(i, True)
                i = i + 2
            else:
                transposed_lines.insert(i, "." * len(transposed_lines[i]))
                cols.insert(i, True)
                i = i + 2
        i += 1

    # transpose that bitch back again final time
    universe = [''.join(row) for row in zip(*transposed_lines)]

    # get the mf coords of those galaxies you son of a -
    for i in range(0, len(universe)):
        for j in range(0, len(universe[i])):
            if universe[i][j] == "#":
                coords.append([j, i])

    # then do taxi cab geometry mother fuckers
    for galaxy1 in range(0, len(coords)):
        for galaxy2 in range(galaxy1 + 1, len(coords)):
            x1 = coords[galaxy1][0]
            x2 = coords[galaxy2][0]
            y1 = coords[galaxy1][1]
            y2 = coords[galaxy2][1]
            shortest_paths.append(abs(x1 - x2) + abs(y1 - y2))

    return sum(shortest_paths)

# TODO: change for the small example given
INPUT_S = '''\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''
EXPECTED = 374


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    main()
