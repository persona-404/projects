import pytest
from calc import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-3) == 9
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")