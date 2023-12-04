import sys
from collections import defaultdict

f = open("input.txt", "rt").read().split("\n")

def part1(input):
  total_sum = 0
  for line in input:
    win_nums, nums = line.split(": ")[1].split(" | ")
    count = sum(w in nums.split() for w in win_nums.split())
    total_sum += 2**(count-1) if count else 0
  return total_sum

def part2(input):
  rounds = 0
  cards = defaultdict(list)
  for line in input:
    cards[int(line.split(":")[0].split()[1])] = {
      "num_of_cards": 1,
      "win_nums": line.split(": ")[1].split(" | ")[0].split(),
      "nums": line.split(": ")[1].split(" | ")[1].split()
    }
  for card in cards:
    for _ in range(cards[card]["num_of_cards"]):
      rounds += 1
      match_count = sum(w in cards[card]["nums"] for w in cards[card]["win_nums"])
      for wn in range(card+1, card+match_count+1):
        cards[wn]["num_of_cards"] += 1
  return rounds

result1 = part1(f)
result2 = part2(f)

print("Part 1 result:", result1)
print("Part 2 result:", result2)
