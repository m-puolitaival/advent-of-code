import pytest
import day6 as app

test_input = [
"Time:      7  15   30",
"Distance:  9  40  200"
]

def test_part1():
  assert app.part1(test_input) == 288

def test_part2():
  assert app.part2(test_input) == 71503