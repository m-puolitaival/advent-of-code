import pytest
import day8 as app

test_input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

def test_part1():
  assert app.part1(test_input.split("\n")) == 2

def test_part2():
  pass
