import pytest

from fizzbuzz import fizzbuzz

def test_1_returns_1():
    actual = fizzbuzz(1)
    expected = 1
    assert expected == actual

def test_2_returns_2():
    actual = fizzbuzz(2)
    expected = 2
    assert expected == actual

def test_3_returns_fizz():
    actual = fizzbuzz(3)
    expected = "fizz"
    assert expected == actual

def test_5_returns_buzz():
    actual = fizzbuzz(5)
    expected = "buzz"
    assert expected == actual

def test_6_returns_fizz():
    actual = fizzbuzz(6)
    expected = "fizz"
    assert expected == actual

def test_9_returns_fizz():
    actual = fizzbuzz(9)
    expected = "fizz"
    assert expected == actual

def test_10_returns_buzz():
    actual = fizzbuzz(10)
    expected = "buzz"
    assert expected == actual

def test_15_returns_fizzbuzz():
    actual = fizzbuzz(15)
    expected = "fizzbuzz"
    assert expected == actual

def test_30_returns_fizzbuzz():
    actual = fizzbuzz(30)
    expected = "fizzbuzz"
    assert expected == actual

def test_45_returns_fizzbuzz():
    actual = fizzbuzz(45)
    expected = "fizzbuzz"
    assert expected == actual
