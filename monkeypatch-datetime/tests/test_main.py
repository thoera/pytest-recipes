import datetime as dt
from unittest.mock import patch

import pytest
from main import create_versioning_name


@patch("main.now")
@pytest.mark.parametrize(
    "date, expected",
    [
        (dt.date(2024, 8, 20), "20240820_000000"),
        (dt.date(1994, 8, 20), "19940820_000000"),
        (dt.datetime(2024, 8, 20), "20240820_000000"),
        (dt.datetime(2024, 8, 20, 18, 4, 32), "20240820_180432"),
        (None, "20240323_180820"),
    ],
)
def test_create_versioning_date(mock_now, date, expected):
    mock_now.return_value = dt.datetime(2024, 3, 23, 18, 8, 20)
    assert create_versioning_name(date=date) == expected
