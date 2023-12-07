import pytest
import day7 as app

test_input = [
  "32T3K 765",
  "T55J5 684",
  "KK677 28",
  "KTJJT 220",
  "QQQJA 483",
]

def test_part1():
  assert app.part1(test_input) == 6440

def test_part2():
  assert app.part2(test_input) == 5905
