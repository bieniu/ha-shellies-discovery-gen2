"""Tests for shellies_discovery_gen2.py."""

import json
import runpy
from pathlib import Path
from unittest.mock import Mock
from syrupy import SnapshotAssertion
import pytest

SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "python_scripts"
    / "shellies_discovery_gen2.py"
)
FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "shelly_1_gen4.json"


def test_none_device_id() -> None:
    """Test that the script raises a ValueError when the device id is None."""
    logger = Mock()
    data = {"id": None}

    with pytest.raises(
        ValueError, match="id value None is not valid, check script configuration"
    ):
        runpy.run_path(str(SCRIPT_PATH), init_globals={"logger": logger, "data": data})


def test_unsupported_model() -> None:
    """Test that the script raises a ValueError for unsupported models."""
    logger = Mock()
    data = {"id": "unsupported-1234"}

    with pytest.raises(
        ValueError,
        match="model unsupported is not supported, please open a feature request",
    ):
        runpy.run_path(str(SCRIPT_PATH), init_globals={"logger": logger, "data": data})


def test_script_prefix_with_trailing_slash() -> None:
    """Test that the script rejects a script prefix ending with '/'."""
    logger = Mock()
    data = {
        "id": "shellyplus1-123456",
        "device_config": {},
        "script_prefix": "bad/prefix/",
    }

    with pytest.raises(
        ValueError,
        match="Script prefix value bad/prefix/ is not valid, check script configuration",
    ):
        runpy.run_path(str(SCRIPT_PATH), init_globals={"logger": logger, "data": data})


def test_invalid_qos() -> None:
    """Test that the script rejects invalid QoS values."""
    logger = Mock()
    data = {
        "id": "shellyplus1-123456",
        "device_config": {},
        "qos": 3,
    }

    with pytest.raises(
        ValueError, match="QoS value 3 is not valid, check script configuration"
    ):
        runpy.run_path(str(SCRIPT_PATH), init_globals={"logger": logger, "data": data})


def test_missing_mqtt_component() -> None:
    """Test that the script rejects device configs without MQTT component."""
    logger = Mock()
    data = {
        "id": "shellyplus1-123456",
        "device_config": {
            "components": [
                {"key": "bluetooth", "config": {}, "attrs": {}},
            ],
        },
    }

    with pytest.raises(
        ValueError,
        match="Missing MQTT component, probably 'Shelly.GetComponent' pagination problem",
    ):
        runpy.run_path(str(SCRIPT_PATH), init_globals={"logger": logger, "data": data})


def test_mqtt_prefix_with_space() -> None:
    """Test that the script rejects MQTT prefix values containing spaces."""
    logger = Mock()
    data = {
        "id": "shellyplus1-123456",
        "device_config": {
            "components": [
                {
                    "key": "mqtt",
                    "config": {"topic_prefix": "bad topic"},
                    "attrs": {},
                },
            ],
        },
    }

    with pytest.raises(
        ValueError,
        match="MQTT prefix value bad topic/ is not valid, check device configuration",
    ):
        runpy.run_path(str(SCRIPT_PATH), init_globals={"logger": logger, "data": data})


def test_shelly_1_gen4(snapshot: SnapshotAssertion) -> None:
    """Test for Shelly 1 Gen4."""
    logger = Mock()
    hass = Mock()
    hass.services = Mock()
    data = json.loads(FIXTURE_PATH.read_text())

    result = runpy.run_path(
        str(SCRIPT_PATH), init_globals={"logger": logger, "data": data, "hass": hass}
    )

    assert result["config_data"]
    assert hass.services.call.called

    for call in range(len(hass.services.call.call_args_list)):
        if payload := hass.services.call.call_args_list[call][0][2].get("payload"):
            assert json.loads(payload) == snapshot
