import pytest

from pytestpractice.calc import add, divide, get_user_name, multiply, subtract


@pytest.mark.simple
def test_add(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 15


@pytest.mark.simple
def test_subtract(sample_numbers):
    a, b = sample_numbers
    assert subtract(a, b) == 5


@pytest.mark.simple
def test_multiply(sample_numbers):
    a, b = sample_numbers
    assert multiply(a, b) == 50


@pytest.mark.edge
def test_divide():
    assert divide(10, 5) == 2.0


@pytest.mark.edge
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_spi(mocker):
    mock_client = mocker.Mock()
    mock_client.fetch_user.return_value = {"name": "kaviya", "age": 20}
    name = get_user_name(mock_client, 1)
    assert name == "kaviya"

def test_temp(tmp_path):
    p1=tmp_path/"sample.txt"
    p1.write_text("sample file")
    print(p1)
    assert p1.read_text() == "sample file"


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected