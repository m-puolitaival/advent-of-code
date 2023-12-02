import sys

f = open("input.txt", "rt").readlines()

digits = {
  "zero" : 0,
  "one"  : 1,
  "two"  : 2,
  "three": 3,
  "four" : 4,
  "five" : 5,
  "six"  : 6,
  "seven": 7,
  "eight": 8,
  "nine" : 9,
}

def get_digit(word):
  if word[0].isdigit():
    return word[0]

  d = next(filter(word.startswith, digits), None)
  return digits.get(d, 0)

def part1(input):
  sum = 0
  for line in input:
    for i in range(len(line)):
      if line[i].isdigit():
        first = int(line[i])
        break
    for i in range(len(line)-1, -1, -1):
      if line[i].isdigit():
        last = int(line[i])
        break
    sum += 10 * first + last
  return sum

def part2(input):
  sum = 0
  for line in input:
    for i in range(len(line)):
      first = get_digit(line[i:])
      if first:
        break
    for i in range(len(line)-1, -1, -1):
      last = get_digit(line[i:])
      if last:
        break
    sum += 10 * int(first) + int(last)
  return sum

result1 = part1(f)
result2 = part2(f)

print("Part 1 result:", result1)
print("Part 2 result:", result2)
