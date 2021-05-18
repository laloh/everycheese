import pytest

pytestmark = pytest.mark.django_db

from .factories import CheeseFactory


def test__str__():
    cheese = CheeseFactory(name="Stracchino")
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name
