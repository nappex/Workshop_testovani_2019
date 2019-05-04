from math import pi
from elipsa import area_elipsa


def test_elipsa_surface():
    assert area_elipsa(1, 1) == pi
