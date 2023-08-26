from unittest.mock import patch

import pytest
from main import AnimalFilter
from omegaconf import read_write


@pytest.fixture(scope="session")
def animals():
    return AnimalFilter()


def test_filter_animals(animals):
    with read_write(animals.config):
        with patch.object(animals.config, "animal", ["lion", "dog"]):
            assert animals.filter_animals() == ["lion"]


def test_filter_animals_empty(animals):
    with read_write(animals.config):
        with patch.object(animals.config, "animal", []):
            assert animals.filter_animals() == []


def test_number_above(animals):
    with read_write(animals.config):
        with patch.dict(animals.config.animal.dog, {"number": 2008}):
            assert animals.config.animal.dog.number > 100


def test_number_below(animals):
    with read_write(animals.config):
        with patch.dict(animals.config.animal.dog, {"number": 1}):
            assert animals.config.animal.dog.number < 5
