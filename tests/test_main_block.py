"""Tests for shellies_discovery_gen2.py."""

import runpy
from pathlib import Path
from unittest.mock import Mock

import pytest


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "python_scripts"
    / "shellies_discovery_gen2.py"
)


def test_none_device_id() -> None:
    """Test that the script raises a ValueError when the device id is None."""
    logger = Mock()
    data = {"id": None}

    with pytest.raises(
        ValueError, match="id value None is not valid, check script configuration"
    ):
        runpy.run_path(str(SCRIPT_PATH), init_globals={"logger": logger, "data": data})
