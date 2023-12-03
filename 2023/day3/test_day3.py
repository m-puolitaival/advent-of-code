import pytest
import day3 as app

test_input = [
  "467..114..",
  "...*......",
  "..35..633.",
  "......#...",
  "617*......",
  ".....+.58.",
  "..592.....",
  "......755.",
  "...$.*....",
  ".664.598..",
]

def test_part1():
  assert app.part1(test_input) == 4361

def test_part2():
  assert app.part2(test_input) == 467835