import pytest

from pyprime.sieves import sundaram_sieve


def test_Throws_When_GivenNegativeNumber():
    with pytest.raises(ValueError):
        list(sundaram_sieve(-1))


# TODO: move to external file
@pytest.mark.parametrize("test_input,expected", [
    (2, [2]),
    (5, [2, 3, 5]),
    (50, [2,
          3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]),
])
def test_Correctly_Works(test_input: int, expected: [int]):
    result = list(sundaram_sieve(test_input))

    assert result == expected
