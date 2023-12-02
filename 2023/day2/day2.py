import sys

f = open("input.txt", "rt").readlines()

cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def part1(input):
  sum = 0
  for line in input:
    is_valid = True
    game_id = line.split(":")[0].strip("Game ")
    for round in line.split(":")[1].split(";"):
      for cube in round.split(","):
        number = cube.strip().split(" ")[0]
        color = cube.strip().split(" ")[1]
        if cubes[color] < int(number):
          is_valid = False
    if is_valid:
      sum += int(game_id)
  return sum


def part2(input):
  sum = 0
  for line in input:
    round_cubes = {
      "red": 0,
      "green": 0,
      "blue": 0,
    }
    for round in line.split(":")[1].split(";"):
      for cube in round.split(","):
        number = cube.strip().split(" ")[0]
        color = cube.strip().split(" ")[1]
        if round_cubes[color] < int(number):
          round_cubes[color] = int(number)
    sum += round_cubes["red"] * round_cubes["green"] * round_cubes["blue"]
  return sum


result1 = part1(f)
result2 = part2(f)

print("Part 1 result:", result1)
print("Part 2 result:", result2)
