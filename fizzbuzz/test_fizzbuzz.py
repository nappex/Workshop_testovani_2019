#  1) jak je cislo delitelne tremi beze zbytku tak vypis Fizz
#  2) kdyz je cislo delitelne peti beze zbytku vypis buzz
#  3) cislo je delitelne 3 a 5 fizzbuzz
#  4) cislo neni delitelne ani 3 ani 5 vypis cislo
from fizzbuzz import fizzbuzz


def test_return_number():
    assert fizzbuzz(1) == 1


def test_return_fizz():
    assert fizzbuzz(3) == "fizz"


def test_return_buzz():
    assert fizzbuzz(5) == "buzz"


def test_return_fizzbuzz():
    assert fizzbuzz(15) == "fizzbuzz"
