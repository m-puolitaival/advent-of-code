import sys
import time

f = open("input.txt", "rt").read().split("\n")

def create_map(input, section):
  start = input.index(section) + 1
  end = start + input[start:].index("")
  map = [{"d": int(x.split()[0]), "s": int(x.split()[1]), "r": int(x.split()[2])} for x in input[start:end]]
  return map

def find_in_maps(seed, maps):
  for map in maps:
    if seed in range(map["s"], map["s"]+map["r"]):
      seed = map["d"] + range(map["s"], map["s"]+map["r"]).index(seed)
      return seed
  return seed

def part1(input):
  seeds = [int(x) for x in input[0].split(": ")[1].split()]
  lowest_seed = sys.maxsize
  maps = [
    create_map(input, "seed-to-soil map:"),
    create_map(input, "soil-to-fertilizer map:"),
    create_map(input, "fertilizer-to-water map:"),
    create_map(input, "water-to-light map:"),
    create_map(input, "light-to-temperature map:"),
    create_map(input, "temperature-to-humidity map:"),
    create_map(input, "humidity-to-location map:")
  ]
  
  for seed in seeds:
    for map in maps:
      seed = find_in_maps(seed, map)
    lowest_seed = min(seed, lowest_seed)
  
  return lowest_seed

def part2(input):
  pass

result1 = part1(f)
result2 = part2(f)

print("Part 1 result:", result1)
print("Part 2 result:", result2)
