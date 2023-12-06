import sys
import math

f = open("input.txt", "rt").read().split("\n")

def part1(input):
  t = list(map(int, input[0].split(": ")[1].split()))
  d = list(map(int, input[1].split(": ")[1].split()))

  c = []
  for i in range(len(t)):
    x = sum(1 for j in range(t[i]) if j * (t[i] - j) > d[i])
    c.append(x)
  return math.prod(c)

def part2(input):
  t = int(input[0].split(":")[1].replace(" ", ""))
  d = int(input[1].split(":")[1].replace(" ", ""))
  
  start = next(i for i in range(t) if i * (t - i) > d)
  end = next(i for i in range(t, 0, -1) if i * (t - i) > d)
  
  return end - start + 1

result1 = part1(f)
result2 = part2(f)

print("Part 1 result:", result1)
print("Part 2 result:", result2)
