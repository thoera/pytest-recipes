from unittest.mock import patch

import pandas as pd
import pytest
from main import max_in_columns


@patch("pandas.read_csv")
def test_max_in_columns(mock_read_csv):
    mock_read_csv.return_value = pd.DataFrame({"a": [2, 0, 0, 8], "b": [1, 2, 3, 4]})
    assert max_in_columns(filename="mock_file") == {"a": 8, "b": 4}


@pytest.fixture
def mock_read_csv(test_input):
    with patch("pandas.read_csv", return_value=test_input):
        yield


@pytest.mark.usefixtures("mock_read_csv")
@pytest.mark.parametrize(
    "test_input, expected",
    [
        (pd.DataFrame(data={"a": [None], "b": [None]}), {"a": None, "b": None}),
        (pd.DataFrame(data={"a": [2, 0, 0, 8], "b": [1, 2, 3, 4]}), {"a": 8, "b": 4}),
    ],
)
def test_max_in_columns_wt_fixture(test_input, expected):
    assert max_in_columns(filename=test_input) == expected
