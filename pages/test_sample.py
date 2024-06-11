import pytest


def test_my1(messages):
    print("Number1")


@pytest.mark.run(order=1)
def test_my2():
    print('Number2')
