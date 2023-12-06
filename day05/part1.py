import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: str) -> int:
    lines = s.splitlines()
    seeds = []
    seedToSoilMap = {}
    soilToFertMap = {}
    fertToWaterMap = {}
    waterToLightMap = {}
    lightToTempMap = {}
    tempToHumidMap = {}
    humidToLocMap = {}

    # Maps are ordered in our input
    maps = [seedToSoilMap, soilToFertMap, fertToWaterMap, waterToLightMap, lightToTempMap, tempToHumidMap,
            humidToLocMap]
    locations = []

    # Populate maps
    mapIndex = -1
    for line in lines:
        if line.startswith("seeds:"):
            seeds = [int(seed) for seed in line.split("seeds: ")[1].split(" ")]
            continue
        if line == "":
            mapIndex += 1
            continue
        print(line)

    # Populate all possible locations
    for seed in seeds:
        locations.append(humidToLocMap[tempToHumidMap[
            lightToTempMap[waterToLightMap[fertToWaterMap[soilToFertMap[seedToSoilMap[seed]]]]]]])

    return min(locations)


# TODO: change for the small example given
INPUT_S = '''\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''
EXPECTED = 35


def test() -> None:
    assert solve(INPUT_S) == EXPECTED


def main() -> int:
    with open(INPUT_TXT) as f:
        print(solve(f.read()))
    return 0


if __name__ == '__main__':
    test()
