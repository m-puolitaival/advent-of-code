import sys 

f = open("input.txt", "r").read().split("\n")

def part1(input):
  route = list(input[0])
  nodes = [
    {
      "n": x.split("=")[0].strip(),
      "L": x.split("=")[1].replace(" ", "").split(",")[0].strip("("),
      "R": x.split("=")[1].replace(" ", "").split(",")[1].strip(")")
    }
    for x in input[1:]
    if x != ""
  ]
  i = [x["n"] for x in nodes].index("AAA")
  steps = 0
  while nodes[i]["n"] != "ZZZ":
    ro = route[steps % len(route)]
    i = [x["n"] for x in nodes].index(nodes[i][ro])
    steps += 1
  return steps

def part2(input):
  return 0

result1 = part1(f)
result2 = part2(f)

print("Part 1 result:", result1)
print("Part 2 result:", result2)
