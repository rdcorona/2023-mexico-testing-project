import pytest
from logistic import f, iterate_f
from math import isclose
from numpy.testing import assert_array_almost_equal, assert_allclose
from numpy import array, random
# # set the random seed for once here
# SEED = random.randint(0, 2**31)
# @pytest.fixture
# def random_state():
#     print(f'Using seed {SEED}')
#     random_state = random.RandomState(SEED)
#     return random_state

@pytest.mark.parametrize("x, r, out",
    [
    (0.1, 2.2, 0.198),
    (0.2, 3.4, 0.544),
    (0.75, 1.7, 0.31875)])
def test_logistic(x, r, out):
    output = f(x, r)
    # Then
    assert isclose(output, out)


@pytest.mark.parametrize("it, x, r, out",
    [(1, 0.1, 2.2, [0.198]),
    (4, 0.2, 3.4, [0.544, 0.843418, 0.449019, 0.841163]),
    (2, 0.75, 1.7, [0.31875, 0.369152])])
def test_logistic_it(it, x, r, out):
    output = iterate_f(it, x, r)
    # Then
    # assert_array_almost_equal(output, out, decimal=3)
    assert_allclose(output, out, atol=1e6)


def test_logistic_it(random_state):
    # SEED = 1234567890
    # random_state = random.RandomState(SEED)
    it = 100
    output = iterate_f(it, random_state.rand(), 1.5)
    # Then
    # assert_array_almost_equal(output, out, decimal=3)
    assert isclose(output[-1], 1/3)