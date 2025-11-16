import pytest
from assignment import decimal_to_binary, bank_simulation, Stack, Queue

@pytest.mark.parametrize("num,expected", [
    (0, "0"),
    (1, "1"),
    (4, "100"),
    (7, "111"),
    (13, "1101"),
    (32, "100000"),
])
def test1(num, expected):
    assert decimal_to_binary(num).strip() == expected.strip()

@pytest.mark.parametrize("customers,expected", [
    (["A"], "Serving: A"),
    (["Alice", "Bob", "Charlie"], "Serving: Alice\nServing: Bob\nServing: Charlie"),
    (["X", "Y"], "Serving: X\nServing: Y"),
    ([], ""),   # empty queue
])
def test2(customers, expected):
    assert bank_simulation(customers).strip() == expected.strip()
