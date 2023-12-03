import sys
import re
import math
from itertools import chain

f = open("input.txt", "rt").read().split("\n")

def check_parts(lines, index, start, end):
  return any(
    re.findall(r"[^0-9.]", line[max(0, start - 1):min(len(lines[index]), end + 1)]) 
    for line in lines[max(0, index - 1):min(len(lines), index + 2)]
  )

def get_gear_parts(lines, index, start):
  gear_parts = []
  for line in lines[max(0, index - 1):min(len(lines), index + 2)]:
    for match in re.finditer(r"\d+", line[max(0, start - 1):min(len(lines[index]), start + 2)]):
      for match in re.finditer(f"\d*{match.group()}\d*", line[max(0, start-3):min(len(lines[index]), start+4)]):
        if match.start() in [5,6] or match.end() in [1,2]:
          continue
        else:
          gear_parts.append(re.findall(f"\d*{match.group()}\d*", line[max(0, start-3):min(len(lines[index]), start+4)]))
  return gear_parts

def part1(input):
  sum = 0
  for index, line in enumerate(input):
    for match in re.finditer(r"\d+", line):
      if check_parts(input, index, match.start(), match.end()):
        sum += int(match.group())
  return sum

def part2(input):
  gears = []
  for index, line in enumerate(input):
    for match in re.finditer(r"\*", line):
      gears.append(list(set(chain(*get_gear_parts(input, index, match.start())))))
  return sum(math.prod(map(int,gear)) for gear in gears if len(gear) == 2)

result1 = part1(f)
result2 = part2(f)

print("Part 1 result:", result1)
print("Part 2 result:", result2)