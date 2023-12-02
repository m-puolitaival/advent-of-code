import pytest
import day1 as app

def test_part1():
  test_input = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
  ]
  assert app.part1(test_input) == 142

def test_part2():
  test_input = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
  ]
  assert app.part2(test_input) == 281
