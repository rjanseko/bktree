#!/usr/bin/python3.7
import pytest
from bktree import BKTree, hamming_distance




def test_hamming_distance():
    a = '10111100'
    b = '01001110'
    c = '00110011'
    assert hamming_distance(a, b) ==  5
    assert hamming_distance(b, c) == 6
    assert hamming_distance(c, a) == 5


def test_bktree():
    pass


