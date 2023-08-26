import datetime
import os
from functools import partialmethod

import pytest
from main import Birthday


@pytest.fixture(name="birthday")
def fixture_birthday(monkeypatch, tmp_path):
    # Mock save_json_file() to use a specific path.
    path = tmp_path / "birthday.jsonl"
    mock_save_json_file = partialmethod(Birthday.save_json_file, path=path)

    monkeypatch.setattr(Birthday, "save_json_file", mock_save_json_file)

    return Birthday(name="lili", birthday=datetime.date(1994, 8, 20), save=True)


def test_file_creation(birthday, tmp_path):
    birthday.run()
    assert os.path.exists(path=tmp_path / "birthday.jsonl")
