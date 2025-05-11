from unittest.mock import patch

from src.compute import long_function


def test_long_function() -> None:
    with patch("time.sleep", return_value=None):
        result = long_function()

    assert result == "Uwu"
