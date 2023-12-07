import sys

f = open("input.txt", "r").read().split("\n")

def score_hand(hand, hand_base, rank):
  c = {}
  for i in hand:
    if i not in c:
      c[i] = 0
    c[i] += 1

  s = sorted(c.values(), reverse=True)
  t = 0
  if s == [5]:
    t = 6
  elif s == [4,1]:
    t = 5
  elif s == [3,2]:
    t = 4
  elif s == [3,1,1]:
    t = 3
  elif s == [2,2,1]:
    t = 2
  elif s == [2,1,1,1]:
    t = 1
  
  base13 = 0
  for i, v in enumerate(hand_base):
    base13 += 13 ** (5 - i) * rank.index(v)

  return t, base13

def part1(input):
  r = "23456789TJQKA"
  hands = []
  for i in [i.split(" ") for i in input]:
    hands.append((score_hand(i[0], i[0], r), i[1]))
  
  total = 0
  for i, h in enumerate(sorted(hands), start=1):
    total += int(h[1]) * i
  return total

def part2(input):
  r = "J23456789TQKA"
  hands = []
  for i in [i.split(" ") for i in input]:
    if "J" in i[0]:
      hands.append((max([score_hand(i[0].replace("J", x), i[0], r) for x in i[0]]), i[1], i[0]))
    else:
      hands.append((score_hand(i[0], i[0], r), i[1], i[0]))

  total = 0
  for i, h in enumerate(sorted(hands), start=1):
    total += int(h[1]) * i
  return total

result1 = part1(f)
result2 = part2(f)

print("Part 1 result:", result1)
print("Part 2 result:", result2)
