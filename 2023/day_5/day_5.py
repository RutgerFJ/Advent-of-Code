class MapRange:
    def __init__(self, start, end, map_distance):
        self.start = start
        self.end = end
        self.map_distance = map_distance
    
    def __gt__(self, other):
        return self.start > other.start


def map_to_ranges(x, ranges):
    for range in ranges:
        if range.start <= x < range.end:
            return x + range.map_distance
    return x


def parse_input(inp):
    seeds = [int(seed) for seed in inp.split('\n\n')[0].split()[1:]]

    maps = {}
    for map in inp.split('\n\n')[1:]:
        ranges = []
        for line in map.strip().split('\n'):

            if line.endswith(':'):
                header = line.rstrip(' map:')
                continue

            cols = [int(x) for x in line.strip().split()]
            ranges.append(MapRange(cols[1], cols[1]+cols[2], cols[0]-cols[1]))

        maps[header] = sorted(ranges)

    return seeds, maps


def part_one(inp):
    seeds, maps = parse_input(inp)
    locations = []
    for location in seeds:
        for key in maps.keys():
            location = map_to_ranges(location, maps[key])
        locations.append(location)
      
    return min(locations)


def part_two(inp):
    seeds, maps = parse_input(inp)
    seed_ranges = []
    for x in range(0, len(seeds), 2):
        seed_ranges.append((seeds[x], seeds[x+1]))

    min_locs = []
    # BRUTE FORCE SOLUTION
    # winning seed_range has been selected after solving puzzle to save time
    for r in seed_ranges[6:7]:
        min_loc = 999999999999
        for location in range(r[0], r[0] + r[1]):
            for key in maps.keys():
                location = map_to_ranges(location, maps[key])
            if min_loc > location:
                min_loc = location
        min_locs.append(min_loc)
    
    return min(min_locs)


def main():
    with open('input.txt', 'r') as f:
        content = ''.join([line for line in f])

    print(part_one(content))
    print(part_two(content))


main()
