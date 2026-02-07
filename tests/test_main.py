"""Tests for shellies_discovery_gen2.py."""

import json
import sys
import types
from importlib import util
from pathlib import Path
from unittest.mock import Mock

import pytest
from syrupy import SnapshotAssertion

SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "python_scripts"
    / "shellies_discovery_gen2.py"
)
FIXTURES_PATH = Path(__file__).resolve().parent / "fixtures"
MODULE_NAME = "python_scripts.shellies_discovery_gen2"


def run_script(*, data, logger, hass=None):
    """Load and execute the script as a module for coverage."""
    if MODULE_NAME in sys.modules:
        del sys.modules[MODULE_NAME]

    if "python_scripts" not in sys.modules:
        package = types.ModuleType("python_scripts")
        package.__path__ = [str(SCRIPT_PATH.parent)]
        sys.modules["python_scripts"] = package

    spec = util.spec_from_file_location(MODULE_NAME, SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load module spec for shellies_discovery_gen2")

    module = util.module_from_spec(spec)
    module.data = data
    module.logger = logger
    if hass is not None:
        module.hass = hass
    sys.modules[MODULE_NAME] = module
    spec.loader.exec_module(module)
    return module

def test_none_device_id() -> None:
    """Test that the script raises a ValueError when the device id is None."""
    logger = Mock()
    data = {"id": None}

    with pytest.raises(
        ValueError, match="id value None is not valid, check script configuration"
    ):
        run_script(logger=logger, data=data)


def test_unsupported_model() -> None:
    """Test that the script raises a ValueError for unsupported models."""
    logger = Mock()
    data = {"id": "unsupported-1234"}

    with pytest.raises(
        ValueError,
        match="model unsupported is not supported, please open a feature request",
    ):
        run_script(logger=logger, data=data)


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
        run_script(logger=logger, data=data)


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
        run_script(logger=logger, data=data)


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
        run_script(logger=logger, data=data)


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
        run_script(logger=logger, data=data)


def test_shelly_1_gen4(snapshot: SnapshotAssertion) -> None:
    """Test for Shelly 1 Gen4."""
    logger = Mock()
    hass = Mock()
    hass.services = Mock()
    fixture_path = FIXTURES_PATH / "shelly_1_gen4.json"
    data = json.loads(fixture_path.read_text())

    result = run_script(logger=logger, data=data, hass=hass)

    assert result.config_data
    assert hass.services.call.called

    for call in range(len(hass.services.call.call_args_list)):
        if payload := hass.services.call.call_args_list[call][0][2].get("payload"):
            assert json.loads(payload) == snapshot

def test_shelly_plug_m_gen3(snapshot: SnapshotAssertion) -> None:
    """Test for Shelly Plug M Gen3."""
    logger = Mock()
    hass = Mock()
    hass.services = Mock()
    fixture_path = FIXTURES_PATH / "shelly_plug_m_gen3.json"
    data = json.loads(fixture_path.read_text())

    result = run_script(logger=logger, data=data, hass=hass)

    assert result.config_data
    assert hass.services.call.called

    for call in range(len(hass.services.call.call_args_list)):
        if payload := hass.services.call.call_args_list[call][0][2].get("payload"):
            assert json.loads(payload) == snapshot

def test_shelly_blu_rc_button_4_zb(snapshot: SnapshotAssertion) -> None:
    """Test for Shelly BLU RC Button 4 ZB."""
    logger = Mock()
    hass = Mock()
    hass.services = Mock()
    fixture_path = FIXTURES_PATH / "shelly_blu_rc_button_4_zb.json"
    data = json.loads(fixture_path.read_text())

    result = run_script(logger=logger, data=data, hass=hass)

    assert result.config_data
    assert hass.services.call.called

    for call in range(len(hass.services.call.call_args_list)):
        if payload := hass.services.call.call_args_list[call][0][2].get("payload"):
            assert json.loads(payload) == snapshot
